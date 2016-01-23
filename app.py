# coding: utf-8
from dragonmapper import hanzi
from flask import Flask

app = Flask(__name__)

s = u'这个字怎么念？'


@app.route("/")
def hello():
    return hanzi.to_pinyin(s)


if __name__ == "__main__":
    app.run()
