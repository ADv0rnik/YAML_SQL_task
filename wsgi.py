from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import yaml_parse

app = Flask(__name__)

# connecting to DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'syberry_test'

mysql = MySQL(app)
cur1 = mysql.connection.cursor()
cur1.execute(yaml_parse.statements[0])

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

# getting parameters from "games" table
@app.route('/games', methods=['GET'])
def get_param_from_games():
    url = request.url
    parsed_url = urlparse(url)
    dates_limits = {'date_from', 'date_to'}
    dic = parse_qs(parsed_url.query)
    cur = mysql.connection.cursor()
    if dates_limits.issubset(dic):
        games_date_from = date_converter(dic.get('date_from')[0])
        games_date_to = date_converter(dic.get('date_to')[0])
        games = cur.execute('''SELECT * FROM games WHERE date >= % s AND date <= %s''',
                            [games_date_from, games_date_to])
    elif 'date_from' in dic:
        games_date_from = date_converter(dic.get('date_from')[0])
        games = cur.execute('''SELECT * FROM games WHERE date >= % s''',
                            [games_date_from])
    elif 'date_to' in dic:
        games_date_to = date_converter(dic.get('date_to')[0])
        games = cur.execute('''SELECT * FROM games WHERE date <= % s''',
                            [games_date_to])
    else:
        print('Parameter not found')
    if games > 0:
        games_info = cur.fetchall()
    return render_template('output_games.html', games_details=games_info)


# simple function to convert dates
def date_converter(date : str):
    date_time = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    return date_time


if __name__ == '__main__':
    app.run(debug=True)