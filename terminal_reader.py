# Meant to process the CSV file information.
import sys, argparse

parser = argparse.ArgumentParser(description="A data processor for a Terminal list")

csv_file = 


def XandSlashEnum(symbol: str) -> int:
	return 1 if symbol is 'X' else 0

# function for converting from my markings into a designation
def translate(port_usage: str) -> int:
	temp: list[str] = port_usage.split(' ')
	sum: int = 0;
	for x in range(len(temp)):
		sum = sum + (2**x)*(XandSlashEnum(temp[x]))
	return sum

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
		self.used = translate(used)
		self.patch_port = patch_port
		self.parent_room = parent_room
		self.comment = comment
def create_list(filename:str) -> list[Terminal]:
	file = open(filename, "r")
	file = file.readlines()