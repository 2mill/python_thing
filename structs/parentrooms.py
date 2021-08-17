
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

def is_header(line: list) -> bool:
	for item in line:
		if item == "Room Number": return True
	return False
	
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
def parent_room_list(terminal_list: list) -> ParentRooms:
	parent_rooms: ParentRooms = ParentRooms()
	for terminal in terminal_list:
		parent_rooms.add(terminal)
	return parent_rooms