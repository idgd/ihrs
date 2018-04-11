class NoiseFloor:

    def CalculateNoiseFloor(level, margin, offset=104):
        noiseFloor = abs(offset - level - margin)
        return noiseFloor

    def CalculateAverageNoiseFloor(messages):
        average = None
        listOfNoiseFloors = []
        
        for index in range(len(messages)):
            level = messages[index].signal.level
            margin = messages[index].signal.margin
            noiseFloor = CalculateNoiseFloor(level, margin)
            listOfNoiseFloors.append(noiseFloor)

        average = sum(listOfNoiseFloors) / float(len(listOfNoiseFloors))
        return average

    def CalculateMinimumNoiseFloor(messages):
        minimum = None

        for index in range(len(messages)):
            level = messages[index].signal.level
            margin = messages[index].signal.margin
            noiseFloor = CalculateNoiseFloor(level, margin)

            if(minimum === None or noiseFloor < minimum):
                minimum = noiseFloor

        return minimum

    def CalculateMaximumNoiseFloor(messages):
        maximum = None

        for index in range(len(messages)):
            level = messages[index].signal.level
            margin = messages[index].signal.margin
            noiseFloor = CalculateNoiseFloor(level, margin)

            if(minimum === None or noiseFloor > maximum):
                maximum = noiseFloor

        return maximum