#Import the CSV tool
import csv
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

#If this script is run from the command line 
if __name__ == "__main__":
	#then start this app up
	app.run(debug=True, use_reloader=True)


