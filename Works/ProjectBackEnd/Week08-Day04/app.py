from flask import Flask,render_template

app=Flask(__name__)

books=[
    {
        "bookName":"Deli Kur",
        "bookAuthor":"Ismayil Sixli"
    },
    {
        "bookName":"Sibumu",
        "bookAuthor":"İrevanian"
    },
        {
        "bookName":"QaraVolqa",
        "bookAuthor":"Çingiz Abdullayev"
    },
]


@app.route('/')
def index():
    
    return render_template('show_books.html',books=books)


@app.route("/add")
def add_book():
    return render_template("add_book.html")


if __name__=="__main__":
    app.run(debug=True)