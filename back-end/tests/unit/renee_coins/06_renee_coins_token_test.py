#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  06_renee_coins_token_test.py
# This module contains the unit tests for the ERC-20 token behavior of the
# Renee Coins contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.deploy_renee_coins import deploy_renee_coins
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts

# * ------------------------------- Variables ------------------------------ #

# * ---------------------------- Token Functions --------------------------- #
# Todo: Test Renee Coins can transfer.
def test_Renee_Coins_can_be_transferred():
    # Arrange
    reneeCoins = deploy_renee_coins()
    sender = get_account()
    recipient = get_account(2)
    starting_balance = reneeCoins.balanceOf(recipient)
    amount = None
    # Act
    # Assert
    assert reneeCoins.balanceOf(recipient) == starting_balance + amount


# Todo: Test Renee Coins transfers revert if amount is greater than sender balance.
# Todo: Test Renee Coins transfers revert if recipient address is invalid.
# Todo: Test Renee Coins transfers produce correct logs.
# Todo: Test Renee Coins transferFrom() works.
# Todo: Test Renee Coins transferFrom() reverts if amount is greater than sender balance.
# Todo: Test Renee Coins transferFrom() reverts if recipient address is invalid.
# Todo: Test Renee Coins transferFrom() produces correct logs.
# Todo: Approvals
# Todo: Burning
