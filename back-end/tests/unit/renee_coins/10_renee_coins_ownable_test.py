#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  10_renee_count_ownable_test.py
# This module contains the unit tests for the Ownable Extension behavior of
# the Renee Coins contract.
#
# Modification History
# 06-28-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks --------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Owner can transfer ownership.
# ✓ Owner can renounce ownership.
# ✓ Renounce ownership can only be called by owner.
# ✓ Transfer ownership can only be called by owner.
# ✓ Owner returns expected value.

# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #
deployer_account = get_account()
contractObject = ReneeCoins

# * ------------------------- Ownable Functions ---------------------------- #


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


def test_owner_returns_expected_value():
    """test to see if owner returns expected value. Test will pass if owner is 
    correct."""
    # Arrange
    # Act
    contract = ReneeCoins.deploy({"from": deployer_account})
    # Assert
    assert contract.owner() == deployer_account


def test_owner_can_renounceOwnership():
    """Test to see if owner can renounce ownership. Test will pass if owner is 
    set to zero address."""
    # Arrange
    contract = ReneeCoins.deploy({"from": deployer_account})
    # Act
    contract.renounceOwnership({"from": deployer_account})
    # Assert
    assert contract.owner() == ZERO_ADDRESS


def test_renounceOwnership_can_only_be_called_by_owner():
    """Test to see if renounce ownership can only be called by owner. Test 
    will pass if transaction reverts."""
    # Arrange
    contract = ReneeCoins.deploy({"from": deployer_account})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.renounceOwnership({"from": get_account(2)})


def test_owner_can_transferOwnership():
    """Test to see if owner can transfer ownership. Test will pass if owner is 
    set to new owner."""
    # Arrange
    new_owner = get_account(1)
    contract = ReneeCoins.deploy({"from": deployer_account})
    # Act
    contract.transferOwnership(get_account(1))
    # Assert
    assert contract.owner() == new_owner


def test_transferOwnership_can_only_be_called_by_owner():
    """Test to see if transfer ownership can only be called by owner. Test 
    will pass if transaction reverts."""
    # Arrange
    contract = ReneeCoins.deploy({"from": deployer_account})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.transferOwnership(get_account(7), {"from": get_account(2)})
