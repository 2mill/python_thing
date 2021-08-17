from typing import Union
class Terminal:
	def __init__(self, info) -> None:

		#Takes a list of attribute names defined previously
		#Slams it into python's dictionary and pares it with an item in info_item
		# Reverse is critical here.
		attr_names = self.__get_header_info()
		attr_names.reverse()
		for info_item in info:
			self.__setattr__(attr_names.pop(), info_item)

		self.used = self.__translate_symbols_to_bin()
	
	# Returns header information for setting attributes
	def __get_header_info(self) -> list:
		return ["room", "box_label", "port_count", "used", "patch_panel", "patch_port", "parent_room", "comment"]
	# function for converting from my markings into a designation
	def __translate_symbols_to_bin(self) -> Union[int, bool]:
		port_usage = self.used
		if port_usage == "undefined": return False
		temp: list[str] = port_usage.split(' ')
		temp.reverse()
		total: int = 0;
		for x in range(len(temp)):
			total = total + (2**x)*(translate_used_symbols(temp[x]))
		return total

	def __str__(self) -> str:
		output = ""
		for item in self.__dict__:
			if item == "parent_room": continue
			if item == "room":
				output = f"{output}\n{item.capitalize()}:{self.__getattribute__(item)}"
			else:
				output = f"{output}\n-{item}:{self.__getattribute__(item)}"
		return output
	def __eq__(self, oterminal: object) -> bool:
		return self.room == oterminal.room and self.box_label == oterminal.box_label
def translate_used_symbols(symbol: str) -> int:
	return 1 if symbol == 'X' else 0
def get_terminal(info) -> Terminal:
	return Terminal(info)