# initialisation de mon serveur flask python pour le bot
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return "Ceci sera mon nom dès que mon codeur en aura trouver un !!!!"


if __name__ == '__main__':
    app.run()

