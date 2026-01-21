import inspect
import logging
import os
from functools import wraps

import allure

SENSITIVE_ENV_KEYS = ("pass", "password", "pwd", "email", "login", "user", "username")


def is_sensitive_env_value(value):
    """Mask if value matches a sensitive ENV variable."""
    if value is None:
        return False
    for key in os.environ.keys():
        if any(s in key.lower() for s in SENSITIVE_ENV_KEYS):
            if os.environ[key] == value:
                return True
    return False


def mask_args(func, args, kwargs):
    """Mask secrets by actual values or ENV matches."""
    sig = inspect.signature(func)
    params = list(sig.parameters.values())

    masked_pos = []
    for i, val in enumerate(args):
        params[i].name if i < len(params) else ""

        if is_sensitive_env_value(val):
            masked_pos.append("***")
            continue

        masked_pos.append(val)

    masked_kw = {}
    for k, v in kwargs.items():
        if is_sensitive_env_value(v):
            masked_kw[k] = "***"
        else:
            masked_kw[k] = v

    return masked_pos, masked_kw


def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logger = logging.getLogger(self.__class__.__name__)

        masked_args, masked_kwargs = mask_args(func, args, kwargs)

        args_repr = ", ".join([repr(a) for a in masked_args] + [f"{k}={v!r}" for k, v in masked_kwargs.items()])

        logger.info(f"Calling: {func.__name__}({args_repr})")

        try:
            res = func(self, *args, **kwargs)
            logger.info(f"Completed: {func.__name__} — success")
            return res
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}")
            raise

    return wrapper


def allure_step(title=None):
    def decorator(func):
        step_title = title or func.__name__

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            masked_args, masked_kwargs = mask_args(func, args, kwargs)

            params = ", ".join([repr(a) for a in masked_args] + [f"{k}={v!r}" for k, v in masked_kwargs.items()])

            with allure.step(f"{step_title}({params})"):
                return func(self, *args, **kwargs)

        return wrapper

    return decorator


def allure_attach_on_fail(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            try:
                allure.attach(
                    self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass
            raise e

    return wrapper
