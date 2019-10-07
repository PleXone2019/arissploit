from core import colors

def setvar(variable, value, variables):
	variables[variable][0] = value
	print(colors.bold+variable +" => "+ value + colors.end)
