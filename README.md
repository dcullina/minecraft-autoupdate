# Autoupdater for NeoForge and Mods from CurseForge

## NeoForge

1. Check installed NeoForge version
   - If not installed, this currently breaks
   - If installed, check the NeoForge version
   - Compare it with the latest version online for a specified minecraft release (e.g., `1.21.1`)
   - Prompt user to install latest version if out of date

## Mods

1. Check installed mods
	- Check if current `minecraft_path/mods/` directory exists
	  - if not, create it
	- Get list of mods in `minecraft_path/mods/` directory
	- Parse list of mods for anything that appears like a "version" number (separated by ".")
	- remove any versions matching `1.21*`