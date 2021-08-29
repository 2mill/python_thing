from tests import csv_process_tests
from tests import patch_panel_tests
import random
header = lambda head: f"----{head}----"
print(header("CSV_PROCESSOR"))
print(csv_process_tests.test_patchinfo_translation_single())
print(csv_process_tests.test_patchinfo_translation_double())
print(csv_process_tests.test_conversions())
print(header("PATCH PANEL"))
print(patch_panel_tests.add_port_without_change())
