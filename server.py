from flask import Flask,redirect,request,render_template,session
app = Flask(__name__)
app.secret_key = "Dominicks secret key!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['firstname']=request.form['firstname']
    session['lastname']=request.form['lastname']
    session['dojolocation']=request.form['dojolocation']
    session['favoritelanguage']=request.form['favoritelanguage']
    session['comment']=request.form['comment']
    # if 'check' not in session:
    #     session['check']= f'{session["firstname"]} is not excited....'
    # if 'check' in session == 'on':
    #     session['check']= f'Lets get this party STARTED!!'
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)





