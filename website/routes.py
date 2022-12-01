from flask import Flask, request, Blueprint, render_template, url_for
from .database import inserir_dados, buscarInfo

routes = Blueprint('routes',__name__)


@routes.route("/")
def i():
    return render_template("home.html")

@routes.route("/home")
def home():
    return render_template("home.html")

@routes.route("/contato",methods = ["POST","GET"])
def contato():
    if request.method == "POST":
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        descricao = request.form.get("desc")
        inserir_dados(email, assunto, descricao)
        return render_template("contato.html")
    return render_template("contato.html")

@routes.route("/quemSomos")
def who():                  
    return render_template("quemSomos.html")

@routes.route("/info")
def info():
    db_info = buscarInfo()
    email = db_info[0]
    assunto = db_info[1]
    descricao = db_info[2]
    num = len(email)
    return render_template("info.html", email=email, assunto=assunto, descricao=descricao, num=num)


