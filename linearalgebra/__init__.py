import numpy as np

dZ = 400  # Abstand von der Referenzebene zum Mittelpunkt des Drehtellers
d0 = 130  # Abstand der Referenzebene zur Stelle auf der Projektionslinie, das in der linksäußersten Pixelspalte der Kamera erscheint
b = 350  # Abstand von der Laserebene zur Kamera
alphaz = np.arctan(dZ / b)  # Winkel zwischen Referenzebene und Drehtellermittelpunkt
alpha0 = np.arctan(d0 / b)  # Winkel zwischen Referenzebene und linksäußersten Punkt
f = 3.6  # Brennweite der Kamera (mm)
d = f * np.tan(alphaz - alpha0)  # halber Durchmesser des Sensors
M = 800  # Anzahl Spalten pro Bild
N = 600  # Anzahl Zeilen im Bild
c = 300 / 500  # Streckungsfaktor
jZ = 500  # Zeilenindex Mittelpunkt vom Drehteller
distance_cam_center = np.sqrt(dZ * dZ + b * b)  # abstand Mittelpunkt drehteller zur kamera


async def transform(array, angle):
    res = np.zeros((array.shape[0], 3))
    for index, coordinates in enumerate(array):
        res[index] = rotate(calculateCoordinates(coordinates),angle)
    return res


def calculateCoordinates(pixel_coordinates):
    distance = abstand_projektionsebene(pixel_coordinates[0])
    x = dZ - distance
    z = 0
    distance_point_cam = np.sqrt(distance * distance + b * b)
    y = (pixel_coordinates[1] * c)
    '''+ ((N // 2 * c - (pixel_coordinates[1] * c)) / distance_cam_center) * (
            distance_cam_center - distance_point_cam)'''
    y = y - (N - jZ) * c
    return x, y   #z=0


def rotate(coordinates,angle):
    return np.array([coordinates[0] * np.cos(angle), coordinates[1], -coordinates[0]*np.sin(angle)])

# Berechnet den Abstand des gefundenen Punktes zum Linienlaser
def abstand_projektionsebene(k):
    if k <= (M // 2):
        phi_k = np.arctan(d * (M - 2 * k) / M * f)
        alphak = alphaz - phi_k
        return b * np.tan(alphak)
    else:
        phi_k = np.arctan(d * (2 * k - M) / M * f)
        alphak = alphaz + phi_k
        return b * np.tan(alphak)

