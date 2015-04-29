from mrjob.job import MRJob

class Count(MRJob):
	def mapper(self, key, record):
		data = record.split(';')[6]
		if len(data) != 0 :
			date = data.split()[0]
			month = date.split('/')
			if len(month) == 3 :
				yield month[1]+'/'+month[2],1
	def reducer(self, month, births):
		yield month, sum(births)

if __name__ == '__main__':
	Count.run()
