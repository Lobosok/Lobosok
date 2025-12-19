# # Конфигурация бота и приложения

# import os
# from dotenv import load_dotenv

# load_dotenv()

# TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# DB_PATH = 'db/database.sqlite3'


##########################

# Конфигурация бота и приложения

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# --- ИСПРАВЛЕННЫЙ КОД ДЛЯ DB_PATH ---

# Определяем абсолютный путь к директории, где лежит текущий скрипт
# os.path.dirname(__file__) возвращает путь к папке, где находится этот файл конфигурации
basedir = os.path.dirname(os.path.abspath(__file__))

# Объединяем этот путь с относительным путем к файлу БД
DB_PATH = os.path.join(basedir, 'db', 'database.sqlite3')

# Теперь DB_PATH будет выглядеть как C:\Users\Kirill\Downloads\HRBOT_windows\db\database.sqlite3
# И Windows сможет его найти.
