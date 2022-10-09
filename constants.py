class R:
	def __init__(self, label, a, b, c, radius, weight):
		self.label = label
		self.a = a
		self.b = b
		self.c = c
		self.radius = radius
		self.weight = weight
		
		self.reg_values = []
		self.real_constant = radius*weight
	def reg_f(self, x):
		force = self.a*(x**2) + self.b*x + self.c 
		self.reg_values.append(force/(x**2))
		return force		

	def real_f(self, x):
		return self.real_constant * (x**2)	
	def get_average_constant(self):
		total = 0
		for y in self.reg_values:
			total += y
		average = total/len(self.reg_values)
		return average
	def print_results(self):
		print(f'{self.label}) medelvärde: {self.get_average_constant()}, korrekt: {self.real_constant}, skillnad: {self.get_average_constant() - self.real_constant}')
f = R('Diagram 1', 0.0173, 0.0609, -0.125, 0.13, 0.150)	
g = R('Diagram 2', 0.0301, 0.0521, 0.0225, 0.13, 0.250)
h = R('Diagram 3', 0.0349, 0.0665, -0.0478, 0.13, 0.300)
i = R('Diagram 4', 0.0389, 0.0492, 0.0654, 0.17, 0.250)

test_intervall = [(i+1) for i in range(0,100)]
for x in test_intervall:
	f.reg_f(x)
	g.reg_f(x)
	h.reg_f(x)
	i.reg_f(x)

f.print_results()
g.print_results()
h.print_results()
i.print_results()
