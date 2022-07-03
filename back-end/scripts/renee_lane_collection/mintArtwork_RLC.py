# ------------------------------ Documentation ------------------------------ #
# Module:  deploy_renee_coins.py
# This script will deploy the Renee Coins smart contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #
from brownie import config, network, ReneeLaneCollection
from scripts.helpful_scripts import get_account
from web3 import Web3


# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #
def get_price(image_number):
    reneeLaneCollection = ReneeLaneCollection[-1]
    price = reneeLaneCollection.artGallery(image_number)[1]
    return price


def mint_artwork(image_number):
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection[-1]
    price = get_price(image_number)
    tx = reneeLaneCollection.mintArtwork(
        image_number, {"value": price, "from": account})
    print(f"Attempting to Mint Art Piece.")
    tx.wait(1)
    print("Art Piece Minted!")
    print(tx.info())
    return reneeLaneCollection


# ----------------------------- Main Function ------------------------------ #
def main():
    image_number = int(input("Which Image (1-50) would you like to mint? "))
    print(
        f"The Price of your Art Piece is: {Web3.fromWei(get_price(image_number), 'ether')} Ether.")
    decision = input("Would you like to mint your Art Piece? (y/n) ")
    if decision == "y":
        mint_artwork(image_number)
    else:
        print("Exiting...")
        exit()
