# coding: utf-8
from dragonmapper import hanzi
from bs4 import BeautifulSoup
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
        # print request.data

        data = request.form
        titlePairs = []
        paragraphsPairs = []
        html_doc = data['data']
        html_doc = u''+html_doc
        soup = BeautifulSoup(html_doc, 'html.parser')
        print soup.h1.text
        # print soup.get_text()
        title = u'' + soup.h1.text
        paragraphs = soup.find_all('p')
        # print 'Reaching'
        for ch in title:
            titlePairs.append((ch, hanzi.to_pinyin(ch)))
        for p in paragraphs:
            paraPairs = []
            print p
            for ch in p.text:
                paraPairs.append((ch, hanzi.to_pinyin(ch)))
            paragraphsPairs.append(paraPairs)
        return jsonify(title=titlePairs, paragraphs=paragraphsPairs)
    else:
        return "Error wrong method"

if __name__ == "__main__":
    app.run(debug=True)
