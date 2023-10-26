from flask import Flask, render_template, request, redirect, url_for
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/items_insert")
def view_items():
    return render_template("insert.html")
    

@application.route("/items_insert", methods=['POST'])
def insert_items():
    
    image_file = request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    img_path = "static/images/{}".format(image_file.filename)
    print(data["category"], data["location"], data["price"], data["status"], data["title"], data["content"])
    return render_template("result.html", data=data, img_path=img_path)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)