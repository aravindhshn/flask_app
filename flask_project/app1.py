import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
import flask
from dbs import Dbconnection

# ...
app = Flask(__name__)

# def get_db_connection():
#     conn = psycopg2.connect(host='localhost',
#                             database='dvdrental',
#                             user=os.environ['DB_USERNAME'],
#                             password=os.environ['DB_PASSWORD'])
#     app.logger.info('%s logged in successfully', conn)
#     return conn



@app.route('/')
def index():
    conn = Dbconnection.getInstance().getconn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM accounts_old;')
    accounts_old = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', accounts_old=accounts_old)


@app.route('/hello/<sender>/<receiver>/<amount>')
def hello_name(sender, receiver, amount):
   
    conn = Dbconnection.getInstance().getconn()
    cursor = conn.cursor()
    cursor.execute("CALL transfer_another(%s, %s, %s);", (sender, receiver, amount))
    conn.commit()
    return redirect(url_for('index'))


@app.route('/create_pro')
def create_pro():
    conn = Dbconnection.getInstance().getconn()
    cursor = conn.cursor()
    cursor.execute("""create or replace procedure transfer_another(
    sender int,
    receiver int, 
    amount dec
            )
            language plpgsql    
            as $$
            begin
                -- subtracting the amount from the sender's account 
                update accounts_old 
                set old_balance=balance,
                balance = balance - amount 
                where id = sender;

                -- adding the amount to the receiver's account
                update accounts_old 
                set old_balance=balance,
                balance = balance + amount 
                where id = receiver;                
    end;$$;""")
    conn.commit()
    conn.close()
    cursor.close()
    return 'Hello procedure Created'



if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)