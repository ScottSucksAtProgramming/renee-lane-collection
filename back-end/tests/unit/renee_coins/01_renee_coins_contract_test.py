#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coin_contract_test.py
# This module contains the unit tests for the contract portion Renee Coins
# smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests added for contract level behaviors.
# 06-28-2022 | SRK | Updated documentation.

# * -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ✓ 1. Contract Deploys and returns address.
# ✓ 2. Contract has all ERC20 functions.
# ✓ 3. Contract has ERC20Burnable Functions.
# ✓ 4. Contract has ERC20Capped Functions.
# ✓ 5. Contract has Ownable Functions.

# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account, function_exists
from scripts.helpful_data import (
    erc20_functions,
    erc20burnable_functions,
    erc20capped_functions,
    ownable_functions,
)
from brownie import ReneeCoins

# * ------------------------------- Variables -------------------------------- #
deployer_account = get_account()
contractObject = ReneeCoins
# * ---------------------------- Contract Tests ------------------------------ #


def test_tests_are_set_up():
    """Tests to see if the tests are set up correctly."""
    # Arrange
    # Act
    if deployer_account == None:
        raise Exception("Deployer account is not set.")
    if contractObject == None:
        raise Exception("Contract object is not set.")
    # Assert
    assert True


def test_contract_can_deploy():
    """Tests to see if the smart contract can be deployed. Test passes if
    deployed contract returns an address."""
    # Arrange
    # Act
    contract = contractObject.deploy({"from": deployer_account})
    # Assert
    assert contract.address != None


def test_contract_has_all_ERC20_public_functions():
    """Tests to see if the contract has the ERC20 functions. Test passes if
    the contract has the functions. Matches the expected functions from the
    ERC20 standard."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = erc20_functions
    # Act
    has_all_functions = function_exists(expected_functions, contract)
    # Assert
    assert has_all_functions


def test_contract_has_all_ERC20Burnable_public_functions():
    """Tests to see if the contract has the ERC20Burnable functions. Test passes if
    the contract has the functions."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = erc20burnable_functions
    # Act
    has_all_functions = function_exists(expected_functions, contract)
    # Assert
    assert has_all_functions


def test_contract_has_all_ERC20Capped_public_functions():
    """Tests to see if the contract has the ERC20Capped functions. Test passes if
    the contract has the functions."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = erc20capped_functions
    # Act
    has_all_functions = function_exists(expected_functions, contract)
    # Assert
    assert has_all_functions


def test_contract_has_all_Ownable_functions():
    """Tests to see if the ReneeLaneCollection contract has the Ownable
    functions. Test passes if the contract has the functions. Matches the
    expected functions from the ERC2981 standard."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = ownable_functions
    # Act
    has_all_functions = function_exists(expected_functions, contract)
    # Assert
    assert has_all_functions
