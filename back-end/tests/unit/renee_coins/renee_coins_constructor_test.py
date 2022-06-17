#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coin_constructor_test.py
# This module contains the unit tests for the constructor portion Renee Coins
# smart contract.
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from webbrowser import get
from scripts.deploy_renee_coins import deploy_contract
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts
import gc

# * ------------------------------- Variables -------------------------------- #


# * --------------------------- Constructor Tests ---------------------------- #
def test_coin_name_is_correct():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_name = "Renee Coins"
    print(f"\nThe expected name is: {expected_name}")
    print(f"The contract name is: {reneeCoins.name()}\n")
    # Assert
    assert reneeCoins.name() == expected_name
    gc.collect(generation=2)


def test_coin_name_is_correct():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_symbol = "RC"
    print(f"\nThe expected symbol is: {expected_symbol}")
    print(f"The contract symbol is: {reneeCoins.symbol()}\n")
    # Assert
    assert reneeCoins.symbol() == expected_symbol
    gc.collect(generation=2)


def test_ReneeCoins_cannot_exceed_cap():
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    expected_amount = 2_000_000
    additional_amount = 1
    reneeCoins.createCoins(expected_amount, {"from": account})
    print(f"\nThe amount of coins in circulation is {reneeCoins.totalSupply()}.")
    print(
        f"Attempting to created another {additional_amount} coin. If transaction reverts due to cap, test will pass.\n"
    )
    # Act and Assert
    with reverts("ERC20Capped: cap exceeded"):
        tx = reneeCoins.createCoins(additional_amount, {"from": account})
        tx.wait(1)
    gc.collect(generation=2)
