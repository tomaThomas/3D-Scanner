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
    for ix,iy in np.ndindex(point_list.shape):
        if iy == 0:
            file_pc.write("v " + str(point_list[ix, iy]))
        elif iy == 1:
            file_pc.write(" " + str(point_list[ix, iy]))
        else:
            file_pc.write(" " + str(point_list[ix, iy]) + "\n")
    file_pc.close()

    print("Running meshlabserver...")
    os.system("meshlabserver -i" + path + name + "_pc.obj -o " + path + name + "_mesh.obj -s exporter/cp2mesh.mlx -l pc2mesh_log.txt")
    print("Export finished.")
    return path + name + "_mesh.obj"
