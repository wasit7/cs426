from mrjob.job import MRJob

class statusCount(MRJob):
	def getStatus(self, key, record):
		data = record.split(';')[3]
		yield data,1	

	def frequency(self, state , value):
		yield state, sum(value)
	def sumMapper(self, state, freq):
		yield 1,freq
	def sumReducer(self, key, value):
		yield 'Number of students',sum(value)
	def steps(self):
		return [self.mr(mapper=self.getStatus,reducer=self.frequency),
			self.mr(mapper=self.sumMapper,reducer=self.sumReducer)]

if __name__ == '__main__' :
	statusCount.run()
