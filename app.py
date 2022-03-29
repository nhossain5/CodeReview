from os import getenv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("hello world")
    return "Hello Nahid!!!!!!!!!"

app.run(
    host=getenv("IP", "0.0.0.0"),
    port=int(getenv("PORT", "8080"))
)