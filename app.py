from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll_dice():
    dice_value = random.randint(1, 6)
    return render_template('index.html', dice_value=dice_value)

if __name__ == '__main__':
    app.run(debug=True)
