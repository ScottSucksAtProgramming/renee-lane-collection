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


# * ------------------------ withdrawPayout() Tests --------------------- #
# Todo: Test withdrawPayout() reverts if no funds owed.
# ! This was tested and works correctly. Test was removed because putting
# ! the require statement 2nd in the function makes it difficult to test,
# ! but makes sense for gas savings.
# def test_withdrawPayout_reverts_if_contract_does_not_have_enough_funds():
#     # Arrange
#     account = get_account()
#     reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
#     contract_balance = reneeLaneCollection.getContractBalance({"from": account})
#     # Act and Assert
#     print(f"\nBalance in contract: {contract_balance}.")
#     print(f"If transaction reverts due to no funds in contract, test will pass.\n")
#     with reverts("No money in contract."):
#         reneeLaneCollection.withdrawPayout({"from": account})


# Todo: Test withdrawPayout() reverts if contract has no funds left.
def test_withdrawPayout_reverts_if_no_payout_owed():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    balance_owed = reneeLaneCollection.payoutsOwed(get_account(3))
    # Act and Assert
    print(f"\nBalanced owed to {account}: {balance_owed}.")
    print(f"If transaction reverts due to no funds owed, test will pass.\n")
    with reverts("No funds owed to this wallet."):
        reneeLaneCollection.withdrawPayout({"from": get_account(3)})


# Todo: Test withdrawPayout() pays out as expected.
def test_withdrawPayout_pays_out_correctly():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
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
    reneeLaneCollection.withdrawPayout(
        {"from": "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"}
    )
    ending_wallet_amount = get_account(1).balance()
    print(f"The ending balance for Artist 1 is: {ending_wallet_amount}.\n")
    artist_payout = ending_wallet_amount - starting_wallet_amount

    # Assert
    assert artist_payout == expected_payout


# Todo: Test that balance is set back to zero after funds withdrawn.
def test_balance_is_zero_after_fund_withdrawal():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    starting_payout_owed = reneeLaneCollection.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    # Act
    print(f"\nStarting payout owed to Artist 1: {starting_payout_owed}.")
    print(f"Paying Artist.")
    reneeLaneCollection.withdrawPayout({"from": get_account(1)})
    end_payout_owed = reneeLaneCollection.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"Payment Complete. Remaining payout owed: {end_payout_owed}")
    # Assert
    assert end_payout_owed == 0
