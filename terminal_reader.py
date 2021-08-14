# Meant to process the CSV file information.
import sys, argparse, csv
from typing import Union

parser = argparse.ArgumentParser(description="A data processor for a Terminal list")


# Supposed to store the parentroom number
# And an actual reference to the Terminal object
# TODO: Make a function for adding new terminal
# I don;t think I need to add a compare for terminals, because
# The CSV files should not have any more information
class ParentRoom:
	def __init__(self, number:str)->None:
		self.terminals: list = []
		self.number:str = number
	def __eq__(self, oparent_room:object) -> bool:
		return self.number == oparent_room.number
		
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
	def add_parent_room(self, parent_room:ParentRoom)->bool:
		if self.contains(parent_room): return False
		self.parent_rooms.append(parent_room)
		return True
	def contains(self, parent_room:ParentRoom)-> bool:
		for room in self.parent_rooms:
			if parent_room.__eq__(room): return True
		return False



def translate_used_symbols(symbol: str) -> int:
	return 1 if symbol == 'X' else 0

# function for converting from my markings into a designation
def translate_symbols_to_bin(port_usage: str) -> Union[int, bool]:
	if port_usage == "undefined": return False
	temp: list[str] = port_usage.split(' ')
	temp.reverse()
	total: int = 0;
	for x in range(len(temp)):
		total = total + (2**x)*(translate_used_symbols(temp[x]))
	return total

	##This should return the sequence


class Terminal:
	def __init__(self, info) -> None:
		self.room, self.box_label, self.port_count, self.port_count, self.used, self.patch_port, self.parent_room, self.comment = info

		self.used = translate_symbols_to_bin(self.used)

	def __str__(self) -> str:
		return f"\t\n{self.room}\t\n{self.box_label}\t\n{self.port_count}\t\n{self.used}\t\n{self.patch_port}\t\n{self.comment}"
	def get_parent_room(self) -> str:
		return self.parent_room
def create_list(filename:str) -> list:
	# DO NOT REMOVE THIS UTF ENCODING
	with open(f"./{filename}", encoding="utf-8-sig") as f:
		reader = csv.reader(f)
		terminal_list: list = []
		for row in reader:
			if is_header(row): continue
			terminal_list.append(Terminal(row))
		return terminal_list

		


def string_terminal_list(terminal_list: list) -> str:
	def myFunc(term: Terminal) -> int:
		return term.parent_room
	terminal_list.sort(key=myFunc)
	# List should be sorted at this point.
	# Collect until room changes.

	builder:str = "";
	for terminals in terminal_list:
		builder






temp: list = create_list(sys.argv[1])

string_terminal_list(temp)
# string_terminal_list(temp)
