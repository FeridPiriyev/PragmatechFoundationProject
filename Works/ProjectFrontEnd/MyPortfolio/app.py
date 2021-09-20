from flask import Flask, render_template


app=Flask(__name__)


@app.route('/home')
def index():
    return render_template('MyPortfolio.html', )

@app.route('/about')
def about():
    return render_template('Support.html',)

@app.route('/join')
def join():
    return render_template('JoinNow.html',)

@app.route('/sign')
def sign():
    return render_template('Signin.html',)

if __name__ == '__main__':
    app.run(debug=True)
