import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Kishaaheer:Kishaaheer@kishaaheer.dxe4o.mongodb.net/?retryWrites=true&w=majority&appName=Kishaaheer")
    DB_NAME = os.environ.get("DB_NAME", "Kishaaheer")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '7159500227').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
