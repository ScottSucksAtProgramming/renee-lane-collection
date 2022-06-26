#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  08_renee_coins_transferFrom_test.py
# This module contains the unit tests for the ERC-20 transferFrom behavior of
# the Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #

# * ---------------------------- Token Functions --------------------------- #
# Todo: Test transferFrom() function.
def test_ERC20_can_transferFrom():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act
    reneeCoins.transferFrom(owner, recipient, 12, {"from": spender})
    # Assert
    assert reneeCoins.balanceOf(recipient) == 12


def test_ERC20_transferFrom_reverts_if_insufficient_amount():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act and Assert
    with reverts("ERC20: insufficient allowance"):
        reneeCoins.transferFrom(owner, recipient, 300, {"from": spender})


def test_ERC20_transferFrom_reverts_if_recipient_address_is_invalid():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act and Assert
    with reverts("ERC20: transfer to the zero address"):
        reneeCoins.transferFrom(owner, ZERO_ADDRESS, 10, {"from": spender})


def test_ERC20_transferFrom_logs_from_correctly():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    recipient = get_account(3)
    value = 12
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act
    tx = reneeCoins.transferFrom(owner, recipient, 12, {"from": spender})
    # Assert
    assert owner == tx.events["Transfer"]["from"]
    assert recipient == tx.events["Transfer"]["to"]
    assert value == tx.events["Transfer"]["value"]
