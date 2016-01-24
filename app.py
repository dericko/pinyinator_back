# coding: utf-8
from dragonmapper import hanzi
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

s = u'这个字怎么念？'

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/pinyinify', methods=['POST'])
def pinyinify():
    if request.method == 'POST':
        print 'POST'
        print request
        data = request.get_json()
        pairs = []
        for ch in data['data']:
            pairs.append((ch, hanzi.to_pinyin(ch)))
        return jsonify(sentence=pairs)
    else:
        return "Error wrong method"

if __name__ == "__main__":
    app.run()
