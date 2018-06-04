import numpy as np

dZ = 0  # Abstand von der Referenzebene zum Mittelpunkt des Drehtellers
d0 = 0  # Abstand der Referenzebene zur Stelle auf der Projektionslinie, das in der linksäußersten Pixelspalte der Kamera erscheint
b = 1  # Abstand von der Laserebene zur Kamera
alphaz = np.arctan(dZ / b)  # Winkel zwischen Referenzebene und Drehtellermittelpunkt
alpha0 = np.arctan(d0 / b)  # Winkel zwischen Referenzebene und linksäußersten Punkt
f = 3.6  # Brennweite der Kamera (mm)
d = f * np.tan(alphaz - alpha0)  # halber Durchmesser des Sensors
M = 800  # Anzahl Spalten pro Bild
N = 600  # Anzahl Zeilen im Bild
c = 0  # Streckungsfaktor
jZ = 0  # Zeilenindex Mittelpunkt vom Drehteller
distance_cam_center = np.sqrt(dZ * dZ + b * b)  # abstand Mittelpunkt drehteller zur kamera


def transform(array, angle):
    res = np.zeros((array.shape[0], 3))
    for index, coordinates in enumerate(array):
        res[index] = calculateCoordinates(array, angle)
    return np.array()


def calculateCoordinates(pixel_coordinates, angle):
    distance = abstand_projektionsebene(pixel_coordinates[0])
    r = np.abs(dZ - distance)
    if (angle >= 0 and angle < np.pi / 2 and distance < dZ):
        x = r * np.sin(angle)
        z = -np.sqrt(r * r - x * x)
    elif (angle >= 0 and angle < np.pi / 2 and distance > dZ):
        x = -r * np.sin(angle)
        z = np.sqrt(r * r - x * x)
    elif (angle >= np.pi / 2 and angle < np.pi and distance < dZ):
        x = r * np.sin(angle)
        z = np.sqrt(r * r - x * x)
    elif (angle >= np.pi / 2 and angle < np.pi and distance > dZ):
        x = -r * np.sin(angle)
        z = -np.sqrt(r * r - x * x)
    elif (angle >= np.pi and angle < 3 / 2 * np.pi and distance < dZ):
        x = -r * np.sin(angle)
        z = np.sqrt(r * r - x * x)
    elif (angle >= np.pi and angle < 3 / 2 * np.pi and distance > dZ):
        x = r * np.sin(angle)
        z = -np.sqrt(r * r - x * x)
    elif (angle >= 3 / 2 * np.pi and angle < 2 * np.pi and distance < dZ):
        x = -r * np.sin(angle)
        z = np.sqrt(r * r - x * x)
    elif (angle >= 3 / 2 * np.pi and angle < 2 * np.pi and distance > dZ):
        x = r * np.sin(angle)
        z = -np.sqrt(r * r - x * x)
    distance_point_cam = np.sqrt(distance * distance + b * b)
    y = (pixel_coordinates[1] * c) + ((N // 2 * c - (pixel_coordinates[1] * c)) / distance_cam_center) * (
            distance_cam_center - distance_point_cam)
    y = y - (N - jZ) * c
    return np.array([x, y, z])


# Berechnet den Abstand des gefundenen Punktes zum Linienlaser
def abstand_projektionsebene(k):
    if k <= M // 2:
        phi_k = np.arctan(d * (M - 2 * k) / M * f)
        alphak = alphaz - phi_k
        return b * np.tan(alphak)
    else:
        phi_k = np.arctan(d * (2 * k - M) / M * f)
        alphak = alphaz + phi_k
        return b * np.tan(alphak)
