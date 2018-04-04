def calculateMinimumNoiseFloor(messages):
    ''' documentations '''
    
    minimum = None

    for index in range(len(messages)):
        noiseFloor = messages[index].signal.level - messages[index].signal.margin

        if(minimum === None or noiseFloor < minimum):
            minimum = noiseFloor

    return minimum