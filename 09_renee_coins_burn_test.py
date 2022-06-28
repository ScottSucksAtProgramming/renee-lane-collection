#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  09_renee_count_burn_test.py
# This module contains the unit tests for the ERC-20 transfer behavior of the
# Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #

# * ---------------------------- burn Functions --------------------------- #
# Todo: Test burn() function
def test_token_owner_can_burn_tokens():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act
    amount_to_be_burnt = 5
    reneeCoins.burn(amount_to_be_burnt)
    # Assert
    assert reneeCoins.balanceOf(owner) == 95


def test_burn_reverts_if_balance_below_amount():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act
    amount_to_be_burnt = 200
    with reverts("ERC20: burn amount exceeds balance"):
        reneeCoins.burn(amount_to_be_burnt)


def test_burn_logs_from_correctly():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burn(amount_to_be_burnt)
    # Assert
    assert expected_from == tx.events["Transfer"]["from"]

def test_burn_logs_t0_correctly():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burn(amount_to_be_burnt)
    # Assert
    assert expected_to == tx.events["Transfer"]["to"]

def test_burn_logs_value_correctly():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burn(amount_to_be_burnt)
    # Assert
    assert expected_value == tx.events["Transfer"]["value"]

def test_spender_can_burnFrom_approved_tokens():
    # Arrange
    owner = get_account()
    spender = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    reneeCoins.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    reneeCoins.burnFrom(owner, amount_to_be_burnt, {"from": spender})
    # Assert
    assert reneeCoins.balanceOf(owner) == 90


def test_burnFrom_reverts_if_spender_not_approved():
    # Arrange
    owner = get_account()
    spender = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    # Act and Assert
    amount_to_be_burnt = 10
    with reverts("ERC20: insufficient allowance"):
        reneeCoins.burnFrom(owner, amount_to_be_burnt, {"from": spender})


def test_burnFrom_logs_from_correctly():
    # Arrange
    owner = get_account()
    spender = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    reneeCoins.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burnFrom(owner, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_from == tx.events["Transfer"]["from"]

def test_burnFrom_logs_to_correctly():
    # Arrange
    owner = get_account()
    spender = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    reneeCoins.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burnFrom(owner, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_to == tx.events["Transfer"]["to"]

def test_burnFrom_logs_value_correctly():
    # Arrange
    owner = get_account()
    spender = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    reneeCoins.createCoins(100)
    reneeCoins.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = owner
    expected_value = amount_to_be_burnt
    tx = reneeCoins.burnFrom(owner, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_value == tx.events["Transfer"]["value"]