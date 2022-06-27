#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  07_renee_coins_approval_and_allowance_test.py
# This module contains the unit tests for the ERC-20 approval and allowance
# behavior of the Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #

# * ---------------------------- Token Functions --------------------------- #
# Todo: Test approval() function.
def test_ERC20_can_approve():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    # Act
    reneeCoins.approve(spender, value, {"from": owner})
    # Assert
    assert reneeCoins.allowance(owner, spender) == value


def test_ERC20_cannot_approve_zero_address():
    # Arrange
    owner = get_account()
    spender = ZERO_ADDRESS
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000)
    # Act and Assert
    with reverts("ERC20: approve to the zero address"):
        reneeCoins.approve(spender, value)


def test_ERC20_approval_logs_correctly():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000)
    # Act
    tx = reneeCoins.approve(spender, value)
    # Assert
    assert owner == tx.events["Approval"]["owner"]
    assert spender == tx.events["Approval"]["spender"]
    assert value == tx.events["Approval"]["value"]

def test_ERC20_can_increase_allowance():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act
    reneeCoins.increaseAllowance(spender, 5, {"from": owner})
    # Assert
    assert reneeCoins.allowance(owner, spender) == value + 5

def test_ERC20_can_decrease_allowance():
    # Arrange
    owner = get_account()
    spender = get_account(2)
    value = 100
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(10000, {"from": owner})
    reneeCoins.approve(spender, value, {"from": owner})
    # Act
    reneeCoins.decreaseAllowance(spender, 5, {"from": owner})
    # Assert
    assert reneeCoins.allowance(owner, spender) == value - 5
