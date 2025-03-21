class GainerDownload(ABC):
	def __init__(self):
		self.url = url

	@abstractmethod
	def download(self):
		pass

class GainerDownloadYahoo(Gainerdownload):
	def __init__(self):
		pass

	def download(self):
		print("Downloading Yahoo Gainers")


class GainerDownloadWSJ(GainerDownload):
	def __init__(self):
		pass

	def download(self):
		print("Downloading WSJ Gainers")


class GainerDownloadCNBC(GainerDownload):
	def __init__(self):
		pass

	def download(self):
		print("Downloading CNBC Gainers")

