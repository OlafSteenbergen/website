from flask import Response, Flask, flash, render_template, redirect, url_for, request, session, g
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

@app.route("/")
def index():
    connection = sqlite3.connect("website.db")
    cursor = connection.cursor()
    allarticles = cursor.execute('SELECT * FROM articles').fetchall()
    return render_template('home.html', allarticles=allarticles)


if __name__ == "__main__":
    app.run(debug=False)