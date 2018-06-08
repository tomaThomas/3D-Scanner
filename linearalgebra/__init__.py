import numpy as np

dZ = 356  # Abstand von der Referenzebene zum Mittelpunkt des Drehtellers
d0 = 113  # Abstand der Referenzebene zur Stelle auf der Projektionslinie, das in der linksäußersten Pixelspalte der Kamera erscheint
b = 365  # Abstand von der Laserebene zur Kamera
alphaz = np.arctan(dZ / b)  # Winkel zwischen Referenzebene und Drehtellermittelpunkt
alpha0 = np.arctan(d0 / b)  # Winkel zwischen Referenzebene und linksäußersten Punkt
f = 3.6  # Brennweite der Kamera (mm)
d = f * np.tan(alphaz - alpha0)  # halber Durchmesser des Sensors
M = 640  # Anzahl Spalten pro Bild (wird durch init neu gesetzt)
N = 480  # Anzahl Zeilen im Bild (wird durch init neu gesetzt)
c = 12.3448  # Streckungsfaktor
jZ = 412  # Zeilenindex Mittelpunkt vom Drehteller
distance_cam_center = np.sqrt(dZ * dZ + b * b)  # abstand Mittelpunkt drehteller zur kamera


def init(width, height):
    M = width
    N = height


async def transform(array, angle):
    res = []
    for coordinates in array:
        distance = abstand_projektionsebene(M - coordinates[0])
        if np.abs(dZ - distance) <= 150:   #Punkte außerhalb des Drehtellers werden ignoriert
            res.append(rotate(calculate_coordinates(distance,N - coordinates[1])))
    return np.array(res)

def calculate_coordinates(distance, y_pixel, angle):
    x = dZ - distance
    distance_point_cam = np.sqrt(distance * distance + b * b)
    y = (y_pixel * c) #+ ((N // 2 * c - (y_pixel * c)) / distance_cam_center) * (distance_cam_center - distance_point_cam)
    y = y - (N - jZ) * c
    return [x, y]  # z=0

def rotate(coordinates, angle):
    return [coordinates[0] * np.cos(angle), coordinates[1], -coordinates[0] * np.sin(angle)]


# Berechnet den Abstand des gefundenen Punktes zum Linienlaser
def abstand_projektionsebene(k):
    if k <= (M // 2):
        phi_k = np.arctan(d * (M - 2 * k) / (M * f))
        alphak = alphaz - phi_k
        return b * np.tan(alphak)
    else:
        phi_k = np.arctan(d * (2 * k - M) / (M * f))
        alphak = alphaz + phi_k
        return b * np.tan(alphak)