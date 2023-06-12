
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "key"



@app.route('/')
def home():
    return render_template('index.html')




@app.route('/result', methods = ['POST'])
def result():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']


    print(request.form)
    return render_template('result.html')

@app.route('/home')
def logout():
    session.clear()
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)