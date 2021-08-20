import csv_processor

def test_conversions() -> bool :
	result_bool = False
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '47.48', '169', '',],]
	result = csv_processor.process(test_csv_file)
	result_bool = result == [['169G', '169G-1', '2', 0, '12', ['47', '48'], '169', '']] 
	test_csv_file: list = [['169G', '169G-1', '2', '/ /', '12', '8.9 - 17.18', '148', '']]
	result_bool = csv_processor.process(test_csv_file) == [['169G', '169G-1', '2', 0, '12', [['8', '9'], ['17', '18']], '148', '']]
	return result_bool
