import random
from flask import Flask, render_template

def get_hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return random.choice(greeting_list)

app = Flask(__name__, static_folder='../static/dist', template_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return get_hello()

if __name__ == '__main__':
    app.run()