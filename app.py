from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # or index.html if that's your homepage

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/diet-plans")
def diet_plans():
    return render_template("diet-plans.html")

@app.route("/calorie-tracker")
def calorie_tracker():
    return render_template("calorie-tracker.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)