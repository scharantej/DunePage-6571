
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/artwork')
def artwork():
    return render_template('artwork.html')

@app.route('/theme')
def theme():
    return render_template('theme.html')

@app.route('/call-to-action')
def call_to_action():
    return render_template('call-to-action.html')

if __name__ == '__main__':
    app.run()
