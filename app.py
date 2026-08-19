from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def welcome():
    return render_template('index.html')

@app.route('/roster.html')
def roster():
    return render_template('roster.html')

if __name__ == '__main__':
    app.run(debug=True)


