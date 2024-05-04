from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cars24@123'
app.config['MYSQL_DB'] = 'flask_app'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Name = details['fname']
        Id = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO file(name,id) VALUES (%s, %s)", (Name, Id))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)