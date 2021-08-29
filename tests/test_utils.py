passed = lambda x: "FAIL" if x else "PASS"
# Stars are there for loading arrays
check_str = lambda load, func, target: f"{load} -> {func(*load)} == {target} ? {passed(func(*load)==target)}"
def get_stacked_set(count=1) -> str:
	def get_set() -> str:
		return "23.22"
	if count < 1: return ""
	ret: str = ""
	for i in range(count):
		ret = f"{ret}{get_set()}" if i == count - 1 else f"{ret}{get_set()}-"
	return ret