## Q28
class fancyPrint:
	message = ""
	
	@classmethod
	def setMessage(cls, new_message):
		cls.message = new_message
		
	@staticmethod
	def fancyPrint():
		print(fancyPrint.message.upper())
		
fancyPrint.fancyPrint()
fancyPrint.setMessage("hello world")
fancyPrint.fancyPrint()
fancyPrint.setMessage("GOODBYE WORLD")
fancyPrint.fancyPrint()

## Q29
def makeFancy(func):
	def wrapper():
		print("*" *  len(fancyPrint.message))
		func()
		print("*" * len(fancyPrint.message))
		print(f"*" * (int(0.5 * len(fancyPrint.message))))
		
	return wrapper
	
	
class fancyPrint:
	message = ""
	
	@classmethod
	def setMessage(cls, new_message):
		cls.message = new_message
		
	@staticmethod
	@makeFancy
	def fancyPrint():
		print(fancyPrint.message.upper())
		
fancyPrint.fancyPrint()
fancyPrint.setMessage("hello world")
fancyPrint.fancyPrint()
fancyPrint.setMessage("GOODBYE WORLD")
fancyPrint.fancyPrint()
		
		

		
		
		