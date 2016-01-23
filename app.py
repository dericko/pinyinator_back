# coding: utf-8
from dragonmapper import hanzi
from flask import Flask, request, jsonify

app = Flask(__name__)

s = u'这个字怎么念？'

pairs = []
for ch in s:
  pairs.append((ch, hanzi.to_pinyin(ch)))


@app.route("/")
def home():
  return hanzi.to_pinyin(s)


@app.route('/pinyinify', methods=['POST'])
def pinyinify():
  if request.method == 'POST':
    data = request.get_json()
    return jsonify(s=hanzi.to_pinyin(data['data']))
  else:
    return "Error wrong method"


if __name__ == "__main__":
  app.run()
