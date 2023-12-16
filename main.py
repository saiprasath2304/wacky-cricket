from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('wacky.html')

@app.route('/add', methods=['POST','GET'])
def click():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    player_name = request.form['player_name']

    conn = sqlite3.connect('wacky.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERS (NAME VARCHAR(255));")
    cursor.execute(f"INSERT INTO PLAYERS (NAME) VALUES ('{player_name}')")

    conn.commit()
    conn.close()

    return render_template('submitted.html', player_name=player_name)

@app.route('/get_players')
def get_players():
    conn = sqlite3.connect('wacky.db')
    cursor = conn.cursor()

    cursor.execute("SELECT NAME FROM PLAYERS;")
    players = cursor.fetchall()

    conn.close()

    # Convert the result to a list of dictionaries
    players_list = [{'name': player[0]} for player in players]
    return jsonify(players_list)


if __name__ == '__main__':
    app.run(debug=True)
