from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Model (object):
	def __init__ (self):
		'''initialize a model for linear regression'''
		self.m = np.random.randn()
		self.b = np.random.randn()

	def eval(self, x):
		'''use the model (the line) to make a prediction'''
		return self.m * x + self.b

	def cost(self, inputs, outputs):
		'''mean squared error function'''
		return 0.5 * np.mean((self.eval(xs)-ys) ** 2)

	def BGD(self, xs, ys, alpha, epochs):
		for e in xrange(epochs):
			nabla_m = np.mean((self.eval(xs) - ys) * xs)
			nabla_b = np.mean(self.eval(xs) - ys)
			self.m = self.m - alpha * nabla_m
			self.b = self.b - alpha * nabla_b
			print "Loss = {}".format(self.cost(xs, ys))

def get_points(PATH):
	data = np.genfromtxt(PATH, delimiter=',') #loads the csv into an array
	print data.shape
	subjects = []
	n = 1
	while n < len(data):
		subject_num = data[n][1]
		intel_avg = 0
		match_avg = 0
		potential_partners = 0
		while data[n][1] == subject_num and n < len(data):
			intel_avg += data[n][2]
			match_avg += data[n][3]
			potential_partners += 1
			n += 1
		intel_avg /= potential_partners
		match_avg /= potential_partners
		subjects.append((intel_avg, match_avg))
	intels = np.array([d[0] for d in subjects])
	intels = (intels - np.mean(intels)) / np.std(intels)
	matches = np.array([d[1] for d in subjects])
	matches = (matches - np.mean(matches)) / np.std(matches)
	subjects_normalized = [(x, y) for x, y in zip(intels, matches)]
	return subjects_normalized

if __name__ == "__main__":
	points = get_points('data.csv')
	print "points loaded" #improve formatting later, ERIC
	m = Model()
	print "model created!"
	xs = [d[0] for d in points]
	ys = [d[1] for d in points]
	plt.scatter(xs, ys)
	plt.show()
