from flask import Flask, render_template, request
from investimento import Investimento

pagina1 = 'Investimento'


app=Flask(__name__)
@app.route('/')
def categoria():
    return render_template('index.html', titulo = pagina1)


app.run()  

      