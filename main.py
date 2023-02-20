import sqlite3
import eel
from mdpOublie import MdpOublieView
from faceRecognition import recognition
# from faceRecognition import release_cam
import graph

eel.init("web")

print('starting server at port 8000')

@eel.expose
def login(user, pwd):
    db = sqlite3.connect('web/db/db.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT id FROM user WHERE email = '{user}' AND pwd = '{pwd}'")
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
def faceRecognition(release):
    print('\n get into face recognition\n')
    return recognition(release)

# @eel.expose
# def release_cam():
#     print('Releasing cam ...')
#     print (release_cam())

@eel.expose
def dessiner(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    return graph.dessiner(l0, l1, l2, o1, o2, xb, yb, nbpas, temp)

@eel.expose
def simuler(l0, l1, l2, o1, o2, xb, yb, nbpas, temp):
    return graph.simuler(l0, l1, l2, o1, o2, xb, yb, nbpas, temp)

@eel.expose
def start() :
    return graph.init()

eel.start("index.html", mode = False)
