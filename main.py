from bot.bot import start_bot
from db.models import init_db

if __name__ == '__main__':
    init_db()
    start_bot()
