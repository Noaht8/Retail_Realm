from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/shopify'
db = SQLAlchemy(app)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(500))
  price = db.Column(db.Integer)

@app.route("/")
def index():
  products = Product.query.all()
  return render_template("index.html", products=products)

@app.route("/login")
def login():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]

    # Check if the user exists in the database.
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
      # Login the user and redirect to the home page.
      login_user(user)
      return redirect(url_for("index"))

    else:
      # Invalid credentials.
      flash("Invalid email or password.")

  return render_template("login.html")

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(debug=True)
