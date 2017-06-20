from __future__ import division
import numpy as np
import pandas as pd

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

if __name__ == "main":
	m = Model()
	print "model created!"
