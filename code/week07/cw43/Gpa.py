from mrjob.job import MRJob

class GpaCount(MRJob):
	def mapper(self, key, record):
		data = record.split(';')[7]
		try :
			data = float(data)
			yield (data >= 3.0),1
		except :
			pass		

	def reducer(self, state , value):
		yield state, sum(value)

if __name__ == '__main__' :
	GpaCount.run()
