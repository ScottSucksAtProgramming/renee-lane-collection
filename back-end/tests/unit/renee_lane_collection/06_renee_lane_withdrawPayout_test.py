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

# * ------------------------ withdrawPayout() Tests --------------------- #


def test_withdrawPayout_assigns_PROJECT_WALLET_ADDRESS_when_called_by_owner(contract_setup_with_open_minting):
    """Test to see if the PROJECT_WALLET_ADDRESS is assigned as the payment 
    recipient when withdrawPayout is called by the contract owner. Test will 
    pass if the PayoutSent 'recipientAddress' is equal to the 
    PROJECT_WALLET_ADDRESS."""
    # Arrange
    contract = contract_setup_with_open_minting
    owner = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    # Act
    tx = contract.withdrawPayout({"from": owner})
    # Assert
    assert tx.events["PayoutSent"]['recipientAddress'] == contract.PROJECT_WALLET_ADDRESS()


def test_withdrawPayout_assigns_sends_to_msg_sender_when_called_by_non_owner(contract_setup_with_open_minting):
    """Test to see if the caller of withdrawPayout is assigned as the payment 
    recipient when withdrawPayout is called by a non-owner. Test will pass if 
    the PayoutSent 'recipientAddress' is equal to the caller of 
    withdrawPayout."""
    # Arrange
    contract = contract_setup_with_open_minting
    owner = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": owner}
    )
    artist_address = contract.artist(1)[0]
    # Act
    tx = contract.withdrawPayout({"from": artist_address})
    # Assert
    assert tx.events["PayoutSent"]['recipientAddress'] == artist_address


def test_withdrawPayout_reverts_if_contract_does_not_have_enough_funds(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    contract_balance = contract.getContractBalance(
        {"from": account})
    # Act and Assert
    print(f"\nBalance in contract: {contract_balance}.")
    print(f"If transaction reverts due to no funds in contract, test will pass.\n")
    with reverts("No money in contract."):
        contract.withdrawPayout({"from": account})


# Todo: Test withdrawPayout() reverts if contract has no funds left.
def test_withdrawPayout_reverts_if_no_payout_owed(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    balance_owed = contract.payoutsOwed(get_account(3))
    # Act and Assert
    print(f"\nBalanced owed to {account}: {balance_owed}.")
    print(f"If transaction reverts due to no funds owed, test will pass.\n")
    with reverts("No funds owed to this wallet."):
        contract.withdrawPayout({"from": get_account(3)})


# Todo: Test withdrawPayout() pays out as expected.
def test_withdrawPayout_pays_out_correctly(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
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
    contract.withdrawPayout(
        {"from": "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"}
    )
    ending_wallet_amount = get_account(1).balance()
    print(f"The ending balance for Artist 1 is: {ending_wallet_amount}.\n")
    artist_payout = ending_wallet_amount - starting_wallet_amount

    # Assert
    assert artist_payout == expected_payout


# Todo: Test that balance is set back to zero after funds withdrawn.
def test_balance_is_zero_after_fund_withdrawal(contract_setup_with_open_minting):
    # Arrange
    contract = contract_setup_with_open_minting
    account = get_account()
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": account}
    )
    starting_payout_owed = contract.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    # Act
    print(f"\nStarting payout owed to Artist 1: {starting_payout_owed}.")
    print(f"Paying Artist.")
    contract.withdrawPayout({"from": get_account(1)})
    end_payout_owed = contract.payoutsOwed(
        "0x33A4622B82D4C04A53E170C638B944CE27CFFCE3"
    )
    print(f"Payment Complete. Remaining payout owed: {end_payout_owed}")
    # Assert
    assert end_payout_owed == 0
