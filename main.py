import platform
import os
from handle_neoforge import autoupdate_neoforge

def get_minecraft_path() -> str:
	current_platform = platform.system()

	if current_platform == "Darwin":
		minecraft_path = os.path.expanduser("~/Library/Application Support/minecraft")
	elif current_platform == "Windows":
		minecraft_path = os.path.join(os.getenv("APPDATA"), ".minecraft")
	else:
		raise Exception("Unsupported platform") # im not bothering to implement for linux

	return minecraft_path


if __name__ == "__main__":

	minecraft_path = get_minecraft_path()
	autoupdate_neoforge(minecraft_path)
	# autoupdate_mods(minecraft_path)

	# Installing mods
	# while True:
	# 	print("\n")
	# 	decision = str(input("Do you wish to install latest versions of mods? ( y / n ): ")).lower()
	# 	if decision == "y":
	# 		print("received yes")
	# 		upgrade_mods(installed_mods)
	# 		break
	# 	elif decision == "n":
	# 		print("received no")
	# 		break
	# 	else:
	# 		print("Unknown input...")


	# session = new_session()
	# version_api(session, main_version, sub_version)