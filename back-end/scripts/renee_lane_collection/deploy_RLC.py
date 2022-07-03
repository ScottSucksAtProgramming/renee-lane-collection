# ------------------------------ Documentation ------------------------------ #
# Module:  deploy_renee_coins.py
# This script will deploy the Renee Coins smart contract.
#
#
# Modification History
# 06-12-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #
from brownie import config, network, ReneeLaneCollection
from scripts.helpful_scripts import get_account


# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #
def deploy_contract():
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(
        f"The Renee Lane Collection contract has been deployed on the {[network.show_active()]} network."
    )
    print(f"The contract address is {reneeLaneCollection.address}")
    return reneeLaneCollection


# ----------------------------- Main Function ------------------------------ #
def main():
    deploy_contract()
