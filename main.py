from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Model (object):
	def __init__ (self):
		'''initialize our linear model with a random slope and y intercept'''
		self.m = np.random.randn()
		self.b = np.random.randn()

	def eval(self, x):
		'''use the model (the line) to make a prediction'''
		return self.m * x + self.b

	def cost(self, xs, ys):
		'''Evaluates the model error on a set of inputs (xs) and outputs (ys)
		with a mean squared cost function. Multiply by one half so the Power
		Rule expression is simplified later...'''
		return 0.5 * np.mean((self.eval(xs)-ys) ** 2)

	def BGD(self, xs, ys, learning_rate, epochs):
		'''Batch Gradient Descent: takes data inputs, outputs, learning rate
		and number of epochs to train for'''
		for e in range(epochs):
			nabla_m = np.mean((self.eval(xs) - ys) * xs) #deriv. with respect to m
			nabla_b = np.mean(self.eval(xs) - ys) #deriv. with respect to b
			#parameter updates...
			self.m = self.m - learning_rate * nabla_m
			self.b = self.b - learning_rate * nabla_b
			#Periodically logs the model's progress
			if e % 20 == 0:
				print ("Epoch {} Loss = {}".format(e, self.cost(xs, ys)))

def get_points(PATH):
	data = np.genfromtxt(PATH, delimiter=',') #loads the csv into an array
	'''The subjects list contains tuples corresponding to each study subject's
	average perceived intelligence and average match success'''
	subjects = []
	n = 1
	while n < len(data):
		subject_num = data[n][1]
		intel_avg = 0
		match_avg = 0
		potential_partners = 0
		while n < len(data) and data[n][1] == subject_num:
			intel_avg += data[n][2]
			match_avg += data[n][3]
			potential_partners += 1
			n += 1
		intel_avg /= potential_partners
		match_avg /= potential_partners
		subjects.append((intel_avg, match_avg))
	intels = np.array([d[0] for d in subjects])
	print ("Mean Perceived Intelligence: {} / 10".format(np.mean(intels)))
	print ("Intelligence std: {}".format(np.std(intels))) #log the std. deviation of the subjects' perceived intelligence
	intels = (intels - np.mean(intels)) / np.std(intels) #gaussian normalize the intelligence values
	matches = np.array([d[1] for d in subjects])
	print ("Mean Match Success: {}%".format(np.mean(matches) * 100))
	print ("Match Success std: {}".format(np.std(matches))) #log the std. deviation of the subjects' match success
	matches = (matches - np.mean(matches)) / np.std(matches) #gaussian normalize the match success values
	return (intels, matches)

if __name__ == "__main__":
	print (" <--- ARE PERCEIVED INTELLIGENCE AND SPEED-DATING SUCCESS CORRELATED? -->")
	print (" <--- Let's find out... --->")

	xs, ys = get_points('data.csv')
	print ("<--- POINTS LOADED --->")
	m = Model()
	m.BGD(xs, ys, 0.1, 200)
	print ("<--- RESULTS --->")
	print ("m = {}, b = {}".format(m.m, m.b))
	plt.scatter(xs, ys)
	plt.plot(xs, m.eval(xs))
	plt.show()
