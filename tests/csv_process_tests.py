import csv_processor
import random


passed = lambda x: "FAIL" if x else "PASS"
check_str = lambda load, result, target: f"{load} -> {result} == {target} ? {passed(result==target)}"

def test_conversions() -> bool :
	result_bool = False
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '47.48', '169', '',],]
	result = csv_processor.process(test_csv_file)
	result_bool = result == [['169G', '169G-1', '2', 0, '12', ['47', '48'], '169', '']] 
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '8.9 - 17.18', '148', '']]
	result_bool = csv_processor.process(test_csv_file) == [['169G', '169G-1', '2', 0, '12', [['8', '9'], ['17', '18']], '148', '']]
	return result_bool


	

def get_stacked_set(count=1) -> str:
	def get_set() -> str:
		return "23.22"
	if count < 1: return ""
	ret: str = ""
	for i in range(count):
		ret = f"{ret}{get_set()}" if i == count - 1 else f"{ret}{get_set()}-"
	return ret


def test_patchinfo_translation_single() -> str:
	load = get_stacked_set()
	return check_str(
		load,
		csv_processor.translate_patch_ports(load),
		target = [23,22]
	)
def test_patchinfo_translation_double() -> str:
	load = get_stacked_set(count=2)
	return check_str(
		load,
		csv_processor.translate_patch_ports(load),
		target = [[23, 22], [23,22]]
	)




	# Model
	# "12.13" -> ["12", "13"]
	# "12.13 - 12.13" -> [["12", "13"], ["12, 13"]]


