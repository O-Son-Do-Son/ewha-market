from flask import Flask, render_template, request
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/items_insert")
def view_items():
    return render_template("insert.html")
    
@application.route("/items_result", methods=['GET'])
def result_items():
    category = request.args.get("category")
    location = request.args.get("location")
    price = request.args.get("price")
    status = request.args.get("status")
    title = request.args.get("title")
    content = request.args.get("content")
    
    print(category, location, price, status, title, content)
    #return render_template("result.html")

@application.route("/items_insert", methods=['POST'])
def insert_items():
    
    image_file = request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data=request.form
        
    return render_template("result.html", data=data, img_path="static/images/{}".format(image_file.filename))

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)