import os

from dotenv import load_dotenv
load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "5291894")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "e15ad5a64cb8bd39b2be463d0314295f") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5575648699:AAExfx8eHMWcvxubDIkpD0FqCHm2IL3R3OQ") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1132901778")] if os.environ.get("ADMINS") else []

DATABASE_NAME = os.environ.get("DATABASE_NAME", "Anurag789")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://renamev3-1:renamev3-1@cluster0.hyv9toa.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "1132901778")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001891138067")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False) # For Force Subscription
BROADCAST_AS_COPY = is_enabled((os.environ.get('BROADCAST_AS_COPY', "False")), False) # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 

