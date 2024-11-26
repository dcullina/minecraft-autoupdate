import argparse
from .handle_neoforge import autoupdate_neoforge
from .handle_mods import autoupdate_mods
import os
import platform


def get_minecraft_path() -> str:
	current_platform = platform.system()

	if current_platform == "Darwin":
		minecraft_path = os.path.expanduser("~/Library/Application Support/minecraft")
	elif current_platform == "Windows":
		minecraft_path = os.path.join(os.getenv("APPDATA"), ".minecraft")
	else:
		raise Exception(
			"Unsupported platform"
		)  # im not bothering to implement for linux

	return minecraft_path


def main() -> int:
	parser = argparse.ArgumentParser(description="blah blah blah test")
	parser.add_argument(
		"--mods-file", required=True, type=str, help="Path to the mods JSON file"
	)
	args = parser.parse_args()

	minecraft_version = "1.21.1"
	minecraft_path = get_minecraft_path()

	autoupdate_neoforge(minecraft_path)
	autoupdate_mods(minecraft_path, args.mods_file)
	return 0