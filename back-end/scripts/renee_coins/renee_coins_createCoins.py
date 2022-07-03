# ------------------------------ Documentation ------------------------------ #
# Module:  deploy_renee_coins.py
# This script will deploy the Renee Coins smart contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #
from brownie import config, network, ReneeCoins
from scripts.helpful_scripts import get_account


# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #
def create_coins():
    account = get_account()
    reneeCoins = ReneeCoins[-1]
    reneeCoins.createCoins(int(input("How many Renee Coins would you like to create? ")), {"from": account})
    print(f"Creating Renee Coins in your wallet.")
    print(f"Your current balance of Renee Coins is {reneeCoins.balanceOf(account)} RC.")
    return reneeCoins


# ----------------------------- Main Function ------------------------------ #
def main():
    create_coins()
