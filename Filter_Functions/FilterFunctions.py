
class FiltersFunctions:
	def __init__(self):
		
	def gaussian_kde(self, cloud, metric):
		kernel = stats.gaussian_kde(data.transpose())
		kernel.silverman_factor()
		kernel = kernel(data.transpose())
		np.save('npy_files/GAUSSIAN_KDE_' + file_name, kernel)
		return kernel
