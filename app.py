from flask import Flask,request,redirect,url_for, render_template
from sql_queries import TourDB
from settings import *
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
db = TourDB()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/places")
def places():
    places_list = db.get_all_places()
    return render_template("places.html",items = places_list)
@app.route("/cities")
def cities():
    return render_template("cities.html")
@app.route("/comment")
def comment():
    comments_list = db.get_all_comments()
    return render_template("comment.html", items = comments_list)
@app.route("/comment_l", methods = ["GET","POST"])
def comment_l():
    if request.method == 'POST':
        db.add_comment(request.form["name"],request.form["comment"])
        return redirect(url_for('comment'))
    return render_template("comment_l.html")

@app.route("/places_l",methods = ["GET","POST"])
def places_l():
    if request.method == 'POST':
        image = request.files['image']
        image.save(PATH_IMG+image.filename)
        db.add_place(request.form["name"],request.form["price"],request.form["desc"],request.form["address"],image.filename)
        return redirect(url_for('places'))
    return render_template("places_l.html")

if __name__ == "__main__":
    app.run(debug=True)
