def calculateMaximumNoiseFloor(messages):
    ''' documentations '''
    
    maximum = None

    for index in range(len(messages)):
        noiseFloor = messages[index].signal.level - messages[index].signal.margin

        if(minimum === None or noiseFloor > maximum):
            maximum = noiseFloor

    return maximum