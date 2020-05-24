from Core.Request_Site import Get_Request
class Get_File(Get_Request):
	def __init__(self,page,imagesave_path):
		super().__init__()
		self.page = page
		self.imagesave_path = imagesave_path
	def save_Image(self):
		self.get_Html()
		with open(self.imagesave_path,'wb') as f:
			image = self.respones
			f.write(image.content)

	@classmethod
	def run_Image(cls,page,imagesave_path):
		return cls(page,imagesave_path).save_Image()
