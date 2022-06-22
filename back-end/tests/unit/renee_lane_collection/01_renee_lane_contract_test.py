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
