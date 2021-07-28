import datetime as dt
import time
from cs50 import SQL
import feedparser
import time
import os
from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message

app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get('email')
EMAIL_PASSWORD = os.environ.get('email_password')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.secret_key = b'P\x9b\xf2\xc7\x14\xc8mb1!\x96\xd9\xeb\x06\xbf>' #PUT IT IN THE VARIABLE

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///news.db")

FEED_URL = "http://america.aljazeera.com/content/ajam/articles.rss"

@app.route("/")
def index():
    article = news_articles()
    return render_template('index.html', article=article)

def news_articles(): #used by the update()
    feed = feedparser.parse(FEED_URL)
    article = feed.entries
    return article

@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    """Register user"""
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
         username = request.form.get("username");
         password = request.form.get("password");
         confirmation = request.form.get("confirmation");
         email = request.form.get("email");

         rows = db.execute("SELECT * FROM users WHERE username = ? OR email = ?", username, email)

         # Ensure username exists and password is correct
         if len(rows) == 1:
            return render_template("subscribe.html", message="Username or Email already taken")

         p = generate_password_hash(password);

         db.execute("INSERT INTO users (username, hash, email) VALUES(?,?, ?)", username, p, email);

         subject = "Welcome to Ayush\'s news Website"
         body = "Hello Flask message sent from Flask-Mail."

         send_mail(email, subject, body)

         # Redirect user to home page
         return redirect("login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
         return render_template("subscribe.html")

def send_mail(email, subject, body):

    msg = Message(subject, sender = EMAIL_ADDRESS, recipients = [email])
    msg.body = body
    mail.send(msg)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

         # Query database for username
         rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

         # Ensure username exists and password is correct
         if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html", message="Invalid username and/or password")

         # Remember which user has logged in
         session["user_id"] = rows[0]["id"]

         # Redirect user to home page
         return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
         return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

if __name__ == '__main__':
   app.run(debug = True)
