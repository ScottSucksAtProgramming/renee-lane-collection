#
#* ----------------------------- Documentation ------------------------------ #
# Module:  owner_whitelists_address_test.py
# DESCRIPTION
#
#
# Modification History
# 07-17-2022 | SRK | Module Created

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from brownie import accounts, config
from control_center import contract_functions
from scripts.helpful_scripts import get_account
import pytest
#* ------------------------------ Variables -------------------------------- #
INVESTOR_ONE_ACCOUNT = get_account(id="investorOne")
INVESTOR_TWO_ACCOUNT = get_account(id="investorTwo")
INVESTOR_THREE_ACCOUNT = get_account(id="investorThree")
INVESTOR_FOUR_ACCOUNT = get_account(id="investorFour")
OWNER_ACCOUNT = get_account()
#* ---------------------------- Main Function ------------------------------ #


def main():
    wallets = load_wallets()
    print(wallets[0])

    #* ----------------------------- Expected Use Cases --------------------------------- #


def load_wallets():
    """Will load all testing wallets as account objects in brownie."""

    passphrase = config["wallets"]["mnemonic"]

    wallets = accounts.from_mnemonic(passphrase, count=11)

    return wallets
