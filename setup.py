from setuptools import setup, find_packages

setup(
    name = "minecraft-autoupdater",            # The name of your package
    version = "0.1.0",                     # Package version
    description = "Used for updating neoforge & curseforge mods",   # Short summary of the package
    long_description = open("README.md").read(),  # Detailed description, often from README
    long_description_content_type = "text/markdown",  # Format of the long description
    author = "Dylan Cullinane",                  # Your name
    author_email = "dylanjcullinane@icloud.com",  # Your email
    url = "https://github.com/dcullina/minecraft-autoupdater",  # Project's homepage or repo
    packages = find_packages("src"),            # Automatically find all packages in the project
	package_dir = {"": "src"},
	entry_points = {
		"console_scripts": [
			"autoupdate_minecraft=mc_autoupdater.auto_update:main"
		]
	}
)