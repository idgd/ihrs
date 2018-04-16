class NoiseFloor:

    def CalculateNoiseFloor(self, level, margin, offset=104):
        noiseFloor = abs(offset - level - margin)
        return noiseFloor

    def CalculateAverageNoiseFloor(self, messages):
        average = None
        listOfNoiseFloors = []
        for f in messages:
            if "signal" in f:
                level = f["signal"]["level"]
                margin = f["signal"]["margin"]
                noiseFloor = self.CalculateNoiseFloor(level,margin)
                listOfNoiseFloors.append(noiseFloor)

        average = sum(listOfNoiseFloors) / float(len(listOfNoiseFloors))
        return average

    def CalculateMinimumNoiseFloor(self, messages):
        minimum = None

        for f in messages:
            if "signal" in f:
                level = f["signal"]["level"]
                margin = f["signal"]["margin"]
                noiseFloor = self.CalculateNoiseFloor(level, margin)

                if(minimum == None or noiseFloor < minimum):
                    minimum = noiseFloor

        return minimum

    def CalculateMaximumNoiseFloor(self, messages):
        maximum = None

        for f in messages:
            if "signal" in f:
                level = f["signal"]["level"]
                margin = f["signal"]["margin"]
                noiseFloor = self.CalculateNoiseFloor(level, margin)

                if(maximum == None or noiseFloor > maximum):
                    maximum = noiseFloor

        return maximum
