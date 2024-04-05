from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

base = []


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        name = request.args.get("name")
        email = request.args.get("email")
        message = request.args.get("message")
        if name and email and message:
            base.extend([name, email, message])
            print(base)
        else:
            return render_template("contact.html")
    return redirect(url_for('contact_submit'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact-submit")
def contact_submit():
    name = base[0]
    message = base[2]
    return f'Спасибо, {name}, ваше сообщение "{message}" отправлено.'


app.run(
    debug=True,
    host="0.0.0.0",
)
