from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Model:
	def __init__ (self):
		self.m = np.random.randn()
		self.b = np.random.randn()
	def eval(self, x):
		return self.m * x + self.b
	def cost(self, xs, ys):
		return 0.5 * np.mean((self.eval(xs)-ys) ** 2)
	def BGD(self, xs, ys, alpha, epochs):
		for e in xrange(epochs):
			nabla_m = np.mean((self.eval(xs) - ys) * xs)
			nabla_b = np.mean(self.eval(xs) - ys)
			self.m = self.m - alpha * nabla_m
			self.b = self.b - alpha * nabla_b
			print "Loss = {}".format(self.cost(xs, ys))

def get_data(n):
	xs = np.arange(-40, 80, 80 / n)
	ys = xs + 3.5*np.random.randn(xs.shape[0])
	return xs, ys

xs, ys = get_data(50)
plt.scatter(xs, ys)
plt.show()
reg = Model()

for i in xrange(10):
	reg.BGD(xs, ys, 0.0001, 1)
	plt.scatter(xs, ys)
	plt.plot(xs, reg.eval(xs))
	plt.show()
