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
from scripts.helpful_scripts import get_account, characters
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import gc, random, string, pytest

# * ------------------------------- Variables ------------------------------ #


def generate_random_string():
    _string = "".join(random.choice(characters) for i in range(1, 3))
    return _string


# * --------------------------- forcePayment() Tests ----------------------- #
# Todo: Test forcePayment can only be called by Owner.
def test_forcePayment_can_only_be_called_by_owner():
    # Arrange
    owner = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": owner})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        reneeLaneCollection.forcePayment(get_account(1), {"from": get_account(1)})


# Todo: Test forcePayment reverts if no money owed to _address.
def test_forcePayment_reverts_if_no_money_owed():
    # Arrange
    owner = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": owner})
    # Act and Assert
    with reverts("No money owed to this address."):
        reneeLaneCollection.forcePayment(get_account(3), {"from": owner})


# Todo: Test forcePayment sends payment correctly.
def test_forcePayment_pays_out_correctly():
    # Arrange
    owner = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": owner})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    artist_wallet = get_account(1)
    # Act
    starting_wallet_amount = get_account(1).balance()
    expected_payout = reneeLaneCollection.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"\nThe starting balance for Artist 1 is: {starting_wallet_amount}")
    print(
        f"The expected payout for Artist 1 is: {expected_payout}.\nInitiating payout."
    )
    reneeLaneCollection.forcePayment(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3", {"from": owner}
    )
    ending_wallet_amount = get_account(1).balance()
    print(f"The ending balance for Artist 1 is: {ending_wallet_amount}.\n")
    artist_payout = ending_wallet_amount - starting_wallet_amount


# Todo: Test forcePayment sets balance to zero after completion.
def test_balance_is_zero_after_forcedPayout():
    # Arrange
    owner = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": owner})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    starting_payout_owed = reneeLaneCollection.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    # Act
    print(f"\nStarting payout owed to Artist 1: {starting_payout_owed}.")
    print(f"Paying Artist.")
    reneeLaneCollection.forcePayment(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3", {"from": owner}
    )
    end_payout_owed = reneeLaneCollection.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"Payment Complete. Remaining payout owed: {end_payout_owed}")
    # Assert
    assert end_payout_owed == 0
