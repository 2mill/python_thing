# The purpose of this program is to be able to map a patch panel based off the information from the CSV file earlier.
# A standard patch panel that I know of has 48 ports. Therefore, it will be an array of size 48 each containig a reference to the Terminal object that has the correct information

true_position = lambda position: position - 1
class PatchPanel:
	def __init__(self) -> None:
		self.ports: list = [None] * 48
	def add_patch(self, port: object, position: int, change=False) -> bool:
		# This is done, due to ports being marked 1 - 48 on patch panels
		# and arrays indexing from 0 - length - 1
		real_pos: int = true_position(position)

		if self.ports[real_pos] is not None and not change:
			return False
		else:
			self.ports[real_pos] = port
			return True
	def get_port_from_patch(self, position):
		real_postion: int = true_position(position)
		return self.ports[true_position]

	
def get_patch_panel():
	return PatchPanel()

