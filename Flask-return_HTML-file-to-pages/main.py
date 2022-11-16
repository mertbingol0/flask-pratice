from flask import Flask, render_template

app = Flask(__name__)

"""
Sayfalara hangi yonlendirmeyi tanimladiysaniz,
sayfalarin htmlinde linklediginiz diger sayfalarin pathi de,
dosya adina ve konumuna gore degil, yonlendirmeye gore olmali.
"""

#index Page
@app.route('/') 
def index():
	return render_template("/index.html")

#contact Page
@app.route('/contact')
def contact():
	return render_template("/contact.html")

#about Page
@app.route('/about')
def about():
	return render_template("/about.html")

if __name__ == '__main__':
	app.run(debug=True)