import pandas

def read_csv(filename):
	data = pandas.read_csv(filename, header=0, index_col=0).T
	data.index = pandas.read_csv(filename, header=None, index_col=0).iloc[0].values
	return data

if __name__ == '__main__': print("lab.py")
