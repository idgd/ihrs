def calculateAverageNoiseFloor(messages):
    ''' documentations '''
        
    average = None
    listOfNoiseFloors = []
    
    for index in range(len(messages)):
        noiseFloor = messages[index].signal.level - messages[index].signal.margin
        listOfNoiseFloors.append(noiseFloor)

    average = sum(listOfNoiseFloors) / float(len(listOfNoiseFloors))

    return average