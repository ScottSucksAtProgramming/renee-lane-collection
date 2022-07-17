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
from brownie import ReneeLaneCollection, reverts, ZERO_ADDRESS
from web3 import Web3
import random
import pytest


# * ------------------------------- Variables ------------------------------ #

@pytest.fixture
def contract_setup_with_open_minting():
    """Setup for the contract. Whitelists the Zero address."""
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    contract.addToWhitelist(ZERO_ADDRESS)
    return contract
# * ---------------------------- tokenURI() Tests -------------------------- #
#! For other token related tests check renee_lane_mintArtwork_test.py
# Todo: Test _baseURI() reverts if token does not exist.


def test_tokenURI_reverts_for_nonexistent_tokenID(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    bad_token_ID = random.randint(0, 999999)
    # Act and Assert
    with reverts("ERC721Metadata: URI query for nonexistent token"):
        contract.tokenURI(bad_token_ID)


def test_tokenURI_returns_expected_string(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    # Act
    expected_string = f"https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/1.json"
    actual_string = contract.tokenURI(1)
    # # Assert
    assert actual_string == expected_string
