#
# * ------------------------------ Documentation ---------------------------- #
# Module:  metadata_builder.py
#
# The metadata_builder.py script is used to build the metadata for the the art
# collection. It uses the metadata_template in the metadata folder to build
# the metadata for each art piece.
#
#
# Modification History
# 07-02-2022 | SRK | Module created.
# 07-02-2022 | SRK | Copied old code.

# * -------------------------------- Tasks --------------------------------- #
# Todo: Update metadata_template to include all the metadata fields.
# Todo: Copy code from old metadata builder script.
# Todo: Update code to use the metadata_template.
# Todo: Complete unit testing prior to generating the metadata.
# Todo: Generate and deploy the metadata for the beta test collection.

# * ------------------------------- Resources ------------------------------ #
from curses import meta
from metadata.metadata_template import metadata_template
from pathlib import Path
# import requests
import json
import os

# * ------------------------------ Variables ------------------------------- #
DEMO_ASSET_IPFS_ADDRESS = "https://ipfs.io/ipfs/QmXnPu4nJi3c86BZnmigSy7W1QpnYkuv5BGjTYw871G3vM/"
IPFS_address = None
image_number: int = None
name: str = None
description: str = None
external_url: str = None
artist: str = None
medium: str = None
photo_source: str = None
title: str = None
edition: int = None
max_edition: int = None
royalty_address = "0x0000000000000000000000000000000000000000"
metadata_info = {}
# * ------------------------------ Functions ------------------------------- #


def create_metadata_file(image_number: int, collectible_metadata: dict = None):
    formatted_image_number = format_number_as_string(image_number)
    metadata_file_name = (
        f"./metadata/{format_number_as_string}.json"
    )
    """Creates the metadata files for the art collection.
    """
    if Path(metadata_file_name).exists():
        print(f"{metadata_file_name} already exists! Delete it to overwrite.")
    else:
        with open(metadata_file_name, "w") as f:
            json.dump(collectible_metadata, f)
        print(f"Creating metadata file: {metadata_file_name}.")


def format_number_as_string(number: int) -> str:
    """Converts an integer to a token_id string.

    Args:
        number (int): The number to convert.

    Returns:
        number_string (str): The number as a string.
    """
    number = str(number)
    if len(number) < 2:
        number = "0" + number
    token_id = str(number)
    return token_id


def create_metadata_file_name(token_id: int) -> str:
    """Creates the metadata file name for the token.

    Args:
        token_id (int): The token ID.

    Returns:
        metadata_file_name (str): The metadata file name.
    """
    token_id = format_number_as_string(token_id)
    metadata_file_name = f"{token_id}.json"
    return metadata_file_name


def return_ipfs_address_for_image(image_number: int) -> str:
    """Returns the IPFS address for the image as a string.

    Args:
       image_number (str): The number of the image.

    Returns:
        image_URI (str): The IPFS address for the image.
    """
    image_number = format_number_as_string(image_number)
    image_URI = f"{DEMO_ASSET_IPFS_ADDRESS}{image_number}.jpeg"
    return image_URI


def write_metadata_files(image_number: int, starting_token_id: int, number_of_editions: int):
    collectible_metadata = metadata_template
    for edition in range(number_of_editions):
        metadata_template["image"] = IPFS_address
        metadata_template["name"] = f"Art Piece Fifty #{edition+1} of #{number_of_editions}"
        metadata_template["description"] = "Last One"
        metadata_template["external_url"] = "https://gynarchy.io/"
        metadata_template["image"] = return_ipfs_address_for_image(
            image_number)
        metadata_template["attributes"][0]["value"] = "Artist 5"
        metadata_template["attributes"][1]["value"] = "Digital Art"
        metadata_template["attributes"][2]["value"] = "I stole it from google."
        metadata_template["attributes"][3]["value"] = "Art Piece Fifty"
        metadata_template["attributes"][4]["value"] = edition + 1
        metadata_template["attributes"][4]["max_value"] = number_of_editions
        metadata_template["Royalty Percentage"] = "10%"
        metadata_template["Royalty Address"] = "0x68a53E615Ea6B30cd27Ae15c6A8D972eE1ff7867"
        metadata_file_name = (
            f"./metadata/{create_metadata_file_name(starting_token_id + edition)}")
        with open(metadata_file_name, "w") as f:
            json.dump(collectible_metadata, f)
# # * ---------------------------- Main Function ----------------------------- #


def main():
    write_metadata_files(50, 578, 3)

# def main():

#     metadata_file_name = (
#         f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
#     )
#     collectible_metadata = metadata_template
#     if Path(metadata_file_name).exists():
#         print(f"{metadata_file_name} already exists! Delete it to overwrite.")
#     else:
#         print(f"Creating metadata file: {metadata_file_name}.")
#         collectible_metadata["name"] = breed
#         collectible_metadata[
#             "description"
#         ] = f"An adorable {breed} doggo who loves you!"
#         image_path = "img/" + breed.lower().replace("_", "-") + ".png"
#         image_uri = None
#         if os.getenv("UPLOAD_IPFS") == "true":
#             image_uri = upload_to_pinata(image_path)
#         image_uri = image_uri if image_uri else breed_to_image_uri[breed]
#         collectible_metadata["image"] = image_uri
#         with open(metadata_file_name, "w") as file:
#             json.dump(collectible_metadata, file)
#         if os.getenv("UPLOAD_IPFS") == "true":
#             upload_to_pinata(metadata_file_name)


# Use this function if you want to upload to your own IPFS node.
# def upload_to_ipfs(filepath):
#    with Path(filepath).open("rb") as fp:
#        image_binary = fp.read()
#        ipfs_url = "http://127.0.0.1:5001"
#        endpoint = "/api/v0/add"
#        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
#        ipfs_hash = response.json()["IpfsHash"]
#        filename = filepath.split("/")[-1:][0]
#        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
#        print(image_uri)
#        return image_uri

# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #

# ----------------------------- Main Function ------------------------------ #
