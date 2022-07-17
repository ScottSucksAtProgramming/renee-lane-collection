#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_contract_constructor_test.py
# This module contains the unit tests for the constructor portion Renee Coins
# smart contract.
#
# Modification History
# 06-15-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests added for constructor level behaviors.
# 06-28-2022 | SRK | Updated documentation.

# * -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Contract name initialized correctly.
# ✓ Contract symbol initialized correctly.
# ✓ Contract cap initialized correctly.
# ✓ Contract owner initialized correctly.

# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins

# * ------------------------------- Variables -------------------------------- #
deployer_account = get_account()
contractObject = ReneeCoins

# * --------------------------- Constructor Tests ---------------------------- #


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


def test_contract_name_is_set_correctly():
    """Test to see if the contract name is set correctly."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    # Act
    expected_name = "Renee Coins"
    # Assert
    assert contract.name() == expected_name


def test_contract_symbol_is_set_correctly():
    """Test to see if the contract symbol is set correctly."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    # Act
    expected_symbol = "RC"
    # Assert
    assert contract.symbol() == expected_symbol


def test_contract_cap_is_set_correctly():
    """Test to see if the contract cap is set correctly."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    # Act
    expected_amount = 2_000_000
    # Assert
    assert contract.cap() == expected_amount


def test_contract_owner_is_set_correctly():
    """Test to see if the contract owner is set correctly."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    # Act
    expected_owner = deployer_account
    # Assert
    assert contract.owner() == expected_owner
