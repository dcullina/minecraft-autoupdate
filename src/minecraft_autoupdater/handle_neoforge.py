import json
import os
import requests
from rich import print
import semver
from .sessions import new_session
import subprocess


def get_current_nf_version(minecraft_path: str) -> str:
    if os.path.exists(minecraft_path):
        with open(minecraft_path + "/launcher_profiles.json") as file:
            data = json.load(file)["profiles"]
    else:
        raise Exception("minecraft install dir not found")

    if "NeoForge" in data:
        return data["NeoForge"]["lastVersionId"].rsplit("-", 1)[-1]
    else:
        return ""


def get_latest_version(main_version: int, sub_version: int) -> str:
    session = new_session()
    url = (
        "https://maven.neoforged.net/api/maven/versions/releases/net/neoforged/neoforge"
    )
    resp = session.get(url)
    resp.raise_for_status()
    versions = resp.json()["versions"]
    filtered_versions = [
        version
        for version in versions
        if version.startswith(f"{main_version}.{sub_version}")
    ]
    latest_version = filtered_versions[-1]

    return latest_version


def upgrade_neoforge(version: str) -> None:
    print(f"Upgrading NeoForge to {version}")
    url = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{version}/neoforge-{version}-installer.jar"
    file_name = url.rsplit("/", 1)[-1]
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        try:
            result = subprocess.run(
                ["java", "-jar", file_name, "--installClient"], check=True
            )
            print(f"Result: {result}")
            print(f"\nInstalled NeoForge {version} successfully!\n")
            os.remove(file_name)
            os.remove(f"{file_name}.log")
            print("\nInstallation files have been cleaned up successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error executing jar file: {e}")
    else:
        print(f"Failed to download NeoForge installer: {response.status_code}")


def autoupdate_neoforge(minecraft_path: str) -> None:
    # Instaling NeoForge
    main_version = 21
    sub_version = 1

    installed_nf_version = get_current_nf_version(minecraft_path)
    # installed_nf_version = "21.1.80"
    latest_nf_version = get_latest_version(main_version, sub_version)
    print(f"{"Installed NeoForge version:":<30}{installed_nf_version:>10}")
    print(f"{"Latest NeoForge version:":<30}{latest_nf_version:>10}")
    result = semver.compare(installed_nf_version, latest_nf_version)
    if result >= 0:
        print("Not upgrading Neoforge...")
        return
    else:
        print("installed version out of date...")

    while True:
        print("\n")
        decision = str(input("Do you wish to upgrade Neoforge? ( y / n ): ")).lower()
        if decision == "y":
            print("received yes")
            upgrade_neoforge(latest_nf_version)
            break
        elif decision == "n":
            print("received no")
            break
        else:
            print("Unknown input...")
