#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_collection_unit_test.py
# This module contains all the unit tests for mintArtwork() function in The
# Renee Lane Collection smart contract.
#
#
# Modification History
# 06-17-22 | SRK | Module Created
# 06-29-22 | SRK | Tests moved to separate files.
# 06-29-22 | SRK | Added tests no achieves 100% coverage for mintArtwork()

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ Test mintArtwork() function reverts when imageNumber is out of range.
# ✓ Test mintArtwork() function reverts when imageNumber is negative.
# ✓ Test mintArtwork() function reverts when imageNumber is a float.
# ✓ Test mintArtwork() function reverts when imageNumber is a string.
# ✓ Test mintArtwork() function reverts if no more tokens are available.
# ✓ Test mintArtwork() function reverts if incorrect price sent.
# ✓ Test mintArtwork() function reverts if no value sent.
# ✓ Test mintArtwork() function calculates artist payouts correctly.
# ✓ Test mintArtwork() function calculates project payouts correctly.
# ✓ Test mintArtwork() function increments currentTokenID correctly.
# ✓ Test mintArtwork() function does not increment currentTokenID if reverted.
# ✓ Test mintArtwork() function logs correctly.


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account, generate_random_string
from brownie import ZERO_ADDRESS, ReneeLaneCollection, reverts
from web3 import Web3
import pytest
# * ------------------------------- Variables ------------------------------ #
# * ------------------------------- Fixtures ------------------------------- #


@pytest.fixture
def contract_setup_with_open_minting():
    """Setup for the contract."""
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    contract.addToWhitelist(ZERO_ADDRESS)
    return contract
# *  ------------------------ mintArtwork() Positive Tests -------------------------- #


def test_artist_payout_calculated_correctly(contract_setup_with_open_minting):
    """Tests to see if artist payout is calculated correctly. Test will pass
    if payouts owed to artist is updated with correct value."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 35
    img_price = Web3.toWei(0.48, "ether")
    artist_address = "0x617F2E2fD72FD9D5503197092aC168c91465E7f2"
    expected_payout = Web3.toWei(0.048, "ether")
    # Act
    contract.mintArtwork(_imageNumber, {"value": img_price})
    # Assert
    assert contract.payoutsOwed(artist_address) == expected_payout


def test_project_payout_calculated_correctly(contract_setup_with_open_minting):
    """Tests to see if project payout is calculated correctly. Test will pass
    if the payout owed to the project owner is correct."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 43

    project_address = contract.PROJECT_WALLET_ADDRESS()
    img_price = Web3.toWei(0.6, "ether")
    expected_payout = Web3.toWei(0.54, "ether")
    # Act
    contract.mintArtwork(_imageNumber, {"value": img_price})
    # Assert
    assert contract.payoutsOwed(project_address) == expected_payout


def test_currentTokenID_increments_after_successful_mint(contract_setup_with_open_minting):
    """Tests to see if currentTokenID increments after successful mint. Test 
    will pass if currentTokenID increments by 1."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 16
    price = Web3.toWei(0.24, "ether")
    starting_token_id = 312

    for i in range(11):
        contract.mintArtwork(
            _imageNumber, {"value": price, "from": deployer_account})
    # Act
    contract.mintArtwork(
        _imageNumber, {"value": price, "from": deployer_account})
    ending_token_id = contract.artGallery(_imageNumber)[2]
    # Assert
    assert ending_token_id == starting_token_id + 1


#* ----------------------------- Log Tests --------------------------------- #


def test_mintArtwork_logs_from_address_correctly(contract_setup_with_open_minting):
    """Tests to see if mintArtwork logs the correct 'from' address. Test will 
    pass if the correct address is logged."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 49
    price = Web3.toWei(0.6, "ether")
    # Act
    tx = contract.mintArtwork(
        _imageNumber, {"value": price, "from": deployer_account})
    # Assert
    assert tx.events["Transfer"]["from"] == ZERO_ADDRESS


