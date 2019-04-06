import io, sys


def weight_on_planets():
	weight = input('What do you weigh on earth? ') # Get input from user
	weight = int(weight)
	mars = weight*0.38 # Convert to weight on mars
	jupiter = weight*2.34 # Convert to weight on jupiter

	print('\nOn Mars you would weigh',str(mars),'pounds.\nOn Jupiter you would weigh',str(jupiter),'pounds.')   
   
   
if __name__ == '__main__':
   weight_on_planets()