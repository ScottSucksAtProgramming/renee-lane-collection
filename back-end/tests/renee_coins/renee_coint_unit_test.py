#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  unit_tests.py
# This module contains all the unit tests for the Renee Coins smart contract.
#
#
# Modification History
# 06-12-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from webbrowser import get
from scripts.deploy_renee_coins import deploy_contract
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts

# * ------------------------------- Variables -------------------------------- #

# * ----------------------------- Contract Tests ---------------------------------- #
def test_deploy():
    # Arrange
    account = get_account()
    # Act
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    starting_value = reneeCoins.totalSupply()
    expected = 0
    print(
        f"\nThe Renee Coins contract was deployed to: {reneeCoins.address}.\nThe total supply of Renee Coins is: {reneeCoins.totalSupply()}\n"
    )
    # Assert
    assert starting_value == expected


# * --------------------------- Constructor Tests ---------------------------- #
def test_coin_name_is_correct():
    # Arrange
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


def test_coin_name_is_correct():
    # Arrange
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


def test_ReneeCoins_cannot_exceed_cap():
    # Arrange
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


# * -------------------------- createCoins() Tests --------------------------- #


def test_createCoins_can_only_called_by_owner():
    # Arrange
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
        tx.wait(1)


def test_createCoins_mints_amount_expected():
    # Arrange
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


def test_createCoins_mints_to_correct_wallet():
    # Arrange
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


# * ------------------------ decimals() Function --------------------------- #
def test_decimals_is_set_correctly():
    # Arrange and Act
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    expected_decimals = 0
    print(f"\nExpected decimals: {expected_decimals}.")
    print(f"Actual decimals:   {reneeCoins.decimals()}.\n")
    # Assert
    assert expected_decimals == reneeCoins.decimals()
