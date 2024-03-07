from app import app
from flask import Flask,render_template,request, jsonify, redirect, url_for, session
import psycopg2 as pg
import numpy as np
from twilio.rest import Client
import random, secrets

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

conn = pg.connect(database = "ifood", host = "localhost", user = "postgres", password = "admin")

app.secret_key = secrets.token_bytes(16)

@app.route("/", endpoint='home')
def pagina_inicial():

    return render_template("teste_pagina2.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro_celular",methods=['POST','GET'])
def cadastro_celular():

    if 'telefone' in session:
        session.pop('telefone', None)

    if request.method == 'POST':
        print(request.form['phoneNumber'])
        session['telefone'] = request.form['phoneNumber']

        codigo1 = random.randrange(100000, 999999, 6)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Seu código de verificação é {codigo1}. Para sua segurança, não o compartilhe.',
            to=f'whatsapp:+55{session["telefone"]}'
            )

        print(message.sid)
        print(session['telefone'])

        session['codAcess'] = codigo1


        return render_template("/código_de_acesso.html")


    return render_template("cadastro_celular.html")

@app.route("/cadastro_email", methods=['POST', 'GET'])
def cadastro_email():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            email = data.get('email')
        else:
            email = request.form.get('email')


    return render_template("cadastro_e-mail.html")



@app.route("/código_de_acesso", methods=['POST','GET'])
def codigo_verificacao():

    if request.method == 'POST':
        codigo_str = request.form.get('accessCode')
        
        if int(codigo_str) == session['codAcess']:
            return render_template('teste_pagina2.html')
        
        else:
            return render_template("código_de_acesso.html", codErrado = True)
        
    return render_template("código_de_acesso.html")



@app.route("/bebidas")
def pagina_bebidas():
    return render_template("Página_bebidas.html")

