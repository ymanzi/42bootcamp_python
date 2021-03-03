import numpy as np

def add_intercept(x):
	"""Adds a column of 1's to the non-empty numpy.ndarray x.
	Args:
		x: has to be an numpy.ndarray, a vector of dimension m * 1.
	Returns:
		X as a numpy.ndarray, a vector of dimension m * 2.
		None if x is not a numpy.ndarray.
		None if x is a empty numpy.ndarray.
	Raises:
		This function should not raise any Exception.
	"""
	if x.ndim == 1:
		return np.array([[1.0, elem] for elem in x])
	else:
		lst = []
		for elem in x:
			tmp = elem.tolist()
			tmp.insert(0, 1.0)
			lst.append(tmp)
		return np.array(lst)
	return x

def predict_(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
	Args:
		x: has to be an numpy.ndarray, a vector of dimension m * 1.
		theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
		y_hat as a numpy.ndarray, a vector of dimension m * 1.
		None if x or theta are empty numpy.ndarray.
		None if x or theta dimensions are not appropriate.
	Raises:
		This function should not raise any Exception.
	"""
	if not isinstance(x, np.ndarray) \
		or not isinstance(theta, np.ndarray) \
		or (x.ndim == 1 and theta.ndim != 1) \
		or (x.ndim != 1 and x.shape[1] + 1 != theta.size ):
		return None 

	x_matrix = add_intercept(x)
	theta = [[elem] for elem in theta]

	new_m = []
	for elem in x_matrix:
		tmp = []
		for elem2 in theta[0]:
			tmp.append(0)
		new_m.append(tmp)
	for v1_x in range(len(x_matrix)):
		for v1_y in range(len(x_matrix[0])):
			for v2_y in range(len(theta[0])):
				new_m[v1_x][v2_y] += x_matrix[v1_x][v1_y] * theta[v1_y][v2_y]
	new_m = [elem for lst in new_m for elem in lst]
	return np.array(new_m)

x = np.arange(1,6)
theta1 = np.array([5, 3])
print(predict_(x, theta1))
