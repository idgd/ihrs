'''t'''

class NoiseFloor:
    '''t'''

    def calculateAverageNoiseFloor(messages):
        ''' documentations '''
            
        average = None
        listOfNoiseFloors = []
        
        for index in range(len(messages)):
            noiseFloor = messages[index].signal.level - messages[index].signal.margin
            listOfNoiseFloors.append(noiseFloor)

        average = sum(listOfNoiseFloors) / float(len(listOfNoiseFloors))

        return average

    def calculateMinimumNoiseFloor(messages):
        ''' documentations '''
        
        minimum = None

        for index in range(len(messages)):
            noiseFloor = messages[index].signal.level - messages[index].signal.margin

            if(minimum === None or noiseFloor < minimum):
                minimum = noiseFloor

        return minimum

    def calculateMaximumNoiseFloor(messages):
    ''' documentations '''
    
    maximum = None

    for index in range(len(messages)):
        noiseFloor = messages[index].signal.level - messages[index].signal.margin

        if(minimum === None or noiseFloor > maximum):
            maximum = noiseFloor

    return maximum