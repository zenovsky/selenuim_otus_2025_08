import os

from dotenv import load_dotenv

load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if not ADMIN_EMAIL or not ADMIN_PASSWORD:
    raise ValueError("Учетные данные администратора (ADMIN_EMAIL или ADMIN_PASSWORD) " \
    "не найдены в переменных окружения или в файле .env")
