from typing import Union
import patch_panel

class Port:
	def __init__():
		pass
class Terminal:
	def __init__(self, info) -> None:

		#Takes a list of attribute names defined previously
		#Slams it into python's dictionary and pares it with an item in info_item
		# Reverse is critical here.
		attr_names = get_header_info()
		attr_names.reverse()
		for info_item in info:
			self.__setattr__(attr_names.pop(), info_item)

		self.used = self.__translate_symbols_to_bin()
	

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
def get_terminal(info) -> Terminal:
	return Terminal(info)