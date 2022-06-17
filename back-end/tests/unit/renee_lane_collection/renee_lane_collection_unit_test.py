#
# * ------------------------------ Documentation --------------------------- #
# Module:  renee_lane_collection_token_test.py
# This module contains all the unit tests for tokens created by The Renee Lane
# collection.
#
#
# Modification History
# 06-17-22 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account, characters
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import gc, random, string, pytest

# * ------------------------------- Variables ------------------------------ #


def generate_random_string():
    _string = "".join(random.choice(characters) for i in range(1, 3))
    return _string


# * ---------------------------- tokenURI() Tests -------------------------- #
