#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_contract_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
#
# Modification History
# 06-15-22 | SRK | Module Created
# 06-28-22 | SRK | Improved documentation
# 06-28-22 | SRK | Added tests for contract level behaviors

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ 1. Contract Deploys and returns address.
# ✓ 2. Contract has all ERC721 functions.
# ✓ 3. Contract has ERC721Royalty Functions.
# ✓ 4. Contract has Ownable Functions.

# * ------------------------------- Resources ------------------------------- #
from scripts.helpful_scripts import get_account, function_exists
from scripts.helpful_data import erc721_functions, erc2981_functions, ownable_functions
from brownie import ReneeLaneCollection

# * ------------------------------- Variables ------------------------------- #
deployer_account = get_account()
contractObject = ReneeLaneCollection
# * -------------------------------- Tests ---------------------------------- #


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
    contract = contractObject.deploy(
        {"from": deployer_account},
    )
    # Assert
    assert contract.address != None


def test_contract_has_all_ERC721_public_functions():
    """Tests to see if the contract has the ERC721 functions. Test passes if the contract has the functions. Matches the
    expected functions from the ERC721 standard."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = erc721_functions
    # Act
    ERC721_functions_exist = function_exists(expected_functions, contract)
    # Assert
    assert ERC721_functions_exist


def test_contract_has_all_ERC721Royalty_functions():
    """Tests to see if the contract has the ERC721Royalty
    functions. Test passes if the contract has the functions. Matches the
    expected functions from the ERC2981 standard."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = erc2981_functions
    # Act
    ERC721Royalty_functions_exist = function_exists(
        expected_functions, contract)
    # Assert
    assert ERC721Royalty_functions_exist


def test_contract_has_all_Ownable_functions():
    """Tests to see if the contract has the Ownable
    functions. Test passes if the contract has the functions. Matches the
    expected functions from the ERC2981 standard."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_functions = ownable_functions
    # Act
    Ownable_functions_exist = function_exists(expected_functions, contract)
    # Assert
    assert Ownable_functions_exist
