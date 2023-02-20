from flask import Flask, render_template, request
import random


app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        numero = int(request.form['num'])
        lista = "abcdefghijklmnopqrstuvwxyz123456789!@##$%&*()_+"
        senha = "".join(random.sample(lista,numero))
    else:
        senha = '' 

    return render_template('login.html', name=senha)

app.run(host='localhost',port=5000, debug=True)
app.run()
    

