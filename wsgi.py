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
    # cur = mysql.connection.cursor()
    # cur.execute('''INSERT INTO toys (toy_id, name, status, status_updated) VALUES (4, 'car', 'ok', '2018-03-20')''')
    # toys = cur.execute('''SELECT * FROM toys''')
    # if toys > 0:
        #toys_details = cur.fetchall()
        #print(type(toys_details))
    return temp
    # render_template('output.html', toys_details=toys_details)


@app.route('/games', methods=['GET'])
def get_param1():
    #games_date_from = date_converter(request.args.get('date_from'))
    #games_date_to = date_converter(request.args.get('date_to'))
    url = request.url
    parsed_url = urlparse(url)
    dic=parse_qs(parsed_url.query)
    if 'date_from' in dic:
        games_date_from = date_converter(dic.get('date_from')[0])
        print(games_date_from)
    cur = mysql.connection.cursor()
    '''
     games = cur.execute(SELECT * FROM games WHERE date >= %s, [games_date_from])
    if games > 0:
        games_details = cur.fetchall()
        #print(type(toys_details))
    '''
    print(dic)
    return request.query_string
        #render_template('output_games.html', games_details=games_details)


def date_converter(date:str):
    date_time = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    return date_time


if __name__ == '__main__':
    app.run(debug=True)