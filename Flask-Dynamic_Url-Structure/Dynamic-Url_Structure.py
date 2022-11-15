from flask import Flask, render_template

app = Flask(__name__)

@app.route('/kitap/<string:id>')
def kitap(id):
	return "Kitap: " + id


if __name__ == "__main__":
	app.run(debug=True)