from flask import Blueprint

app = Blueprint("general", __name__)


@app.route('/')
def main():  # put application's code here
    return 'yashar'