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

# * --------------------------- forcePayment() Tests ----------------------- #
# Todo: Test forcePayment can only be called by Owner.


def test_forcePayment_can_only_be_called_by_owner(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.forcePayment(
            get_account(1), {"from": get_account(1)})


# Todo: Test forcePayment reverts if no money owed to _address.
def test_forcePayment_reverts_if_no_money_owed(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    owner = get_account()
    # Act and Assert
    with reverts("No money owed to this address."):
        contract.forcePayment(get_account(3), {"from": owner})


# Todo: Test forcePayment sends payment correctly.
def test_forcePayment_pays_out_correctly(contract_setup_with_open_minting):
    # Arrange
    owner = get_account()
    contract = contract_setup_with_open_minting
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    artist_wallet = get_account(1)
    # Act
    starting_wallet_amount = get_account(1).balance()
    expected_payout = contract.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"\nThe starting balance for Artist 1 is: {starting_wallet_amount}")
    print(
        f"The expected payout for Artist 1 is: {expected_payout}.\nInitiating payout."
    )
    contract.forcePayment(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3", {"from": owner}
    )
    ending_wallet_amount = get_account(1).balance()
    print(f"The ending balance for Artist 1 is: {ending_wallet_amount}.\n")
    artist_payout = ending_wallet_amount - starting_wallet_amount


# Todo: Test forcePayment sets balance to zero after completion.
def test_balance_is_zero_after_forcedPayout(contract_setup_with_open_minting):
    # Arrange
    owner = get_account()
    contract = contract_setup_with_open_minting
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    starting_payout_owed = contract.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    # Act
    print(f"\nStarting payout owed to Artist 1: {starting_payout_owed}.")
    print(f"Paying Artist.")
    contract.forcePayment(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3", {"from": owner}
    )
    end_payout_owed = contract.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"Payment Complete. Remaining payout owed: {end_payout_owed}")
    # Assert
    assert end_payout_owed == 0