def test_mintArtwork_logs_to_address_correctly(contract_setup_with_open_minting):
    """Tests to see if mintArtwork logs the correct 'to' address. Test will 
    pass if the correct address is logged."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 49
    price = Web3.toWei(0.6, "ether")
    # Act
    tx = contract.mintArtwork(
        _imageNumber, {"value": price, "from": deployer_account})
    # Assert
    assert tx.events["Transfer"]["to"] == deployer_account


def test_mintArtwork_logs_tokenID_correctly(contract_setup_with_open_minting):
    """Tests to see if mintArtwork logs the correct tokenID. Test 
    will pass if the correct tokenID is logged."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 40
    price = Web3.toWei(0.48, "ether")
    # Act
    tx = contract.mintArtwork(
        _imageNumber, {"value": price, "from": deployer_account})
    # Assert
    assert tx.events["Transfer"]["tokenId"] == 546

#* -------------------------- Reverting Tests ------------------------------ #


def test_mintArtwork_reverts_if_no_value_sent(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts if no value sent. Test will pass if
    transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 27
    # Act and Asset
    with reverts("You didn't send the correct amount of Ether."):
        contract.mintArtwork(_imageNumber)


def test_mintArtwork_reverts_when_imageNumber_is_above_range(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts when imageNumber is out of range.
    Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    # Act and Assert
    with reverts("The image you have selected does not exist in this collection."):
        contract.mintArtwork(250, {"from": deployer_account})


def test_mintArtwork_reverts_when_imageNumber_is_below_range(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts when imageNumber is out of range.
    Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    # Act and Assert
    with reverts("The image you have selected does not exist in this collection."):
        contract.mintArtwork(0, {"from": deployer_account})


def test_mintArtwork_reverts_when_imageNumber_is_negative(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts when imageNumber is negative.
    Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = -234
    # Act and Assert
    with pytest.raises(OverflowError):
        contract.mintArtwork(_imageNumber, {"from": deployer_account})


def test_mintArtwork_reverts_when_imageNumber_is_float(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts when imageNumber is a float.
    Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 2134.234
    # Act and Assert
    with reverts("The image you have selected does not exist in this collection."):
        contract.mintArtwork(_imageNumber, {"from": deployer_account})


def test_mintArtwork_reverts_when_imageNumber_is_string(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts when imageNumber is a string.
    Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = generate_random_string()
    # Act and Assert
    with pytest.raises(TypeError):
        contract.mintArtwork(_imageNumber, {"from": deployer_account})


def test_mintArtwork_reverts_if_no_more_tokens_available(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts if no more tokens are available
    for that image. Test will pass if the transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    for i in range(20):
        contract.mintArtwork(
            1, {"from": deployer_account, "value": Web3.toWei(0.12, "ether")})
    # Act and Assert
    with reverts("No more editions of this image are available."):
        contract.mintArtwork(1, {"value": Web3.toWei(0.12, "ether")})


def test_mintArtwork_reverts_if_incorrect_value_sent(contract_setup_with_open_minting):
    """Tests to see if mintArtwork reverts if incorrect price sent. Test will
    pass if transaction reverts."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    # Act and Asset
    with reverts("You didn't send the correct amount of Ether."):
        contract.mintArtwork(1, {"value": Web3.toWei(1, "ether")})


def test_currentTokenID_does_not_increment_if_transaction_reverts(contract_setup_with_open_minting):
    """Tests to see if currentTokenID does not increment if minting reverts. 
    Test will pass if ending token ID is the same as starting token ID."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    _imageNumber = 49
    price = Web3.toWei(1, "ether")
    original_tokenID = 575
    # Act
    with reverts("You didn't send the correct amount of Ether."):
        contract.mintArtwork(
            _imageNumber, {"value": price, "from": deployer_account}
        )
    currentTokenID = contract.artGallery(_imageNumber)[2]
    # Assert
    assert currentTokenID == original_tokenID
