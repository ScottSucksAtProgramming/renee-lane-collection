#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coin_contract_test.py
# This module contains the unit tests for the contract portion Renee Coins smart
# contract.
#
#
# Modification History
# 06-15-2022 | SRK | Module Created

# * -------------------------------- Tasks ----------------------------------- #


# * ------------------------------- Resources -------------------------------- #
from webbrowser import get
from scripts.deploy_renee_coins import deploy_contract
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeCoins, reverts

# * ------------------------------- Variables -------------------------------- #

# * ----------------------------- Contract Tests ---------------------------------- #
def test_contract_can_deploy():
    # Arrange
    account = get_account()
    # Act
    reneeCoins = ReneeCoins.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    starting_value = reneeCoins.totalSupply()
    expected = 0
    print(
        f"\nThe Renee Coins contract was deployed to: {reneeCoins.address}.\nThe total supply of Renee Coins is: {reneeCoins.totalSupply()}\n"
    )
    # Assert
    assert starting_value == expected
