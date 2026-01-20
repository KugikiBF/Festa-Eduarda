from flask import Flask

app= Flask(__name__)

@app.route("/")
def teste():
    return "<h1> Eu te amo mozão, to aprendendo a a </h1>"

if __name__== "__main__":
    app.run(debug=True)