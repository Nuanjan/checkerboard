from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<x>')
def sizeX(x):
    return render_template("sizeX.html", column=int(x))


@app.route('/<x>/<y>')
def sizeXY(x, y):
    return render_template("sizeXY.html", column=int(x), row=int(y))


@app.route('/<x>/<y>/<color1>')
def sizeAndColor1(x, y, color1):
    print(color1)
    return render_template("sizeAndColor1.html", column=int(x), row=int(y), color1=color1)


@app.route('/<x>/<y>/<color1>/<color2>')
def sizeAndColors(x, y, color1, color2):
    return render_template("sizeAndColors.html", column=int(x), row=int(y), color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
