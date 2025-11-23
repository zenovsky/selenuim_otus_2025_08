import logging
from functools import wraps

import allure


def mask_value(value):
    if value is None:
        return None
    val = str(value).lower()
    if "pass" in val or "email" in val or "login" in val:
        return "***"
    return value


def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logger = logging.getLogger(self.__class__.__name__)

        masked_args = [repr(mask_value(a)) for a in args]
        masked_kwargs = [f"{k}={mask_value(v)!r}" for k, v in kwargs.items()]

        args_str = ", ".join(masked_args + masked_kwargs)

        logger.info(f"Calling: {func.__name__}({args_str})")

        try:
            result = func(self, *args, **kwargs)
            logger.info(f"Completed: {func.__name__} — success")
            return result
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}")
            raise

    return wrapper


def allure_step(title: str = None):

    def decorator(func):
        step_title = title or func.__name__

        @wraps(func)
        def wrapper(self, *args, **kwargs):

            params = ", ".join(
                [repr(a) for a in args] +
                [f"{k}={v!r}" for k, v in kwargs.items()]
            )

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
                png = self.driver.get_screenshot_as_png()
                allure.attach(
                    png,
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass

            raise e

    return wrapper
