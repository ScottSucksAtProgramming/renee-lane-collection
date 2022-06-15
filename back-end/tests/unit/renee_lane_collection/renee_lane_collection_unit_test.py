#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_collection_unit_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
#
# Modification History
# 05-31-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# Write Contract Tests - Completed (6/13/2022)
# Write Constructor Tests - Completed (6/14/2022)
# Todo: Write mintImage() Tests
# Todo: Write tokenURI() Tests
# Todo: Write isInvestor() Tests
# Todo: Write printInvestorList() Tests
# Todo: Write checkArtistBalances() Tests
# Todo: Write withdrawFunds() Tests
# Todo: Write forcePayment() Tests
# Todo: Write getImageInfo() Tests
# Todo: Write getContractBalance() Tests


# * ------------------------------- Resources ------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import random, string, pytest

# * ------------------------------- Variables ------------------------------- #
letters = [string.ascii_letters, string.punctuation]


def generate_random_string():
    _string = "".join(random.choice(letters) for i in range(1, 3))
    return _string


# * ---------------------------- Contract Tests ----------------------------- #
def test_contract_can_deploy():
    # Arrange
    account = get_account()
    # Act
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(
        f"\nThe Renee Lane Collection contract was deployed to: {reneeLaneCollection.address}.\n"
    )
    # Assert
    assert reneeLaneCollection.address != 0


# * --------------------------- Constructor Tests --------------------------- #
# Todo: Test Collection Name
def test_collection_name_is_correct():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_name = "The Renee Lane Collection"
    print(f"\nThe expected name is: {expected_name}")
    print(f"The contract name is: {reneeLaneCollection.name()}\n")
    # Assert
    assert reneeLaneCollection.name() == expected_name


# Todo: Test collection Symbol
def test_collection_symbol_is_correct():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_symbol = "TRLC"
    print(f"\nThe expected symbol is: {expected_symbol}")
    print(f"The contract symbol is: {reneeLaneCollection.symbol()}\n")
    # Assert
    assert reneeLaneCollection.symbol() == expected_symbol


# Todo: Confirm artist mapping initiates correctly.
@pytest.mark.parametrize("artistID", [1, 2, 3, 4, 5])
def test_artist_mapping_is_correct(artistID):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_addresses = [
        (
            "0x0000000000000000000000000000000000000000,"
            "0x0000000000000000000000000000000000000000,"
        ),
        (
            "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2",
            "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2",
        ),
        (
            "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db",
            "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db",
        ),
        (
            "0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB",
            "0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB",
        ),
        (
            "0x617F2E2fD72FD9D5503197092aC168c91465E7f2",
            "0x617F2E2fD72FD9D5503197092aC168c91465E7f2",
        ),
        (
            "0x17F6AD8Ef982297579C203069C1DbfFE4348c372",
            "0x17F6AD8Ef982297579C203069C1DbfFE4348c372",
        ),
    ]
    contract_addresses = reneeLaneCollection.artist(artistID)
    print(f"\nThe expected directAddress is: {expected_addresses[artistID]}")
    print(f"The contract directAddress is: {contract_addresses}\n")
    # Assert
    assert contract_addresses == expected_addresses[artistID]


# Todo: Confirm imageGallery initiates correctly.
@pytest.mark.parametrize("_imageNumber", [0, 1, 10, 20, 21, 30, 31, 40, 41, 50])
def test_imageGallery_mapping_is_correct(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Act
    expected_properties = {
        0: (0, Web3.toWei(0.0, "ether"), 0, 0, 0),
        1: (1, Web3.toWei(0.12, "ether"), 1, 20, 1),
        10: (10, Web3.toWei(0.12, "ether"), 181, 200, 1),
        20: (20, Web3.toWei(0.24, "ether"), 381, 400, 2),
        21: (21, Web3.toWei(0.36, "ether"), 401, 410, 3),
        30: (30, Web3.toWei(0.36, "ether"), 491, 500, 3),
        31: (31, Web3.toWei(0.48, "ether"), 501, 505, 4),
        40: (40, Web3.toWei(0.48, "ether"), 546, 550, 4),
        41: (41, Web3.toWei(0.60, "ether"), 551, 553, 5),
        50: (50, Web3.toWei(0.60, "ether"), 578, 580, 5),
    }

    contract_properties = reneeLaneCollection.imageGallery(_imageNumber)
    print(f"\nThe expected image information is: {expected_properties[_imageNumber]}")
    print(f"The contract image information is: {contract_properties}\n")
    # Assert
    assert contract_properties == expected_properties[_imageNumber]


# *  ------------------------ mintImage() Tests ---------------------------- #
# Todo: Test transaction reverts if _imageNumber is out of range.
@given(_imageNumber=strategy("uint256", exclude=range(1, 50)))
def test_mintImage_reverts_when_imageNumber_is_out_of_range(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction revert, test will pass.\n")
    # Act and Assert
    with reverts():
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})


