#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  07_renee_coins_approval_and_allowance_test.py
# This module contains the unit tests for the ERC-20 approval and allowance
# behavior of the Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks --------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Approvals can be set.
# ✓ Allowance can be increased.
# ✓ Allowance can be decreased.
# ✓ Reverts if the spender is the zero address.
# ✓ Reverts if the value is negative.
# ✓ Approval logs are correct.

# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS
from pytest import raises

# * ------------------------------- Variables ------------------------------ #
deployer_account = get_account()
contractObject = ReneeCoins

# * ----------------------------- Approve Tests ---------------------------- #


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


def test_ERC20_can_approve():
    """Tests to see if the ERC-20 approval behavior is correct. Test will pass
    if the allowance of the spender is set to the value."""
    # Arrange
    spender = get_account(2)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    # Act
    contract.approve(spender, value, {"from": deployer_account})
    # Assert
    assert contract.allowance(deployer_account, spender) == value


def test_ERC20_can_increase_allowance():
    """Tests to see if the ERC-20 approval behavior is correct. Test will pass 
    if the allowance of the spender is increased by the value."""
    # Arrange
    spender = get_account(2)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    contract.increaseAllowance(spender, 5, {"from": deployer_account})
    # Assert
    assert contract.allowance(deployer_account, spender) == value + 5


def test_ERC20_can_decrease_allowance():
    """Tests to see if the ERC-20 approval behavior is correct. Test will pass if the allowance of the spender is decreased by the value."""
    # Arrange
    spender = get_account(2)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    contract.decreaseAllowance(spender, 5, {"from": deployer_account})
    # Assert
    assert contract.allowance(deployer_account, spender) == value - 5


def test_ERC20_cannot_approve_zero_address():
    """Tests to see if the zero address can be used as the spender. Test will 
    pass if the transaction reverts."""
    # Arrange
    spender = ZERO_ADDRESS
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000)
    # Act and Assert
    with reverts("ERC20: approve to the zero address"):
        contract.approve(spender, value)


def test_ERC20_cannot_approve_negative_amount():
    """Tests to see if the ERC-20 approval behavior is correct. Test will pass
    if transaction throws OverFlow exception."""
    # Arrange
    spender = get_account(2)
    value = -100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    # Act and Assert
    with raises(OverflowError):
        contract.approve(spender, value, {"from": deployer_account})


def test_ERC20_approval_logs_owner_correctly():
    """Tests to see if the approval logs the owner address correctly. Test 
    will pass if the owner address is correct."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000)
    # Act
    tx = contract.approve(spender, value)
    # Assert
    assert deployer_account == tx.events["Approval"]["owner"]


def test_ERC20_approval_logs_spender_correctly():
    """Tests to see if the approval logs the spender address correctly. Test 
    will pass if the spender address is correct."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000)
    # Act
    tx = contract.approve(spender, value)
    # Assert
    assert spender == tx.events["Approval"]["spender"]


def test_ERC20_approval_logs_value_correctly():
    """Tests to see if the approval logs the value correctly. Test will pass 
    if the value is correct."""
    # Arrange
    spender = get_account(2)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000)
    # Act
    tx = contract.approve(spender, value)
    # Assert
    assert value == tx.events["Approval"]["value"]
