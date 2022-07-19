#
# * ------------------------------ Documentation ---------------------------- #
# Module:  13_renee_lane_setTokenRoyalty_test.py
# This module contains all the unit tests for _setTokenRoyalty() function in
# The Renee Lane Collection smart contract.
#
#
# Modification History
# 06-29-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ Test RoyaltyAddress of minted token is set correctly.
# ✓ Test RoyaltyAmount of minted token is set correctly.


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection, ZERO_ADDRESS
from web3 import Web3
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
#*  --------------------- _setTokenRoyalty() Tests -------------------------- #


def test_token_royalty_address_is_set_correctly(contract_setup_with_open_minting):
    """Tests to see if the token royalty address is set correctly for minted 
    tokens. Test will pass if expected royalty address equals actual royalty 
    address."""
    # Arrange
    deployer_account = get_account()
    contract = contract_setup_with_open_minting
    price = Web3.toWei(0.12, "ether")
    _imageNumber = 5
    token_ID = 81
    artist_ID = 1
    expected_address = contract.artist(artist_ID)[1]
    secondary_sale_price = Web3.toWei(1, "ether")
    # Act
    contract.purchaseArtwork(
        _imageNumber, {"value": price, "from": deployer_account}
    )
    actual_address = contract.royaltyInfo(
        token_ID, secondary_sale_price)[0]
    # Assert
    assert expected_address == actual_address


def test_token_royalty_amount_is_set_correctly(contract_setup_with_open_minting):
    """Tests to see if the token royalty value is calculated correctly for 
    minted tokens. Test will pass if royalty payout equals 10% of secondary 
    sale price."""
    # Arrange
    deployer_account = get_account()
    contract = contract_setup_with_open_minting
    _imageNumber = 27
    price = Web3.toWei(0.36, "ether")
    token_ID = 461
    secondary_sale_price = Web3.toWei(0.5, "ether")
    expected_royalty_amount = Web3.toWei(0.05, "ether")
    # Act
    contract.purchaseArtwork(
        _imageNumber, {"value": price, "from": deployer_account}
    )
    actual_royalty_amount = contract.royaltyInfo(
        token_ID, secondary_sale_price
    )[1]
    # Assert
    assert expected_royalty_amount == actual_royalty_amount
