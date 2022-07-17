#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  08_renee_coins_transferFrom_test.py
# This module contains the unit tests for the ERC-20 transferFrom behavior of
# the Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks --------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Renee Coins contract can transfer from.
# ✓ Renee Coins contract can transfer from with a value of 0.
# ✓ Transaction reverts if sender has insufficient balance.
# ✓ Transaction reverts if recipient address is invalid.
# ✓ TransferFrom logs are correct.

# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #
deployer_account = get_account()
contractObject = ReneeCoins

# * ---------------------------- Token Functions --------------------------- #


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


def test_ERC20_can_transferFrom():
    """Test to see if the contract can transfer from. Test will pass if the 
    recipient's balance is equal to the value sent."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    contract.transferFrom(deployer_account, recipient, 12, {"from": spender})
    # Assert
    assert contract.balanceOf(recipient) == 12


def test_ERC20_can_transferFrom_zero_tokens():
    """Tests to see if the contract can transfer from with a value of 0. Test 
    will pass if the logs show the value of 0."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    tx = contract.transferFrom(
        deployer_account, recipient, 0, {"from": spender})
    # Assert
    assert tx.events["Transfer"]["value"] == 0


def test_ERC20_transferFrom_reverts_if_insufficient_amount():
    """Tests to see if the sender can send more than their balance. Test will 
    pass if transaction reverts."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act and Assert
    with reverts("ERC20: insufficient allowance"):
        contract.transferFrom(
            deployer_account, recipient, 300, {"from": spender})


def test_ERC20_transferFrom_reverts_if_recipient_address_is_invalid():
    """Tests to see if transferFrom can send tokens to the zero address. Test 
    will pass if transaction reverts."""
    # Arrange
    spender = get_account(2)
    value = 100
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act and Assert
    with reverts("ERC20: transfer to the zero address"):
        contract.transferFrom(
            deployer_account, ZERO_ADDRESS, 10, {"from": spender})


def test_ERC20_transferFrom_logs_from_correctly():
    """Test to see if Transfer from logs the correct sender address. Test will 
    pass if the sender address is correct."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 12
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    tx = contract.transferFrom(
        deployer_account, recipient, 12, {"from": spender})
    # Assert
    assert deployer_account == tx.events["Transfer"]["from"]


def test_ERC20_transferFrom_logs_to_correctly():
    """Test to see if Transfer from logs the correct recipient address. Test 
    will pass if the recipient address is correct."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 12
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    tx = contract.transferFrom(
        deployer_account, recipient, 12, {"from": spender})
    # Assert
    assert recipient == tx.events["Transfer"]["to"]


def test_ERC20_transferFrom_value_from_correctly():
    """Test to see if Transfer from logs the correct value. Test will pass if 
    the value is correct."""
    # Arrange
    spender = get_account(2)
    recipient = get_account(3)
    value = 12
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(10000, {"from": deployer_account})
    contract.approve(spender, value, {"from": deployer_account})
    # Act
    tx = contract.transferFrom(
        deployer_account, recipient, 12, {"from": spender})
    # Assert
    assert value == tx.events["Transfer"]["value"]
