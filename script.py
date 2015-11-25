import math
from Tkinter import *


def getMatrix():
    L = [None] * 3
    for j in range(3):
        print "Ligne " + str(j) + "\n"
        L[j] = [None] * 3
        for i in range(3):
            L[j][i] = input("Terme " + str(i) + "\n")
    return L


def getPoint():
    L = [None] * 3
    for j in range(2):
        L[j] = input("Terme " + str(j) + "\n")
    L[2] = 1
    return L


def PrintPoint(L):
    s = "[" + str(L[0]) + "," + str(L[1]) + "," + str(L[2]) + "]"
    print s


def PrintMatrix(L):
    s = "[" + str(L[0][0]) + "," + str(L[0][1]) + "," + str(L[0][2]) + "]"
    print s
    s = "[" + str(L[1][0]) + "," + str(L[1][1]) + "," + str(L[1][2]) + "]"
    print s
    s = "[" + str(L[2][0]) + "," + str(L[2][1]) + "," + str(L[2][2]) + "]"
    print s


def MatrixProduct(L, M):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(L)):
        for j in range(len(M[0])):
            for k in range(len(M)):
                result[i][j] += L[i][k] * M[k][j]
    return result


def MatrixPointProduct(L, P):
    result = [0, 0, 0]
    for i in range(len(L)):
        for j in range(len(P)):
            result[i] += L[i][j] * P[j]
    return result


def GenRotationMatrix(teta):
    L = [[math.cos(teta), -math.sin(teta), 0],
         [math.sin(teta), math.cos(teta), 0],
         [0, 0, 1]]
    return L


def GenHomothetieMatrix(k):
    L = [[k, 0, 0],
         [0, k, 0],
         [0, 0, 1]]
    return L


def GenTranslationMatrix(a, b):
    L = [[1, 0, a],
         [0, 1, b],
         [0, 0, 1]]
    return L


def GenCentredRotationMatrix(teta, a, b):
    return MatrixProduct(MatrixProduct(GenRotationMatrix(teta), GenTranslationMatrix(-a, -b)),
                         GenTranslationMatrix(a, b))


def GenCentredHomothetieMatrix(k, a, b):
    return MatrixProduct(MatrixProduct(GenHomothetieMatrix(k), GenTranslationMatrix(-a, -b)),
                         GenTranslationMatrix(a, b))


def GetPolygon():
    nb = input("Combien de point voulez vous ?")
    L = [None] * nb
    for i in range(nb):
        L[i] = getPoint()
    return L


def GetFace():
    nb = input("Combien de polygone voulez vous ?")
    L = [None] * nb
    for i in range(nb):
        L[i] = GetPolygon()
    return L


def addPoint(polygon, a, b):
    L = [None] * (len(polygon) + 1)
    for i in range(len(polygon)):
        L[i] = polygon[i]
    L[len(polygon)] = [None] * 3
    L[len(polygon)][0] = a
    L[len(polygon)][1] = b
    L[len(polygon)][2] = 1
    return L


def addPolygon(face, polygon):
    L = [None] * (len(face) + 1)
    for i in range(len(face)):
        L[i] = face[i]
    L[len(face)] = polygon
    return L


def ApplyModif(face, matrix):
    for i in range(len(face)):
        for j in range(len(face[i])):
            face[i][j] = MatrixPointProduct(matrix, face[i][j])
    return face


def DisplayFace(face):
    fenetre = Tk()
    can = Canvas(fenetre, height=720, width=1280)
    for i in range(len(face)):
        for j in range(len(face[i])):
            if j % 2 == 0 and (j % 2 + 1) != len(face[i]):
                can.create_line(face[i][j][0], face[i][j][1], face[i][j + 1][0], face[i][j + 1][1], width=2,
                                fill='black')
    can.pack()
    fenetre.mainloop()


DisplayFace(GetFace())
