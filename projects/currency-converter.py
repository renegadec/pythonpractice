from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = "90273ff32d73f1feacad"

printer = PrettyPrinter()

def get_currencies()
endpoint = f"/api/v7/currencies?apiKey={API_KEY}"