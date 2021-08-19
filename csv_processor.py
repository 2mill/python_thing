import csv
from typing import Union

def is_header(line: list) -> bool:
	for item in line:
		if item == "Room Number": return True
	return False


def get_header_info() -> list:
	return ["room", "box_label", "port_count", "used", "patch_panel", "patch_port", "parent_room", "comment"]
def process(loaded_csv: list):
	processes_list: list = []
	for item in loaded_csv:
		header_info: list = get_header_info()
		header_info.reverse()
		new_line: list = []
		for el in item:
			el_info = header_info().pop()
			if el_info == "used":
				new_line.append(translate_symbols_to_bin(el))
			elif el_info == "patch_port":
				new_line.append(el.split('.'))
			else:
				new_line.append(el)
		processes_list.append(new_line)
def translate_used_symbols(symbol: str) -> int:
	return 1 if symbol == 'X' else 0
# Returns header information for setting attributes
# function for converting from my markings into a designation
def translate_symbols_to_bin(self) -> Union[int, bool]:
	port_usage = self.used
	if port_usage == "undefined": return False
	temp: list[str] = port_usage.split(' ')
	temp.reverse()
	total: int = 0;
	for x in range(len(temp)):
		total = total + (2**x)*(translate_used_symbols(temp[x]))
	return total