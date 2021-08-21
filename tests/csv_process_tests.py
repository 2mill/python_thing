import csv_processor
import random


passed = lambda x: "FAIL" if x else "PASS"

def test_conversions() -> bool :
	result_bool = False
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '47.48', '169', '',],]
	result = csv_processor.process(test_csv_file)
	result_bool = result == [['169G', '169G-1', '2', 0, '12', ['47', '48'], '169', '']] 
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '8.9 - 17.18', '148', '']]
	result_bool = csv_processor.process(test_csv_file) == [['169G', '169G-1', '2', 0, '12', [['8', '9'], ['17', '18']], '148', '']]
	return result_bool


def get_random_set() -> str:
	return f"{random.randrange(1,48)}.{random.randrange(1,48)}"

# Returns the string attempt
def random_list_and_formatted(size: int) -> str:
	other_temp: str = ""
	for i in range(size):
		number = random.randrange(1,49)
		# BAD CODE GOES BRRT
		other_temp = f"{number}" if len(other_temp) == 0 else f"{other_temp}.{number}"

	return other_temp
	

def test_patchinfo_translation_single(size) -> None:
	tester: str = random_list_and_formatted(4) 

	# TODO: REBUILD THIS PART TO TAKE THE OUTPUT
	# FROM THE PREVIOUS FUNCTION AND FORMAT IT SO THAT TRIES TO MATCH	
	pass


	# Model
	# "12.13" -> ["12", "13"]
	# "12.13 - 12.13" -> [["12", "13"], ["12, 13"]]


def test_patchinfo_translation_double() -> bool:
	pass
