from flask import Flask, jsonify, request
import os
import mysql.connector
from dotenv import load_dotenv
from goodreadsScrape import get_books
load_dotenv()
 
mydb = mysql.connector.connect(
	host=os.getenv('MYSQLHOST'),
	port=os.getenv('MYSQLPORT'),
	database=os.getenv('MYSQLDATABASE'),
 	user=os.getenv('MYSQLUSER'),
 	password=os.getenv('MYSQLPASSWORD')
)

app = Flask(__name__)

# Schema: id, title, author, link, rating


@app.route('/')
def index():
	if 'year' in request.args:
		year = request.args['year']

		table = "books%s" % (year)

		cursor = mydb.cursor()     # get the cursor

		selectQuery = "SELECT * FROM %s" % (table)
		cursor.execute(selectQuery)

		result = cursor.fetchall()

		return jsonify(result)
	
	else: 
		return 'This is my personal books API. Written by Alex Reyes for use in www.alexreyes.xyz. Please request a specific year. For example: /?year=2021'

# endpoint to update the book list
@app.route('/', methods=["POST"])
def update_list(): 
	if 'year' in request.args:
		year = request.args['year']
		table = "books%s" % (year)

		bookList = get_books(year)

		cursor = mydb.cursor() 
			
		insertPartOne = "INSERT INTO books2019 (title, link) VALUES ('test', 'yeet')"
		cursor.execute(insertPartOne);

		result = cursor.fetchall()

		return(jsonify(result))

		bookInsert = []

	else: 
		return 'SPECIFY YEAR'



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))