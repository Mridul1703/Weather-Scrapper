from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return render_template("index.html")

@app.route('/weather', methods = ['POST'])
def weather():
    from time import time
    from bs4 import BeautifulSoup
    import requests

    city = request.form['city']
    url = 'https://www.google.com/search?q=weather' + city

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    temp = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

    time = soup.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
    data = time.split('\n')

    return render_template("weather.html",ct=city, t=temp, d0=data[0], d1=data[1])

if __name__ == "__main__":
    app.run(debug=True)