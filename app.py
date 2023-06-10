from flask import Flask, render_template, request, session
import uuid, os, schedule

app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form/<string:design>", methods = ["GET","POST"])
def form(design):
    session["s_design"] = design
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    design_upload = session.get("s_design")
    if design_upload == "design1":
        design_name = "design1.html"
    elif design_upload == "design2":
        design_name = "design2.html"

    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        designation = request.form.get("designation")
        school = request.form.get("school")
        college = request.form.get("college")
        address = request.form.get("address")
        phone = request.form.get("phone")
        email = request.form.get("email")
        linkedin = request.form.get("linkedin")
        facebook = request.form.get("facebook")
        twitter = request.form.get("twitter")
        about = request.form.get("about")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")

        key = uuid.uuid1()
        img = request.files["dp"]
        img.save(f"static/SavedPics/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/SavedPics/{img.filename}", f"static/SavedPics/{img_new_name}")

    return render_template(design_name,
                           fname = firstname,
                           lname = lastname,
                           des = designation,
                           sch = school,
                           col = college,
                           add = address,
                           ph = phone,
                           em = email,
                           ln = linkedin,
                           fb = facebook,
                           tw = twitter,
                           abt = about,
                           sk1 = skill1,
                           sk2 = skill2,
                           sk3 = skill3,
                           sk4 = skill4,
                           img = img_new_name)

def delete():
    files = os.listdir("static/SavedPics")
    for f in files:
        os.remove(f"static/SavedPics/{f}")

if __name__ == "__main__":
    schedule.every().hour.do(delete)
    app.run(debug = False, host = '0.0.0.0')