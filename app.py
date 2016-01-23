# coding: utf-8
from dragonmapper import hanzi
from flask import Flask, request, jsonify

app = Flask(__name__)

s = u'这个字怎么念？'

pairs = []
for ch in s:
    pairs.append((ch, hanzi.to_pinyin(ch)))


@app.route("/")
def hello():
    return hanzi.to_pinyin(s)


@app.route('/test', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        sentence = request.get_json()
        print sentence
        return jsonify(s=hanzi.to_pinyin(s))
    else:
        return "Error wrong method"


if __name__ == "__main__":
    app.run()
