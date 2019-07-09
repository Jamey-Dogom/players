from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('players')	        # call the function, passing in the name of our db
    player = mysql.query_db('SELECT * FROM player_table;')  # call the query_db function, pass in the query as a string
    return render_template("index.html", player = player)

@app.route("/create_user", methods = ["POST"])
def create_user():
    mysql = connectToMySQL('players')
    query = "INSERT INTO player_table (first_name, last_name, team, sport) VALUES (%(fname)s, %(lname)s, %(tname)s, %(sname)s);"

    data = {
        "fname": request.form['fn'],
        "lname": request.form['ln'],
        "tname": request.form['tn'],
        "sname": request.form['sn']
    }

    new_player = mysql.query_db(query, data)

    return redirect("/")

@app.route("/delete_user", methods= ["POST"])
def delete_user():
    mysql = connectToMySQL('players')
    query = "DELETE FROM player_table WHERE id = %(delid)s;" 

    data = {      
        "delid": request.form['del']
    }

    del_player = mysql.query_db(query, data)
    return redirect("/")




@app.route("/update_user", methods=["POST"])
def update_user():
    mysql = connectToMySQL('players')
    query = "UPDATE player_table SET first_name = %(uf)s,  last_name =%(ul)s ,  team = %(ut)s, sport = %(us)s WHERE id = %(uz)s;"

    data = {
        "uf": request.form['first'],
        "ul": request.form['last'],
        "ut": request.form['team'],  
        "us": request.form['sport'],
        "uz": request.form['id']
    }

    print(data)
    update_player = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)