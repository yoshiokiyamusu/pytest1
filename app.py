
from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd

from flask_mysqldb import MySQL


# initializations
app = Flask(__name__)

# Pandas example


# Mysql Connection
app.config['MYSQL_HOST'] = 'ysp9sse09kl0tzxj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mlq7ddpaya3gnozv'
app.config['MYSQL_PASSWORD'] = 'n4slsu3xuaiqtbgd'
app.config['MYSQL_DB'] = 'szps1l4ru1pkph3s'
mysql = MySQL(app)

# settings //Session in the app memory
app.secret_key = "mysecretkey"


s = pd.Series([1, 2, 3, 4, 5, 6])
t = pd.Series([2, 4, 6, 8, 10, 12])
df = pd.DataFrame({'col1': s, 'col2': t})


# routes


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('select * from tb_imagen')
    data = cur.fetchall()

    cur.close()
    return render_template('index.html', contacts=df)


print(df)

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
