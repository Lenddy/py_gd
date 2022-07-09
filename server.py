from flask import Flask, render_template


app = Flask(__name__)

# always put your DECORATOR !!!!!!!!!!!!!!!!!


# shows 3 box 
@app.route('/play')
def display_boxes():
    return render_template("index.html",num=3,color = "teal")

# you chose the amount of boxes
@app.route("/play/<int:num>")
def add_boxes(num):
    return render_template("index.html",num = num,color = "teal")

# you chose the amount of boxes and the color
@app.route("/play/<int:num>/<string:color>")
def select_color(num,color):

    return render_template("index.html",num=num,color=color)





if __name__ == "__main__":
    app.run(debug = True)