# Todo: Test transaction reverts if _imageNumber is negative.
@given(_imageNumber=strategy("int256", max_value=-1))
def test_mintImage_reverts_when_imageNumber_is_negative(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with pytest.raises(OverflowError):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})


# Todo: Test transaction reverts if _imageNumber is negative.
@given(_imageNumber=strategy("int256", max_value=-1))
def test_mintImage_reverts_when_imageNumber_is_float(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with pytest.raises(OverflowError):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})


# Todo: Test transaction reverts if _imageNumber is a string.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        generate_random_string(),
        generate_random_string(),
        generate_random_string(),
        generate_random_string(),
        generate_random_string(),
    ],
)
def test_mintImage_reverts_when_imageNumber_is_string(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an TypeError, test will pass.\n")
    # Act and Assert
    with pytest.raises(TypeError):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})


# Todo: Test _newTokenID is expected value based on _imageNumber parameter.
@given(
    transactions=strategy("uint256", min_value=0, max_value=10),
    image=strategy("uint256", min_value=1, max_value=10),
)
def test_newTokenID_is_set_correctly(transactions, image):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    for i in range(transactions):
        reneeLaneCollection.mintImage(image, {"value": Web3.toWei(0.12, "ether")})
    # Act
    expected_tokenID = reneeLaneCollection.imageGallery(image)[2]
    tx_one = reneeLaneCollection.mintImage(image, {"value": Web3.toWei(0.12, "ether")})
    print(f"\nThe expected _newTokenID() is: {expected_tokenID}.")
    print(f"The returned _newTokenID() is: {tx_one.return_value[0]}.")
    # Assert
    assert tx_one.return_value[0] == expected_tokenID


# Todo: Test transaction reverts if no more tokens are available.
def test_mintImage_reverts_if_no_more_tokens_available():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    for i in range(20):
        reneeLaneCollection.mintImage(1, {"value": Web3.toWei(0.12, "ether")})
    minted_tokens = reneeLaneCollection.imageGallery(1)[2] - 1
    supply = reneeLaneCollection.imageGallery(1)[3]
    print(f"\nTokens minted for this image: {minted_tokens}/{supply}.")
    print(f"Attempting to mint one more token.")
    print(f"If this transaction reverts correctly, test will pass.\n")
    # Act and Assert
    with reverts("No more editions of this image are available."):
        reneeLaneCollection.mintImage(1, {"value": Web3.toWei(0.12, "ether")})


# Todo: Test transaction reverts if msg.value isn't equal to price.
@given(_imageNumber=strategy("int256", min_value=1, max_value=50))
def test_mintImage_reverts_if_incorrect_value_sent(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act and Asset
    with reverts("You didn't send the correct amount of Ether."):
        reneeLaneCollection.mintImage(_imageNumber, {"value": Web3.toWei(1, "ether")})


# Todo: Test _artist is expected values.
# Todo: Test _artistCut is correct value.
# Todo: Test _projectCut is correct value.
# Todo: Test payouts owed to artist is adjusted correctly.
# Todo: Test payouts owed to project is adjusted correctly.
# Todo: Test that _safeMint works correctly.
# Todo: Test _setTokenRoyalty works correctly.
# Todo: Test that investors mapping is updated when address is not investor.
# Todo: Test that investorList is updated when address is not investor.
# Todo: Test that investors mapping is not updated when address is already investor.
# Todo: Test that investorList is not updated when address is already investor.
# Todo: Test that currentTokenID is incremented after successful mint.
# Todo: Test that currentTokenID is not incremented if transaction reverts.
