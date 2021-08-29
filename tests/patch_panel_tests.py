import patch_panel
from .test_utils import passed, check_str




## This is just a model and not what it will actually look like.
def add_port_without_change():
	panel = patch_panel.get_patch_panel()
	panel.add_patch("FIRST PORT", 1)
	return check_str(
		["SECOND PORT", 1],
		panel.add_patch,
		"False"
	)
def add_port_with_change():
	panel = patch_panel.get_patch_panel()
	panel.add_patch("FIRST PORT", 1)
	return check_str(
		["SECOND PORT", 1, True],
		panel.add_patch,
		"True"
	)
