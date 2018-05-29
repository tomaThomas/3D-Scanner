import numpy as np

point_list = np.array([])


def create():
    print("Create new object...")
    global point_list
    point_list = np.array([])


def add_row(array):
    print("Adding row...")
    global point_list
    point_list = np.vstack((point_list, array))
    return point_list


def export(name):
    print("Exporting...")
