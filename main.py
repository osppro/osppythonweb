from flask import Flask,render_template

app = Flask(__name__)


# index / home page...
@app.route('/') 
def home():
	return render_template("index.html")

# about us page..
@app.route('/about')
def about():
	return render_template("about.html")

# contact us page..
@app.route('/contact')
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
	app.run(debug=True)
