from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("static/index.html")

@app.route('/data.html')
def data():  # put application's code here
    return render_template("static/data.html")

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template("static/wordcloud.html")

@app.route('/toplist.html')
def toplist():  # put application's code here
    return render_template("static/toplist.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
