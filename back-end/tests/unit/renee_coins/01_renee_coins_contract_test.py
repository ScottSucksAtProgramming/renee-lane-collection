#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coin_contract_test.py
# This module contains the unit tests for the contract portion Renee Coins smart
# contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import config, network, ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables -------------------------------- #

# * ---------------------------- Contract Tests ------------------------------ #
def test_contract_can_deploy():
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

def test_owner_returns_expected_value():
    # Arrange
    owner = get_account()
    # Act
    reneeCoins = ReneeCoins.deploy({"from": owner})
    # Assert
    assert reneeCoins.owner() == owner


def test_owner_can_renounceOwnership():
    # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    # Act
    reneeCoins.renounceOwnership()
    # Assert
    assert reneeCoins.owner() == ZERO_ADDRESS

def test_renounceOwnership_can_only_be_called_by_owner():
        # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        reneeCoins.renounceOwnership({"from": get_account(2)})

def test_owner_can_transferOwnership():
    # Arrange
    owner = get_account()
    new_owner = get_account(1)
    reneeCoins = ReneeCoins.deploy({"from": owner})
    # Act
    reneeCoins.transferOwnership(get_account(1))
    # Assert
    assert reneeCoins.owner() == new_owner

def test_transferOwnership_can_only_be_called_by_owner():
        # Arrange
    owner = get_account()
    reneeCoins = ReneeCoins.deploy({"from": owner})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        reneeCoins.transferOwnership(get_account(7),{"from": get_account(2)})