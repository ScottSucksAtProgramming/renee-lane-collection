# ------------------------------ Documentation ------------------------------ #
# Module:  deploy_renee_coins.py
# This script will deploy the Renee Coins smart contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #
from brownie import config, network, ReneeLaneCollection, ZERO_ADDRESS
from scripts.helpful_scripts import get_account


# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #
def get_price(imageNumber):
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection[-1]
    price = reneeLaneCollection.artGallery(imageNumber)[1]
    return price


def whitelist_zero_address():
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection[-1]
    tx = reneeLaneCollection.addToWhitelist(
        ZERO_ADDRESS, {"from": account})
    print(f"Attempting to whitelist {ZERO_ADDRESS}.")
    tx.wait(1)
    print("Success!")
    print(f"Minting Should be open for all.")
    return reneeLaneCollection


# ----------------------------- Main Function ------------------------------ #
def main():
    whitelist_zero_address()
