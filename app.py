from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



@app.route("/")
def main():
    return render_template('map.html')

def zoomChanged():
    #_zoomlevel = map.getZoom()


if __name__ == "__main__":
    app.run()
