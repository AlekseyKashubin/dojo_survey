from flask_app import app
from flask import  render_template, request, redirect, session

from flask_app.models.dojo_survey_model import Survey




@app.route('/')
def home():
    return render_template('index.html')




@app.route('/result', methods = ['POST'])
def result():
    print(request.form)
    if not Survey.validate_survey(request.form):
        return redirect('/')


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