#must have capital F flask- from the flask library, import the flask application
from flask import Flask
#This goes out to the flask library and gets the render template
from flask import render_template

#create the app- there are two underscores on either side of name
app = Flask(__name__)

#connecting our browser to the python function
@app.route('/')

def index():
	template = "index.html"
#this is passing in what is in the template file into the render function- it will render it and then pass it back to us in the browser
	return render_template(template)

#If this script is run from the command line 
if __name__ == "__main__":
	#then start this app up
	app.run(debug=True, use_reloader=True)


