from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
	return "Anasayfaya Hos Geldiniz!"

@app.route("/contact")
def contact():
	return "mail: test@test.com"

@app.route("/about")
def about():
	return "bla blabla flask ogreniyorum."

if __name__ == "__main__":
	app.run(debug=True)