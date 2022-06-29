#
# * ------------------------------ Documentation --------------------------- #
# Module:  renee_lane_collection_token_test.py
# This module contains all the unit tests for tokens created by The Renee Lane
# collection.
#
#
# Modification History
# 06-17-22 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection

# * ------------------------------- Variables ------------------------------ #


# * ------------------------ supportsInterface() Tests -------------------- #
# Todo: Test supportsInterface() returns true for ERC721.
def test_supportsInterface_returns_true_for_ERC721():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act
    erc721_interface = 0x80AC58CD
    returned_input = reneeLaneCollection.supportsInterface(erc721_interface)
    # Assert
    assert returned_input == True


# Todo: Test supportsInterface() returns true for ERC165.
def test_supportsInterface_returns_true_for_ERC165():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act
    erc721_interface = 0x01FFC9A7
    returned_input = reneeLaneCollection.supportsInterface(erc721_interface)
    # Assert
    assert returned_input == True


# Todo: Test supportsInterface() returns false for unsupported inputs.
def test_supportsInterface_returns_false_for_unsupported_inputs():
    # Arrange
    import os
    import binascii

    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act
    random_input = binascii.b2a_hex(os.urandom(2))
    returned_input = reneeLaneCollection.supportsInterface(random_input)
    print(f"\nAttempting to verify {random_input}.")
    print("Expected value: False.")
    print(f"Returned value: {returned_input}")
    # Assert
    assert returned_input == False
