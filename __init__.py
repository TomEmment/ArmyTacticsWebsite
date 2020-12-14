from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///FeedbackClass.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Smudge"

db = SQLAlchemy(app)

class FeedbackClass(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    Name = db.Column("Name", db.String(100))
    Score = db.Column("Score", db.Integer)
    Cost = db.Column("Cost", db.Float)
    Review = db.Column("Review", db.String(3000))

    def __repr__(self):
        return '<FeedbackClass %r>' % self.Name

db.create_all()

@app.route("/")

def home():
    return render_template("Home.html")

@app.route("/Wiki")

def Wiki():
    return render_template("Wiki.html")

@app.route("/About")

def About():
    return render_template("about.html")

@app.route("/Feedback", methods=["POST","GET"])

def Feedback():
    if request.method == "POST":
        user = request.form["Name"]
        score = request.form["Fun"]
        cost = request.form["Cost"]
        review = request.form["Feedback"]
        Temp = FeedbackClass(Name = user, Score = score,Cost = cost,Review = review)
        db.session.add(Temp)
        db.session.commit()
        flash("Feedback submitted! Thank you :)", "info")
        return render_template("Feedback.html")
    else:
        return render_template("Feedback.html")

@app.route("/Review")
def Review():
    return render_template("Review.html", values = FeedbackClass.query.all())

if __name__ == "__main__":
    app.run(debug=True)
