#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  renee_coins_decimals_test.py
# This module contains the unit tests for the decimals() function of the Renee
# Coins smart contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks --------------------------------- #


# * ------------------------------- Resources ------------------------------ #
from webbrowser import get
from scripts.deploy_renee_coins import deploy_renee_coins
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts
import gc

# * ------------------------------- Variables ------------------------------ #

# * ------------------------ decimals() Function --------------------------- #
def test_decimals_is_set_correctly():
    # Arrange and Act
    gc.collect(generation=2)
    account = get_account()
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    expected_decimals = 0
    print(f"\nExpected decimals: {expected_decimals}.")
    print(f"Actual decimals:   {reneeCoins.decimals()}.\n")
    # Assert
    assert expected_decimals == reneeCoins.decimals()
    gc.collect(generation=2)
