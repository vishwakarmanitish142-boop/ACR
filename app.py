from flask import Flask, render_template, request

import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/academics")
def academics():
    return render_template("academics.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/news")
def news():

    conn = sqlite3.connect("database/school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news ORDER BY id DESC")

    news_data = cursor.fetchall()

    conn.close()

    return render_template(
        "news.html",
        news=news_data
    )

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/admin")
def admin():

    return render_template("admin_login.html")

@app.route("/admin/add-news", methods=["GET","POST"])
def add_news():
    return "Add News Page"

@app.route("/admission", methods=["POST"])

@app.route("/complaint", methods=["GET","POST"])
def complaint():

    if request.method == "POST":

        name = request.form["name"]
        mobile = request.form["mobile"]
        category = request.form["category"]
        subject = request.form["subject"]
        complaint_text = request.form["complaint"]

        conn = sqlite3.connect("database/school.db")

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO complaints
        (name,mobile,category,subject,complaint)

        VALUES(?,?,?,?,?)

        """,

        (name,mobile,category,subject,complaint_text))

        conn.commit()
        conn.close()

        return "शिकायत सफलतापूर्वक दर्ज हो गई"

    return render_template("complaint.html")

if __name__ == "__main__":
    app.run(debug=True)
   