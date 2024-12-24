from flask import Flask, render_template, request
from redis import Redis


app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    redis.incr("hits")
    return "Hello World! I have been seen %s times!!!!" % redis.get("hits")


@app.route("/t1")
def t1():
    return render_template("t1.html")


@app.route("/t2", methods=["GET"])
def t2():
    name = request.args.get("name")
    return render_template("t2.html", var1=name)


@app.route("/t3", methods=["GET"])
def t3():
    return render_template("t3.html")


@app.route("/get_post", methods=["GET"])
def get_from_post():
    return render_template("t4.html", msg="enter your name")


@app.route("/get_post", methods=["POST"])
def post_from_post():
    name = request.form["myname"]
    return render_template("t4.html", msg=f"hello {name}")


@app.route("/t5")
def t5():
    return render_template("t5.html", msg="This is message", warning=True)


@app.route("/t6")
def t6():
    data = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return render_template("t6.html", unrolled_data=data, data=data)


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return render_template("chat.html", conversation="Hello")
    elif request.method == "POST":
        msg = request.form["msg"]
        redis.lpush("log", msg)
        message_log = redis.lrange("log", 0, -1)
        return render_template("chat.html", conversation=message_log)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
