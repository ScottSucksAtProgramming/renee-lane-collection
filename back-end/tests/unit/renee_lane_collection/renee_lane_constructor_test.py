#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_contract_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
#
# Modification History
# 06-15-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #


# * ------------------------------- Resources ------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import random, string, pytest, gc

# * ------------------------------- Variables ------------------------------- #
letters = [string.ascii_letters, string.punctuation]


def generate_random_string():
    _string = "".join(random.choice(letters) for i in range(1, 3))
    return _string


PROJECT_WALLET_ADDRESS = 0xDD870FA1B7C4700F2BD7F44238821C26F7392148

# * --------------------------- Constructor Tests --------------------------- #
# Todo: Test Collection Name
def test_collection_name_is_correct():
    # Arrange
    gc.collect(generation=2)
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
    gc.collect(generation=2)


# Todo: Test collection Symbol
def test_collection_symbol_is_correct():
    # Arrange
    gc.collect(generation=2)
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
    gc.collect(generation=2)


# Todo: Confirm artist mapping initiates correctly.
def test_artist_mapping_is_correct(artistID=random.randint(1, 5)):
    # Arrange
    gc.collect(generation=2)
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
    gc.collect(generation=2)


# Todo: Confirm imageGallery initiates correctly.
def test_imageGallery_mapping_is_correct():
    # Arrange
    gc.collect(generation=2)
    image_list = [0, 1, 10, 20, 21, 30, 31, 40, 41, 50]
    _imageNumber = random.choice(image_list)
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
    gc.collect(generation=2)
