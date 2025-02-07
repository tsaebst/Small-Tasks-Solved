import matplotlib.pyplot as plt
from functools import cmp_to_key
from matplotlib.patches import Polygon


def creating_alg(verts_array, min_y_value):
    # Find the lowest point
    for i in range(len(verts_array)):
        if verts_array[i][1] <= min_y_value[1]:
            if verts_array[i][1] < min_y_value[1]:
                min_y_value = verts_array[i]
            else:
                min_y_value = min(verts_array[i], min_y_value, key=lambda x: (x[0], x[1]))

    # Compute determinant of the vector cross product
    def det(p1, p2, origin=min_y_value):
        return (p2[0] - origin[0]) * (p1[1] - origin[1]) - (p1[0] - origin[0]) * (p2[1] - origin[1])

    def hull(verts_array):
        verts_array.remove(min_y_value)
        verts_array.sort(key=cmp_to_key(det))
        hull = [min_y_value, verts_array[0], verts_array[1]]
        n = len(verts_array)
        i = 2
        while i < n:
            while len(hull) > 1 and det(verts_array[i], hull[-2], origin=hull[-1]) > 0:
                hull.pop()
            hull.append(verts_array[i])
            i += 1
        return hull

    def output(verts_array, hull):
        fig, ax1 = plt.subplots()
        verts_array.append(hull[0])
        x = [p[0] for p in verts_array]
        y = [p[1] for p in verts_array]
        ax1.plot(x, y, marker=".", linestyle='None')
        xy = list(zip([p[0] for p in hull], [p[1] for p in hull]))
        ax1.add_patch(Polygon(xy, alpha=0.2))
        plt.show()

    hull = hull(verts_array)
    output(verts_array, hull)
    return


if __name__ == "__main__":
    verts = []
    min_y_value = (float('inf'), float('inf'))
    file = "/your/path/data.txt"
    with open(file, 'r') as fp:
        fp.readline()
        for line in fp:
            coordinates = line.split()
            verts.append([int(coordinates[0]), int(coordinates[1])])

    creating_alg(verts, min_y_value)
