from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<font size='30'><marquee scrollamount='12' direction='right'>Hello World!</marquee></font>"


if __name__ == "__main__":
    app.run()
