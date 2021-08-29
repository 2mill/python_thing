def get_stacked_set(count=1) -> str:
	def get_set() -> str:
		return "23.22"
	if count < 1: return ""
	ret: str = ""
	for i in range(count):
		ret = f"{ret}{get_set()}" if i == count - 1 else f"{ret}{get_set()}-"
	return ret