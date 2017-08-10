from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(since,'%M %d %Y') FROM friends" # define your query, make sure you use the DATE_FORMAT stuff in your key 
    friends = mysql.query_db(query) # run query with query_db()
    return render_template('index.html', full_friends=friends)


@app.route('/add_friends', methods=['POST'])
def add_afriend():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, since, created_at, updated_at) VALUES (:name, :age, NOW(), NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)