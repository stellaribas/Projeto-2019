from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('_Paginas/Cadastro.html')


if(__name__=='__main__'):
    app.run(debug=True)
