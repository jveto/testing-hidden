from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key="notouchy"

@app.route('/', methods = ['GET'])
def index():
    if not session['visits']:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/twoVisits', methods = ['POST'])
def twoVisits():
    if request.form['visits2']:
        session['visits'] += int(request.form['visits2'])
    return redirect('/')

@app.route('/zeroVisits', methods=['POST'])
def zeroVisits():
    if request.form['visits0']:
        session['visits'] = int(request.form['visits0'])
    return redirect('/')


if __name__ == "__main__":  
    app.run(debug = True)