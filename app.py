from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/template")
def show_template():
    return render_template('index.html')

@app.route("/")
def hello():
    return "!!"

if __name__=='__main__':
    app.run(debug=True)