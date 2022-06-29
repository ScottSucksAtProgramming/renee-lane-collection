#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  03_renee_coins_createCoins_test.py
# This module contains the unit tests for the createCoins() function of the
# Renee Coins smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ CreateCoins() can only be called by the owner.
# ✓ CreateCoins() mints the correct amount of Renee Coins.
# ✓ CreateCoins() mints to the correct wallet.
# ✓ CreateCoins() cannot exceed the cap.

# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts

# * ------------------------------- Variables -------------------------------- #
deployer_account = get_account()
contractObject = ReneeCoins

# * -------------------------- createCoins() Tests --------------------------- #


def test_tests_are_set_up():
    """Tests to see if the tests are set up correctly."""
    # Arrange
    if deployer_account == None:
        raise Exception("Deployer account is not set.")
    if contractObject == None:
        raise Exception("Contract object is not set.")
    # Act
    # Assert
    assert True


def test_createCoins_can_only_called_by_owner():
    """Test to see if createCoins() can only be called by the owner. Test will
    pass if transaction reverts"""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    not_owner = get_account(4)
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        reneeCoins.createCoins(10_000, {"from": not_owner})


def test_createCoins_mints_amount_expected():
    """Test to see if createCoins() mints the correct amount of Renee Coins. 
    Test will pass if total supply of Renee Coins is equal to amount minted."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    # Act
    expected_amount = 10_000
    reneeCoins.createCoins(expected_amount, {"from": deployer_account})
    # Assert
    assert reneeCoins.totalSupply() == expected_amount


def test_createCoins_mints_to_correct_wallet():
    """Test to see if createCoins() mints to the correct wallet. Test will 
    pass if balance of Renee Coins in wallet is equal to amount minted."""
    # Arrange
    reneeCoins = ReneeCoins.deploy(
        {"from": deployer_account})
    # Act
    expected_amount = 200_000
    reneeCoins.createCoins(expected_amount, {"from": deployer_account})
    # Assert
    assert reneeCoins.balanceOf(deployer_account) == expected_amount


def test_createCoins_cannot_exceed_cap():
    """Test to see if createCoins() cannot exceed the cap. Test will pass if 
    transaction trying to mint Renee Coins exceeds the cap."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_amount = 2_000_000
    additional_amount = 100
    contract.createCoins(expected_amount, {"from": deployer_account})
    # Act and Assert
    with reverts("ERC20Capped: cap exceeded"):
        contract.createCoins(additional_amount, {"from": deployer_account})
