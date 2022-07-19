#
# * ------------------------------ Documentation ---------------------------- #
# Module:  14_renee_lane_whitelist_test
# This module contains tests for the Renee Lane Collection Whitelist behaviors.
#
#
# Modification History
# 06-29-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ isWhitelisted can be called.
# ✓ can add new address to whitelist mapping.
# ✓ addToWhitelist can only be called by owner.
# ✓ addToWhitelist reverts if address is already on whitelist.
# ✓ can remove address from whitelist mapping.
# ✓ removeFromWhitelist can only be called by owner.
# ✓ removeFromWhitelist reverts if address is not on whitelist.
# ✓ address can call purchaseArtwork if whitelisted.
# ✓ address cannot call purchaseArtwork if not whitelisted.
# ✓ all addresses can call purchaseArtwork if ZERO_ADDRESS is whitelisted.


# * ------------------------------- Resources ------------------------------ #
from hashlib import new
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection, reverts, ZERO_ADDRESS
from web3 import Web3
import pytest
# * ------------------------------- Variables ------------------------------ #

# * ------------------------------- Fixtures ------------------------------- #


@pytest.fixture
def contract_setup():
    """Setup for the contract."""
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    return contract
# *  ------------------------ isWhitelisted Tests -------------------------- #


def test_is_whitelisted_can_be_called(contract_setup):
    """Tests to see if isWhitelisted can be called. Test will pass if
    isWhiteListed returns a value."""
    # Arrange
    contract = contract_setup
    # Act and Assert
    try:
        contract.isWhitelisted(get_account())
    except AttributeError:
        pytest.fail("isWhitelisted cannot be called.")


def test_can_add_new_address_to_whitelist_mapping(contract_setup):
    """Tests to see if a new address can be added to the whitelist. Test will 
    pass if new address returns true for isWhitelisted."""
    # Arrange
    contract = contract_setup
    new_address = get_account(4)
    # Act
    contract.addToWhitelist(new_address)
    result = contract.isWhitelisted(new_address)
    # Assert
    assert result is True


def test_addToWhitelist_can_only_be_called_by_owner(contract_setup):
    """Tests to see if addToWhitelist can only be called by the owner. Test 
    will pass if transaction is reverted when called by non-owner."""
    # Arrange
    contract = contract_setup
    non_owner = get_account(4)
    new_address = get_account(5)
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.addToWhitelist(new_address, {"from": non_owner})


def test_addToWhitelist_reverts_if_address_is_already_on_whitelist(contract_setup):
    """Tests to see if addToWhitelist throws an error if the address is 
    already on the whitelist. Test will pass if transaction is reverted."""
    # Arrange
    contract = contract_setup
    new_address = get_account(4)
    contract.addToWhitelist(new_address)
    # Act and Assert
    with reverts("Address is already on the whitelist."):
        contract.addToWhitelist(new_address)


def test_can_remove_address_from_whitelist_mapping(contract_setup):
    """Tests to see if an address can be removed from the whitelist. Test will 
    pass if address that used to return true when added to whitelist is now 
    false for isWhitelisted after being removed."""
    # Arrange
    contract = contract_setup
    new_address = get_account(4)
    contract.addToWhitelist(new_address)
    was_on_whitelist = contract.isWhitelisted(new_address)
    # Act
    contract.removeFromWhitelist(new_address)
    result = contract.isWhitelisted(new_address)
    # Assert
    assert result is False and was_on_whitelist is True


def test_removeFromWhitelist_can_only_be_called_by_owner(contract_setup):
    """Tests to see if removeFromWhitelist can only be called by the owner. 
    Test will pass if transaction is reverted when called by non-owner."""
    # Arrange
    contract = contract_setup
    non_owner = get_account(4)
    new_address = get_account(5)
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.removeFromWhitelist(new_address, {"from": non_owner})


def test_removeFromWhitelist_reverts_if_address_is_not_whitelisted(contract_setup):
    """Tests to see if removeFromWhitelist throws an error if the address is 
    not on the whitelist. Test will pass if transaction is reverted."""
    # Arrange
    contract = contract_setup
    new_address = get_account(4)
    # Act and Assert
    with reverts("Address is not on the whitelist."):
        contract.removeFromWhitelist(new_address)


def test_address_can_call_purchaseArtwork_if_whitelisted(contract_setup):
    """Tests to see if purchaseArtwork can be called by a whitelisted address. 
    Test will pass if Transfer event is emitted."""
    # Arrange
    contract = contract_setup
    minter = get_account(4)
    contract.addToWhitelist(minter)
    # Act
    tx = contract.purchaseArtwork(1, {"value": Web3.toWei(
        0.12, "ether"), "from": minter})
    # Assert
    assert tx.events["Transfer"]


def test_address_cannot_call_purchaseArtwork_if_not_whitelisted(contract_setup):
    """Tests to see if purchaseArtwork can be called by a non-whitelisted address. 
    Test will pass if transaction reverts."""
    # Arrange
    contract = contract_setup
    minter = get_account(4)
    # Act and Assert
    with reverts("You are not whitelisted"):
        contract.purchaseArtwork(1, {"value": Web3.toWei(
            0.12, "ether"), "from": minter})


def test_all_addresses_can_call_purchaseArtwork_if_zero_address_is_whitelisted(contract_setup):
    """Tests to see if purchaseArtwork can be called by a non-whitelisted address. 
    when the zero address is whitelisted. Test will pass if Transfer event is 
    emitted."""
    # Arrange
    contract = contract_setup
    minter = get_account(4)
    contract.addToWhitelist(ZERO_ADDRESS)
    # Act
    tx = contract.purchaseArtwork(1, {"value": Web3.toWei(
        0.12, "ether"), "from": minter})
    # Assert
    assert tx.events["Transfer"]
