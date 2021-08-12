# Meant to process the CSV file information.
import sys, argparse, csv
from typing import Union

parser = argparse.ArgumentParser(description="A data processor for a Terminal list")

# csv_file = 


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
	def __init__(
		self,
		room: str, 
		box_label: str,
		port_count: int,
		used:str,
		patch_port: str,
		parent_room: str,
		comment: str,
		) -> None:
		self.room = room
		self.box_label = box_label
		self.port_count = port_count
		self.used = translate_symbols_to_bin(used)
		self.patch_port = patch_port
		self.parent_room = parent_room
		self.comment = comment

	def __str__(self) -> str:
		return f"\t\n{self.room}\t\n{self.box_label}\t\n{self.port_count}\t\n{self.used}\t\n{self.patch_port}\t\n{self.comment}"
	def get_parent_room(self) -> str:
		return self.parent_room
def create_list(filename:str) -> list:
	file = open(filename, "r")
	# Remove header information
	file.readline()
	file = file.readlines()
	terminal_list: list = []
	for line in file:
		info: list = line.split(',')
		#Remove trailing whitespace
		info.pop()
		print(info)
		terminal_list.append(Terminal(*info))
	return terminal_list

def string_terminal_list(terminal_list: list) -> str:
	builder: str = ""
	for terminal in terminal_list:
		parent_room: str = terminal.parent_room 
		print(f"{parent_room}, {terminal.comment}")


temp: list = create_list(sys.argv[1])
# string_terminal_list(temp)
