from flask import render_template, request
from app import app
import random


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jouer', methods=['POST'])
def jouer():
    options = ["pierre", "feuille", "ciseaux"]

    joueur = request.form.get('choix').lower()
    ordinateur = random.choice(options)

    if joueur == ordinateur:
        resultat = "Égalité !"
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "feuille" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "feuille"):
        resultat = "Vous avez gagné !"
    else:
        resultat = "Vous avez perdu !"

    return render_template('index.html', joueur=joueur, ordinateur=ordinateur, resultat=resultat)