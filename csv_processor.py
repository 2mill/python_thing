import csv
from typing import Union

# Checks if the header matches or not,
# Planning on making this more dynamic w/ a CSV file.
matches_header = lambda source: source== [
	"room",
	"box_label",
	"port_count",
	"used",
	"patch_panel",
	"patch_port",
	"parent_room",
	"comment"
]



def generate_patch_panel(loaded_csv: list):
	# Remove the header information.
	# Parse for patch panel information.
	# Generate new patch panels as needed. Requires Patchpanel list
	processes_list: list = []
	for item in loaded_csv:
def translate_used_symbols(symbol: str) -> int:
	return 1 if symbol == 'X' else 0
# Returns header information for setting attributes
# function for converting from my markings into a designation
def translate_symbols_to_bin(port_usage) -> Union[int, bool]:
	if port_usage == "undefined": return False
	temp: list[str] = port_usage.split(' ')
	temp.reverse()
	total: int = 0;
	for x in range(len(temp)):
		total = total + (2**x)*(translate_used_symbols(temp[x]))
	return total

def translate_patch_ports(panel_info: str)-> list:
	panel_info.replace(" ", "")
	first: list = panel_info.split("-")
	output: list = []
	for item in first:
		output.append(item.split("."))

	# If a split occurs because of a -, then there are more than one
	# however, if there is no - in the split, then we just need to pop
	# the first value.
	return output if len(output) > 1 else output.pop()
