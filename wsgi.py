from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'syberry_test'

mysql = MySQL(app)

@app.route('/toys', methods=['GET'])
def get_param():
    #cur = mysql.connection.cursor()
    #cur.execute('''INSERT INTO toys (toy_id, name, status, status_updated) VALUES (4, 'car', 'ok', '2018-03-20')''')
    #toys = cur.execute('''SELECT * FROM toys''')
    #if toys > 0:
        #toys_details = cur.fetchall()
        #print(type(toys_details))
    return request.query_string
        #render_template('output.html', toys_details=toys_details)


if __name__ == '__main__':
    app.run()