# Meant to process the CSV file information.
# TODO: Make terminal_reader the command handler, and allow for structs and other things to do the work.
import sys, argparse, csv
from typing import Union

parser = argparse.ArgumentParser(description="A data processor for a Terminal list")


# Supposed to store the parentroom number
# And an actual reference to the Terminal object
# TODO: ~~Make a function for adding new terminal~~: Complete
# I don;t think I need to add a compare for terminals, because
# The CSV files should not have any more information
class ParentRoom:
	def __init__(self, number:str)->None:
		self.terminals: list = []
		self.number:str = number
	def __eq__(self, oparent_room:object) -> bool:
		return self.number == oparent_room.number
	def add(self, terminal: object) -> bool:
		for term in self.terminals:
			if term == terminal: return False
		self.terminals.append(terminal)	
		return True
	def contains(self, oterminal: object) -> bool:
		for terminal in self.terminals:
			if oterminal == terminal: return True
		return False
	def __str__(self)-> str:
		output = f"--{self.number}--"
		for terminal in self.terminals:
			output = f"{output}{terminal}\n"
		return output + "\n"
def is_header(csv_line: list) -> bool:
	for index in csv_line:
		if index == "Room Number": return True
		else: return False

# ParentRooms data information:
# supposed to store a list of all the parent rooms.
# I think I can refactor this into a couple of functions instead of a whole class.
class ParentRooms:
	def __init__(self)->None:
		self.parent_rooms:list=[]
	# This function should if not present make a new parent room if one does not exist
	# Add a terminal to a parent room 
	# If the room exists, add the terminal to the room.
	def add(self, terminal: object) -> bool:
		parent_room: str = terminal.parent_room
		for room in self.parent_rooms:
			if room.number == parent_room:
				return room.add(terminal)
		new_parent_room = ParentRoom(parent_room)
		new_parent_room.add(terminal)
		self.parent_rooms.append(new_parent_room)
		return True
	# TODO: check and verify formatting
	def __str__(self) -> str:
		output = ""
		for room in self.parent_rooms:
			output = f"{output}{room}"
		return output



def translate_used_symbols(symbol: str) -> int:
	return 1 if symbol == 'X' else 0

# function for converting from my markings into a designation
# FIXME: This ain't working right now for some reason.
def translate_symbols_to_bin(port_usage: str) -> Union[int, bool]:
	if port_usage == "undefined": return False
	temp: list[str] = port_usage.split(' ')
	temp.reverse()
	total: int = 0;
	for x in range(len(temp)):
		total = total + (2**x)*(translate_used_symbols(temp[x]))
	return total

	##This should return the sequence



# TODO: Refactor constructor to be more efficient
# TODO: Move structs into seperate file
class Terminal:
	def __init__(self, info) -> None:
		self.room, self.box_label, self.port_count, self.port_count, self.used, self.patch_port, self.parent_room, self.comment = info

		# TODO reimplement when done
		# self.used = translate_symbols_to_bin(self.used)

		self.used = translate_symbols_to_bin(self.used)

	def __str__(self) -> str:
		output = ""
		for item in self.__dict__:
			if item == "parent_room": continue
			if item == "room":
				output = f"{output}\n{item.capitalize()}:{self.__getattribute__(item)}"
			else:
				output = f"{output}\n-{item}:{self.__getattribute__(item)}"
		return output
			# print("---dict shit--")
			# print(self.__getattribute__(item))
		# return f"\t\n{self.room}\t\n{self.box_label}\t\n{self.port_count}\t\n{self.used}\t\n{self.patch_port}{self.comment}"
	#TODO: figure out __dict__ efficiently
	def __eq__(self, oterminal: object) -> bool:
		print(self.__dict__)
		
	def get_parent_room(self) -> str:
		return self.parent_room
	def __eq__(self, oterminal: object) -> bool:
		return self.room == oterminal.room and self.box_label == oterminal.box_label

def create_list(filename:str) -> list:
	# REQ utf-8-sig
	with open(f"./{filename}", encoding="utf-8-sig") as f:
		reader = csv.reader(f)
		terminal_list: list = []
		for row in reader:
			if is_header(row): continue
			terminal_list.append(Terminal(row))
		return terminal_list

def parent_room_list(terminal_list: list) -> ParentRooms:
	parent_rooms: ParentRooms = ParentRooms()
	for terminal in terminal_list:
		parent_rooms.add(terminal)
	print(parent_rooms)



# TODO make this somehow different
def string_terminal_list(terminal_list: list) -> str:
	def myFunc(term: Terminal) -> int:
		return term.parent_room
	terminal_list.sort(key=myFunc)
	# List should be sorted at this point.
	# Collect until room changes.

	builder:str = "";
	for terminals in terminal_list:
		builder





parent_room_list(create_list(sys.argv[1]))