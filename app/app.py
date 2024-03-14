from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #return "<h1>Hola mundo desde Flask que tal</h1>"

    data = {
        "Titulo": "Index",
        "bienvenida": "Saludos!!!"
    }

    return render_template("index.html",data=data)

if __name__ == "__main__":
    app.run(debug = True, port=5000)
