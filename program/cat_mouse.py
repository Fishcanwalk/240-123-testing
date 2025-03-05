def catAndMouse(xyz):
    x, y, z = map(int, xyz)

    if abs(x - z) == abs(y - z):
        return "Mouse C"
    elif abs(z - y) > abs(z - x):
        return "Cat A"
    else:
        return "Cat B"
