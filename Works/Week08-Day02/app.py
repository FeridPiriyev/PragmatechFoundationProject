from flask import Flask,request

app=Flask(__name__)


@app.route("/")
def index():
    return "salam dunya"

@app.route("/about/<ad>",methods=["GET","POST"])
def about(ad):

    return str(ad)


if __name__=="__main__":
    app.run(debug=True)
