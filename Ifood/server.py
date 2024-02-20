from flask import Flask,render_template,request
import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    user="postgres",
    password="Ml304210?",
    port="5432",
    dbname="Ifood.bd"
)

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("teste_pagina2.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro_celular",methods=['POST','GET'])
def cadastro_celular():
    if request.method == "POST":
        telefone = request.form['phoneNumber']
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TBIF_CADASTRO(Telefone) VALUES(%s)",(telefone,))
            conn.commit()
            cursor.close()
        except Exception as e:
            print("Erro:",e)
            conn.rollback()
        finally:
            cursor.close()
    return render_template("cadastro_celular.html")

@app.route("/cadastro_email", methods=['POST','GET'])
def cadastro_email():
    if request.method == "POST":
        email = request.form['email']
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TBIF_CADASTRO(Email) VALUES(%s)",(email,))
            conn.commit()
            cursor.close()
        except Exception as e:
            print("Erro:",e)
            conn.rollback()
        finally:
            cursor.close()


    return render_template("cadastro_e-mail.html")

@app.route("/")
def codigo_verificacao():
    return render_template("código_de_acesso.html")




if __name__ == '__main__':
    app.run(debug=True)

