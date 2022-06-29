#
# * ------------------------------ Documentation ---------------------------- #
# Module:  12_renee_lane_Token_test.py
# This module contains all the unit tests for Tokens created by Renee Lane
# Collection smart contract.
#
#
# Modification History
# 06-29-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ Test token owner is set correctly.
# ✓ Test tokenID of minted token is set correctly.
# ✓ Test URI of minted token is set correctly.


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection
from web3 import Web3
# * ------------------------------- Variables ------------------------------ #


# # *  --------------------------- Token Tests ------------------------------- #
def test_token_owner_is_set_correctly():
    """Tests to see if the token is minted to the correct owner. Test will 
    pass if ownerOf Token is the same as the minter address."""
    # Arrange
    deployer_account = get_account()
    minter_account = get_account(3)
    _imageNumber = 1
    token_ID = 1
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    # Act
    contract.mintArtwork(
        _imageNumber,
        {"value": Web3.toWei(0.12, "ether"),
         "from": minter_account})
    # Assert
    owner_of_token = contract.ownerOf(token_ID)
    assert owner_of_token == minter_account


def test_tokenID_is_set_correctly():
    """Tests that minted tokens have the correct tokenID. Test will pass if 
    logged TokenId equals expectedTokenID"""
    # Arrange
    deployer_account = get_account()
    _imageNumber = 1
    price = Web3.toWei(0.12, "ether")
    expected_token_ID = 1
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    tx = contract.mintArtwork(
        _imageNumber, {"value": price, "from": deployer_account}
    )
    actual_token_ID = tx.events["Transfer"]["tokenId"]
    # Assert
    assert expected_token_ID == actual_token_ID


def test_token_URI_is_set_correctly():
    """Test to see if the token URI is set correctly. Test will pass if 
    expected URI equals actual URI."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    expected_URI = "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/121.json"
    # Act
    tx = contract.mintArtwork(
        7, {"value": Web3.toWei(0.12, "ether"), "from": deployer_account}
    )
    actual_URI = contract.tokenURI(121)
    # Assert
    assert expected_URI == actual_URI
