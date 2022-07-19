#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_contract_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
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
# ✓ Contract owner initialized correctly.
# ✓ Contract artGallery mapping initialized correctly.
# ✓ Contract isInvestor mapping initialized correctly.
# ✓ Contract artist mapping initialized correctly.
# ✓ Contract payoutsOwed mapping initialized correctly.

# * ------------------------------- Resources ------------------------------- #
from brownie import ZERO_ADDRESS, ReneeLaneCollection
from scripts.helpful_scripts import get_account
from brownie import ReneeLaneCollection
from scripts.helpful_scripts import get_account, check_address, check_properties
from scripts.helpful_data import artGallery_properties, artist_addresses

# * ------------------------------- Variables ------------------------------- #

# * --------------------------- Constructor Tests --------------------------- #


def test_contract_name_is_set_correctly():
    """Test to see if the contract name is set correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    expected_name = "The Renee Lane Collection"
    # Assert
    assert contract.name() == expected_name


def test_contract_symbol_is_set_correctly():
    """Test to see if the contract symbol is set correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    expected_symbol = "TRLC"
    # Assert
    assert contract.symbol() == expected_symbol


def test_contract_owner_is_set_correctly():
    """Test to see if the contract owner is set correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    expected_owner = deployer_account
    # Assert
    assert contract.owner() == expected_owner


def test_artGallery_mapping_initialized_correctly():
    """Test to see if the artGallery mapping is initialized correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    expected_properties = artGallery_properties
    # Act
    artGallery_properties_are_correct = check_properties(
        artGallery_properties, contract)
    # Assert
    assert artGallery_properties_are_correct


def test_isInvestor_mapping_initialized_correctly():
    """Test to see if the isInvestor mapping is initialized correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    if contract.isInvestor(get_account(6)) == False:
        isInvestor_mapping_is_correct = True
    else:
        print("isInvestor mapping is not initialized correctly.")
    # Assert
    assert isInvestor_mapping_is_correct


def test_artist_mapping_initialized_correctly():
    """Test to see if the artist mapping is initialized correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    expected_addresses = artist_addresses
    # Act
    artist_mapping_is_correct = check_address(
        expected_addresses, contract)
    # Assert
    assert artist_mapping_is_correct


def test_payoutsOwed_mapping_initialized_correctly():
    """Test to see if the payoutsOwed mapping is initialized correctly."""
    # Arrange
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy({"from": deployer_account})
    # Act
    if contract.payoutsOwed(get_account(7)) == 0:
        payoutsOwed_mapping_is_correct = True
    else:
        print("isInvestor mapping is not initialized correctly.")
    # Assert
    assert payoutsOwed_mapping_is_correct
