#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  renee_coins_decimals_test.py
# This module contains the unit tests for the decimals() function of the Renee
# Coins smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ decimals() is set correctly.

# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins

# * ------------------------------- Variables -------------------------------- #
deployer_account = get_account()
contractObject = ReneeCoins

# * ------------------------- decimals() Tests --------------------------- #


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


def test_decimals_is_set_correctly():
    """Tests to see if the decimals() function is set correctly. Test will 
    pass if decimals returned is 0."""
    # Arrange and Act
    contract = contractObject.deploy({"from": deployer_account})
    expected_decimals = 0
    # Assert
    assert expected_decimals == contract.decimals()
