from flask import Flask, render_template, request, redirect
import helpers
import os

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')
    

@app.route('/features', methods = ["GET", "POST"])
def features():
    if request.method == "GET":
        return render_template('features.html')
    
    else:
        coords = request.form["coords"]
        coordinates = coords.split(',')
        try:
            os.remove('static/AfterImage.png')
            os.remove('static/BeforeImage.png')
            os.remove('static/outputAfter.png')
            os.remove('static/outputBefore.png')
            os.remove('static/result.png')
        except:
            print('hello')
        helpers.getBeforeAndAfterImages(coordinates)
        return redirect('/contact')
        
@app.route('/contact') #by default is GET request
def result():
    return render_template('contact.html')

@app.route('/leaderboard') #by default is GET request
def leaderboard():
    return render_template('pricing.html')


if __name__ == '__main__':
    #./ngrok http 3000
    app.run(port=3000) #debug = True in order to not run every time
