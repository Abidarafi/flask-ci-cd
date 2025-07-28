from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan post dalam list sementara (tanpa database dulu)
posts = []

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        posts[index]["title"] = request.form["title"]
        posts[index]["content"] = request.form["content"]
        return redirect(url_for("index"))
    return render_template("edit.html", post=posts[index], index=index)

@app.route("/delete/<int:index>")
def delete(index):
    posts.pop(index)
    return redirect(url_for("index"))
