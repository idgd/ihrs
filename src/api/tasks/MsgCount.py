class MsgCount:

	def CalculateAveragePerSec(self, messages):
		average = []
		for f in messages:
			if "timestamp" in f:
				average.append(f["timestamp"])

		return(sum(average) / len(average))
