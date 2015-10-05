# -*- coding: utf-8 -*-
class Factorial:
	def get_factorial(self, num):
		if num==0 or num==1:
			return 1
		return num*self.get_factorial(num-1)