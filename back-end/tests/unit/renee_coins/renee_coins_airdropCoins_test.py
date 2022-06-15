#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coins_airDropCoins_test.py
# This module contains the unit tests for the airdropCoins() function of the
# Renee Coins smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from webbrowser import get
from scripts.deploy_renee_coins import deploy_contract
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts

# * ------------------------------- Variables -------------------------------- #

# * ------------------------- airdropCoins() Tests --------------------------- #


def test_airDropCoins_can_only_called_by_owner():
    # Arrange
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"\nAttempting to call airdropCoins() with {get_account(1)}.")
    print(f"If this transaction reverts due to owner error the test will pass.\n")
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        tx = reneeCoins.airdropCoins(get_account(1), 10_000, {"from": get_account(1)})
        tx.wait(1)


def test_airdropCoins_mints_amount_expected():
    # Arrange
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_amount = 10_000
    reneeCoins.airdropCoins(get_account(1), expected_amount, {"from": account})
    print(
        f"\nThe amount of coins airdropped is:   {reneeCoins.balanceOf(get_account(1))}."
    )
    print(f"The expected coins to be airdropped: {expected_amount}.\n")
    # Assert
    assert reneeCoins.totalSupply() == expected_amount


def test_airdropCoins_mints_to_correct_wallet():
    # Arrange
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_amount = 2_000_000
    expected_account = get_account(1)
    reneeCoins.airdropCoins(get_account(1), expected_amount, {"from": account})
    print(
        f"\nExpected amount of coins is: {expected_amount} minted to:     {expected_account}."
    )
    print(
        f"Actual amount of coins is:   {reneeCoins.balanceOf(get_account(1))} airdropped to: {get_account(1)}.\n"
    )
    # Assert
    assert reneeCoins.balanceOf(get_account(1)) == expected_amount
