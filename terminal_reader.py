# Meant to process the CSV file information.
# TODO: Make terminal_reader the command handler, and allow for structs and other things to do the work.
import sys, argparse, csv
from typing import Union
from structs import terminal, parentrooms
import csv_processor

def generate_parent_room_list(terminal_list: list) -> object:
	return parentrooms.generate_parent_room_list(terminal_list)


parser = argparse.ArgumentParser(description="A data processor for a Terminal list")


# Supposed to store the parentroom number
# And an actual reference to the Terminal object
# I don;t think I need to add a compare for terminals, because
# The CSV files should not have any more information
	
# ParentRooms data information:
# supposed to store a list of all the parent rooms.
# I think I can refactor this into a couple of functions instead of a whole class.





	##This should return the sequence







def string_terminal_list(terminal_list: list) -> str:
	def myFunc(term: object) -> int:
		return term.parent_room
	terminal_list.sort(key=myFunc)
	# List should be sorted at this point.
	# Collect until room changes.

	builder:str = "";
	for terminals in terminal_list:
		builder






create_list(sys.argv[1])