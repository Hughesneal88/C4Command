from cmd import Cmd
from modules.TextColor import *
from modules.connect import Listen

#global variables
global default
default = Fore.BLACK
class Console(Cmd):
	intro = red("""
			C4Command C2
  ======================================
	        8888888888888888
	      88888888888888888888
	    888888             8888
	   888888
	  88888                     888
	 88888           88       8888
	88888          8888     888888888888888888888888888888
	88888         88 88   88888888888888888888888888888888
	88888        88  88     888888888888888888888888888888
	88888       88   88       8888
	888888     88    88          888                         8
	 888888   88888888888  888                               8
	  888888         88   88   888 888888 888888 8888 8888 888
	   888888        88   88   8 8 8 88 8 8 88 8 8 88 8  8 8 8
	    888888       88    888 888 8 88 8 8 88 8 8888 8  8 888 0
	     888888                                   8 
	      8888888          8888
	        888888888888888888
	          888888888888888
	         
	""")
	TEXT_COLOR = default
	prompt = f"{Fore.BLUE}|C4|>_| {Fore.RESET}{TEXT_COLOR}"
	def do_info(self, inputted):
		"""About the Program"""
		info ="""C4Command <-|=|
		This is a console version for the C4Command C2
		It is a project by Allison
		"""
		
	def do_exit(self, inputted):
		"""Exit the Program"""
		print(Fore.RESET)
		exit()
	def do_listen(self, port):
		Host = '0.0.0.0'
		port = port
		Listen(Host, port)
		command = None
		try:	
			while command != b"exit":
				command = input(f"C4 Connected|>_ ")
				Listen.send(command.encode())
				output = Listen.recvlines()
				print(output.decode())
		except Exception as e:
			print(e)

if __name__ == '__main__':
	Console().cmdloop()
