
class Port:
	def __init__(self, number: int, port_connection: str):
		self.number = number
		self.port_connection = port_connection

	def __str__(self) -> str:
		return f"{self.number}:{self.port_connection}"

class PatchPanel:
	def __init__(self, building: str, room: str, pp_number: int):
		self.building = building
		self.room = room
		self.pp_number = pp_number

		# 48 ports per patch
		ports: List[Port] = []
		for port_number in range(49):
			ports.append(Port(port_number, None))

		self.ports = ports

	def __str__(self) -> str:
		portss: str = "";
		for port in self.ports:
			portss = f"{portss}\t{port}\n"
		return f"{self.building}:{self.room}:PP{self.pp_number}\n{portss}"


