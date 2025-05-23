from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("20088801"))
    API_HASH = getenv("b761ce9bcc78b5ad5d1d677762e831d1")
    BOT_TOKEN = getenv("7572322597:AAEHoFL2QId_fLpukLDLeXZYRweuQBq6Ins")
    MONGO_URI = getenv("mongodb+srv://Japusahu:Japusahu@japusahu.qnu3j.mongodb.net/?retryWrites=true&w=majority&appName=JAPUSAHU")

# API_ID=20088801
# API_HASH=b761ce9bcc78b5ad5d1d677762e831d1
# BOT_TOKEN=7572322597:AAEHoFL2QId_fLpukLDLeXZYRweuQBq6Ins
# MONGO_URI=mongodb+srv://Japusahu:Japusahu@japusahu.qnu3j.mongodb.net/?retryWrites=true&w=majority&appName=JAPUSAHU
