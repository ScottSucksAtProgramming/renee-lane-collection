#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  06_renee_coins_transfer_test.py
# This module contains the unit tests for the ERC-20 transfer behavior of the
# Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks --------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Tokens can be transferred.
# ✓ Transaction reverts when attempting to send more coins than owned.
# ✓ Transaction reverts when attempting to send to the zero address.
# ✓ Transaction logs are correct.

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


def test_ERC20_can_transfer():
    """This test will attempt to transfer 12 tokens from sender to recipient.
    It will pass if the recipient's balance after the transfer equals amount 
    sent."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    sender = get_account()
    recipient = get_account(2)
    # Act
    reneeCoins.createCoins(500, {"from": deployer_account})
    reneeCoins.transfer(recipient, 12)
    # Assert
    assert reneeCoins.balanceOf(recipient) == 12


def test_ERC20_transfer_reverts_if_insufficient_amount():
    """This test will attempt to transfer 700 tokens from an account who only
    has 500 tokens. It will pass if this transaction reverts with the error
    message: ERC20: transfer amount exceeds balance."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    recipient = get_account(2)
    # Act
    reneeCoins.createCoins(500, {"from": deployer_account})
    # Assert
    with reverts("ERC20: transfer amount exceeds balance"):
        reneeCoins.transfer(recipient, 700, {"from": deployer_account})


def test_ERC20_transfer_reverts_if_recipient_address_is_invalid():
    """This test will attempt to transfer 10 tokens to the Zero Address (0x0).
    It will pass if the transaction reverts with the error message:
    ERC20: transfer to the zero address."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    # Act
    reneeCoins.createCoins(500, {"from": deployer_account})
    # Assert
    with reverts("ERC20: transfer to the zero address"):
        reneeCoins.transfer(ZERO_ADDRESS, 10, {"from": deployer_account})


def test_ERC20_transfer_logs_from_correctly():
    """This test will compare the 'from' values of the transfer event log to
    what is expected. The test will pass if the actual and expected 'from'
    values are the same."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    sender = get_account()
    recipient = get_account(2)
    # Act
    reneeCoins.createCoins(500, {"from": deployer_account})
    transfer = reneeCoins.transfer(recipient, 12)
    expected_from = deployer_account
    # Assert
    assert expected_from == transfer.events["Transfer"]["from"]


def test_ERC20_transfer_logs_to_correctly():
    """This test will compare the 'to' values of the transfer event log to
    what is expected. The test will pass if the actual and expected 'to'
    values are the same."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    recipient = get_account(2)
    # Act
    reneeCoins.createCoins(500, {"from": deployer_account})
    transfer = reneeCoins.transfer(recipient, 12)
    expected_to = recipient
    # Assert
    assert expected_to == transfer.events["Transfer"]["to"]


def test_ERC20_transfer_logs_value_correctly():
    """This test will compare the 'value' values of the transfer event log to
    what is expected. The test will pass if the actual and expected 'value'
    values are the same."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": get_account()})
    sender = get_account()
    recipient = get_account(2)
    # Act
    reneeCoins.createCoins(500, {"from": sender})
    transfer = reneeCoins.transfer(recipient, 12)
    # Assert
    assert 12 == transfer.events["Transfer"]["value"]
