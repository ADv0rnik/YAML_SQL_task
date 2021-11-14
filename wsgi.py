from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from urllib.parse import urlparse, parse_qs
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'syberry_test'

mysql = MySQL(app)


@app.route('/toys', methods=['GET'])
def get_param():
    temp = request.args.get('name')
    #cur = mysql.connection.cursor()
    #cur.execute('''INSERT INTO toys (toy_id, name, status, status_updated) VALUES (4, 'car', 'ok', '2018-03-20')''')
    #toys = cur.execute('''SELECT * FROM toys''')
    #if toys > 0:
        #toys_details = cur.fetchall()
        #print(type(toys_details))
    return temp
    #render_template('output.html', toys_details=toys_details)

@app.route('/games', methods=['GET'])
def get_param1():
    games_date_from = request.args.get('date_from')
    games_date_to = request.args.get('date_to')

    '''
    cur = mysql.connection.cursor()
    games = cur.execute(SELECT * FROM toys)
    if games > 0:
        games_details = cur.fetchall()
    '''
    print(type(games_date_from))
    d = date_converter(games_date_from)
    print(d)
    return games_date_from
        #render_template('output_games.html', games_details=games_details)

def date_converter(date:str):
    date_time = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    return date_time

if __name__ == '__main__':
    app.run()