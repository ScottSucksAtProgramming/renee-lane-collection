#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  unit_tests.py
# This module contains the unit tests for the createCoins() function of the
# Renee Coins smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from scripts.deploy_renee_coins import deploy_renee_coins
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts
import gc

# * ------------------------------- Variables -------------------------------- #

# * -------------------------- createCoins() Tests --------------------------- #


def test_createCoins_can_only_called_by_owner():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act and Assert
    print(f"\nThe Owner of the contract is {reneeCoins.owner()}.")
    print(
        f"Attempting to call createCoins() with account {get_account(1)}. If transaction reverts due to ownership, test will pass.\n"
    )
    with reverts("Ownable: caller is not the owner"):
        tx = reneeCoins.createCoins(10_000, {"from": get_account(1)})
    gc.collect(generation=2)


def test_createCoins_mints_amount_expected():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_amount = 10_000
    reneeCoins.createCoins(expected_amount, {"from": account})
    print(f"\nThe amount of coins created is:  {reneeCoins.balanceOf(account)}.")
    print(f"The expected amount of coins is: {expected_amount}.\n")
    # Assert
    assert reneeCoins.totalSupply() == expected_amount
    gc.collect(generation=2)


def test_createCoins_mints_to_correct_wallet():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_amount = 2_000_000
    reneeCoins.createCoins(expected_amount, {"from": account})
    print(f"\nThe amount of coins created is: {reneeCoins.balanceOf(account)}.")
    print(f"The amount of coins expected:   {expected_amount}.\n")
    # Assert
    assert reneeCoins.balanceOf(account) == expected_amount
    gc.collect(generation=2)
