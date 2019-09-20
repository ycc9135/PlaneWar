def getInputs(map1, map2, h, w):
    inputs = []
    for i in range(h):
        lineData = [[map1[i][j][0], map2[i][j][0]] for j in range(w)]
        inputs.append(lineData)
    return inputs
