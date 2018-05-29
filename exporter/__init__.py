import numpy as np
import os

path = "web-interface/data/"
point_list = np.array([])


def create():
    print("Creating new object...")
    global point_list
    point_list = np.array([])


def add_row(array):
    print("Adding row...")
    global point_list
    point_list = np.vstack((point_list, array))
    return point_list


def export(name):
    print("Exporting...")
    file_pc = open(path + name + "_pc.obj", "w")
    for point in np.nditer(point_list):
        file_pc.write("v " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]) + "\n")
    file_pc.close()
    print("Running meshlabserver...")
    os.system("meshlabserver -i" + path + name + "_pc.obj -o " + path + name + "_mesh.obj -s exporter/cp2mesh.mlx -l pc2mesh_log.txt")
    print("Export finished.")
    return path + name + "_mesh.obj"
