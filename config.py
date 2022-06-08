from environs import Env
from sys import exit

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
IP = env.str("IP")

if not BOT_TOKEN:
    exit("Error: no token provided")
