#Import the CSV tool
import csv
from flask import abort
#must have capital F flask- from the flask library, import the flask application
from flask import Flask
#This goes out to the flask library and gets the render template
from flask import render_template

#create the app- there are two underscores on either side of name
app = Flask(__name__)

# to create the csv function
def get_csv():
	#where the csv file is. We are going to make it a named variable so we can call it later. It is a shortcut.
	csv_path = "static/la-riots-deaths.csv"
	#Now we need python to open the file  and save it to a variable. The rb means read binary, telling python how to open it
	csv_file = open(csv_path, 'rb')
	#now we need to parse it as a CSV
	csv_obj = csv.DictReader(csv_file)
	#so sublime doesn't crash
	csv_list =list(csv_obj)
	return csv_list


#connecting our browser to the python function
@app.route('/')

def index():
	template = "index.html"
	#passing the csv into the template
	object_list = get_csv()
#this is passing in what is in the template file into the render function- it will render it and then pass it back to us in the browser
	return render_template(template, object_list=object_list)

#connecting our browser to the detail page which will use the id as the variable that will hold which record to put on the website
@app.route('/<row_id>/')
def detail(row_id):
	template = "detail.html"
	object_list = get_csv()
	for row in object_list:
#so now we are creating a for loop and have a logical test, == checks to see if two things are equal
		if row['id'] == row_id:
			return render_template(template, object= row)
		abort(404)




#If this script is run from the command line 
if __name__ == "__main__":
	#then start this app up
	app.run(debug=True, use_reloader=True)


