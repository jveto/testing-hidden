from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key="notouchy"

@app.route('/')
def index():
    session['visits'] += 1
    print("************************************ we got it")
    print(session['visits'])
    if request.form['action'] == "2":
        print("gotit")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)