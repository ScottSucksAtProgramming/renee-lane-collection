# ------------------------------ Documentation ------------------------------ #
# Module:  metadata_builder_test.py
# The metadata_builder_test.py script contains the unit tests for the
# metadata_builder.py script and the metadata_template.py script.
#
#
# Modification History
# 07-02-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ! Test can return correct IPFS address for image.
# ! Generates the metadata for the beta test collection.

# ! The goal for this builder is to generate the metadata for the beta test,
# ! using the metadata_template.py script. It should create a new .json file
# ! for each image in the collection.
# ------------------------------- Resources -------------------------------- #
from tracemalloc import start
from scripts import metadata_builder as mb
from pathlib import Path
import warnings
import os
# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #

# ----------------------------- Tests ------------------------------ #


def test_can_format_int_to_token_id():
    # Arrange
    number = 7
    expected_token_id = "07"
    # Act
    token_id = mb.format_number_as_string(number)
    # Assert
    print(f"token_id: {token_id}")
    assert token_id == expected_token_id


def test_can_create_metadata_file_name():
    # Arrange
    token_id = 50
    expected_metadata_file_name = f"{token_id}.json"
    # Act
    metadata_file_name = mb.create_metadata_file_name(token_id)
    # Assert
    print(f"metadata_file_name: {expected_metadata_file_name}")
    assert metadata_file_name == expected_metadata_file_name


def test_can_return_correct_ipfs_address_for_image():
    # Arrange
    expected_imageURI = "https://ipfs.io/ipfs/QmXnPu4nJi3c86BZnmigSy7W1QpnYkuv5BGjTYw871G3vM/01.jpeg"
    # Act
    image_URI = mb.return_ipfs_address_for_image(1)
    # Assert
    print(f"image_URI: {image_URI}")
    assert image_URI == expected_imageURI


def test_can_create_json_files():
    # Arrange
    image_number = 900
    starting_token_id = 900
    number_of_editions = 20
    # Act
    mb.write_metadata_files(
        image_number, starting_token_id, number_of_editions)
    # Assert
    assert Path(
        f"./metadata/{mb.format_number_as_string((starting_token_id + number_of_editions)-1)}.json").exists()


def test_can_return_user_inputs():
    # Arrange
    # Act
    # Assert
    assert mb.metadata_info["medium"] == "Oil on canvas"

# def test_write_image_to_metadata_file():
#     # Arrange
#     image_number = 5
#     expected_imageURI = "https://ipfs.io/ipfs/QmXnPu4nJi3c86BZnmigSy7W1QpnYkuv5BGjTYw871G3vM/05.jpeg"
#     # Act
#     # Assert
#     assert mb.write_metadata_files(image_number)
