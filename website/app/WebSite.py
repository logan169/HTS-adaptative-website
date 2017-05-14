#-*- encoding:utf-8 -*-
from flask import Flask, render_template,url_for,redirect,request,flash
from flask_mail import Mail,Message


listeChapitres=['Introduction','chapitre1','chapitre2','chapitre3','chapitre4','chapitre5','chapitre6','chapitre7','chapitre8','chapitre9']

def getChapitreUrl(direction,element):
    x=listeChapitres.index(element)
    if direction == 'next':
        if x < len(listeChapitres)-1:
            output= listeChapitres[x+1]
        else:
            output= listeChapitres[x]

    elif direction == 'last':
        if x > 0:
            output= listeChapitres[x-1]
        else:
            output= listeChapitres[x]

    return output


def WebSite():
    app= Flask (__name__)

    app.config.from_object('config.ConfigClass')
    mail = Mail(app)

    chapters=['chapitre1','chapitre2','chapitre3','chapitre4','chapitre5','chapitre6','chapitre7','chapitre8','chapitre9']

    @app.route('/')
    def init():
        return redirect(url_for('home',))

    @app.route('/home')
    def home():
        return render_template('home.html',chapters=chapters,titre_chapitre='Home')

    @app.route('/chapter/<chapter>')
    def chapter(chapter):
        print chapter
        return render_template('chapitres/'+str(chapter)+'.html',navbar=listeChapitres,buttonLast=getChapitreUrl('last',chapter),buttonNext=getChapitreUrl('next',chapter))

    @app.route('/chapitres')
    def chapitres():
        return redirect('/chapter/Introduction')

    @app.route('/ressources')
    def ressources():
        return render_template('ressources.html')

    @app.route('/video')
    def video():
        return render_template('video.html')

    @app.route('/questions',methods=['POST','GET'])
    def questions():
        if request.method == 'POST':
            nom = request.form['nom']
            email = request.form['mail']
            mess = request.form['message']

            try:
                msg = Message('Site HTS',recipients=["loganschwartz@hotmail.com","antoine.dallaire@gmail.com "],body='Nom: ' + nom +'\n\nMail: '+email+'\n\nMessage:\n\n'+mess)
                mail.send(msg)
                output_message=unicode('Votre message a bien été envoyé! nous vous répondrons dans les meilleurs délais. Bonne journée! =)','utf-8')
            except:
                output_message=unicode('Erreur, votre message n\'a pas été envoyé. Vous pouvez me joindre directement à loganschwartz@homail.com','utf-8')
            flash(output_message)
            return render_template('message.html')
        return render_template('questions.html')

    return app

if __name__=='__main__':
    app = WebSite()
    app.run(host='0.0.0.0', port=8085, debug=True)