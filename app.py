from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)
# 存储留言的列表
messages = []

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", messages=messages)

@app.route("/add_message", methods=["POST"])
def add_message():
    message = request.form.get("message")
    messages.append(message)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
