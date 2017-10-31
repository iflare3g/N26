from flask import Flask
from app.transactions import Transaction

app = Flask(__name__)
trans = Transaction()

from app import views 

