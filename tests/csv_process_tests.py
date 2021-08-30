import csv_processor
import random
from .test_utils import get_stacked_set


passed = lambda x: "FAIL" if x else "PASS"
check_str = lambda load, func, target: f"{load} -> {func(load)} == {target} ? {passed(func(load)==target)}"

def test_conversions() -> bool :
	return check_str(
		load = [['169G', '169G-1', '2', '/ /', '12', '47.48', '169', '',]],
		func = csv_processor.generate_patch_panel,
		target = [['169G', '169G-1', '2', 0, '12', [47, 48], '169', '']] 
	)


	

def get_stacked_set(count=1) -> str:
	def get_set() -> str:
		return "23.22"
	if count < 1: return ""
	ret: str = ""
	for i in range(count):
		ret = f"{ret}{get_set()}" if i == count - 1 else f"{ret}{get_set()}-"
	return ret


def test_patchinfo_translation_single() -> str:
	return check_str(
		load = get_stacked_set(),
		func = csv_processor.translate_patch_ports,
		target = [23,22]
	)
def test_patchinfo_translation_double() -> str:
	return check_str(
		load = get_stacked_set(count=2),
		func = csv_processor.translate_patch_ports,
		target = [[23, 22], [23,22]]
	)




	# Model
	# "12.13" -> ["12", "13"]
	# "12.13 - 12.13" -> [["12", "13"], ["12, 13"]]


