import numpy as np
import os

path = "web-interface/data/"
point_list = np.array([]).reshape(0, 3)


def create():
    print("Creating new object...")

    global point_list
    point_list = np.array([]).reshape(0, 3)


def add_row(array):
    print("Adding row...")

    point_count = array.shape[0];
    array = np.reshape(array, (point_count, 3))

    global point_list
    point_list = np.append(point_list, array, axis=0)
    return point_list


def export(name):
    print("Exporting...")

    file_pc = open(path + name + "_pc.obj", "w")
    for x in range(0, point_list.shape[0]):
        file_pc.write("v " + str(point_list[x][0]) + " " + str(point_list[x][1]) + " " + str(point_list[x][2]) + "\n")
    file_pc.close()

    print("Running meshlabserver...")
    os.system("meshlabserver -i" + path + name + "_pc.obj -o " + path + name + "_mesh.obj -s exporter/cp2mesh.mlx -l pc2mesh_log.txt")
    print("Export finished.")

    return path + name + "_mesh.obj"
