import sqlite3
import eel
from mdpOublie import MdpOublieView
from faceRecognition import recognition
import graph

eel.init("web")


@eel.expose
def login(user, pwd):
    db = sqlite3.connect('web/asset/db/db.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT id FROM user WHERE username = '{user}' AND passwd = '{pwd}'")
    if(cursor.fetchall() != []):
        return 1
    else :
        return 0
        
@eel.expose
def getpwd(email):
    print('got into sendmail function')
    user = MdpOublieView(email)
    if user.sendMail() :
        del(user)
        return 1
    else :
        del(user)
        return 0

@eel.expose
def faceRecognition():
    print('get into face recognition')
    return recognition()


@eel.expose
def dessiner(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    return graph.dessiner(l0, l1, l2, o1, o2, xb, yb, nbpas, temp)

@eel.expose
def simuler(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    return graph.simuler(l0, l1, l2, o1, o2, xb, yb, nbpas, temp)

eel.start("index.html", mode = False)
