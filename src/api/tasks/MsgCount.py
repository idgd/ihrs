class MsgCount:

	def CalculateAveragePerSec(self, messages):
		average = []
		for f in messages:
			if "time" in f:
				average.append(f["time"])

		return((average[-1] - average[0]) / len(average))

	def CalculateRedundantCount(self, messages):
		redundant = []
		for f in range(1,len(messages)):
			if "time" in messages[f] and "time" in messages[f - 1]:
				if abs(messages[f]["time"] - messages[f - 1]["time"]) < 0.25:
					redundant.append(0)

		return(len(redundant))
