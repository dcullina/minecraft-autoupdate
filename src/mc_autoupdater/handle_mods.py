import json
import os
from rich import print
from .sessions import new_session

def get_installed_mods(minecraft_path: str) -> list[str]:
	mods_path = f"{minecraft_path}/mods"
	if os.path.exists(mods_path):
		print("found mods folder!")
		return os.listdir(mods_path)
	else:
		os.mkdir(mods_path)
		return []

def get_latest_mod_versions(mods: dict) -> str:
	session = new_session()
	for mod in mods["mods"]:
		url = f"https://www.curseforge.com/api/v1/mods/{mod["projectId"]}/files?pageIndex=0&pageSize=1&sort=dateCreated&sortDescending=true&gameVersionId={mods["gameVersionId"]}&gameFlavorId={mods["gameFlavorId"]}&removeAlphas=false"
		resp = session.get(url)
		resp.raise_for_status()
		mod_id = resp.json()["data"][0]["id"]
		print(f"{mod["modName"]}: {mod_id}")

def query_mod(mod: dict):
	pass

def download_latest_mod_version() -> None:
	pass

def autoupdate_mods(minecraft_path: str, mods_file_path: str) -> None:

	# Instaling NeoForge
	# main_version = 21
	# sub_version = 1

	with open(mods_file_path) as file:
		mods = json.load(file)

	get_latest_mod_versions(mods)
	get_installed_mods(minecraft_path)