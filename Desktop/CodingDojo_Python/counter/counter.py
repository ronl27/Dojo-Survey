from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "thisismysecretkey"

@app.route ('/')

def index ():
  if 'count' not in session:
      session['count'] = 1
  else:
      session ['count'] += 1
  return render_template('index.html')

@app.route('/plus', methods = ['GET', 'POST'])
def plus():


    if request.form['button'] == 'plus 2':
        session['count'] += 1
        return redirect('/')

    elif request.form['button'] == 'reset':
        session['count'] = 0
        return redirect('/')

    else:
        return redirect('/')

app.run(debug = True)
