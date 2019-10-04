from flask import Flask, render_template

nome = 'Aula 4'

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html')
app.run()

