#
#* ----------------------------- Documentation ------------------------------ #
# Module:  owner_whitelists_address_test.py
# Integration tests for the Renee Lane Collection Whitelist Functions.
#
# ! These tests are meant to be run all together and in order.
#
# User attempts to check their whitelist status (should return false). The
# Contract owner then whitelists that user's address. The user checks again
# and this time gets true. The owner then removes them from the whitelist.
# Finally the owner sets open minting by whitelisting the Zero Address.
#
# Modification History
# 07-17-2022 | SRK | Module Created

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from brownie import accounts, config, ZERO_ADDRESS, reverts
from yaml import load
from control_center import contract_functions
from scripts.helpful_scripts import get_account
import pytest
#* ------------------------------ Variables -------------------------------- #

#* ----------------------------- Fixtures ---------------------------------- #


@pytest.fixture
def load_wallets():
    """Will load all testing wallets as account objects in brownie."""

    passphrase = config["wallets"]["mnemonic"]

    wallets = accounts.from_mnemonic(passphrase, count=11)

    owner_address = wallets[0]
    project_wallet_address = wallets[1]

    artist_1_address = wallets[2]
    artist_2_address = wallets[3]
    artist_3_address = wallets[4]
    artist_4_address = wallets[5]
    artist_5_address = wallets[6]

    investor_1_address = wallets[7]
    investor_2_address = wallets[8]
    investor_3_address = wallets[9]
    investor_4_address = wallets[10]

    return (
        wallets, owner_address, project_wallet_address, artist_1_address,
        artist_2_address, artist_3_address, artist_4_address,
        artist_5_address, investor_1_address, investor_2_address,
        investor_3_address, investor_4_address
    )

#* ----------------------- Expected Use Case ------------------------------- #


def test_user_checks_their_whitelist_status(load_wallets):
    wallets = load_wallets

    user_account = wallets[7]

    whitelist_status = contract_functions.isWhitelisted(user_account)

    assert whitelist_status == False


def test_owner_adds_address_to_whitelist(load_wallets):
    wallets = load_wallets

    new_address = wallets[7]
    owner_address = wallets[0]

    if contract_functions.isWhitelisted(new_address) == True:
        return UserWarning("Address is already whitelisted")

    tx = contract_functions.addToWhitelist(new_address, owner_address)

    assert contract_functions.isWhitelisted(new_address) == True
    print(tx.info())


def test_user_checks_their_whitelist_status_success(load_wallets):
    wallets = load_wallets

    user_account = wallets[7]

    whitelist_status = contract_functions.isWhitelisted(user_account)

    assert whitelist_status == True


def test_owner_removes_address_from_whitelist(load_wallets):
    wallets = load_wallets
    new_address = wallets[7]
    owner_address = wallets[0]

    tx = contract_functions.removeFromWhitelist(new_address, owner_address)

    assert contract_functions.isWhitelisted(new_address) == False
    print(tx.info())


def test_owner_sets_open_minting(load_wallets):
    wallets = load_wallets
    new_address = wallets[10]
    owner_address = wallets[0]

    if not contract_functions.isWhitelisted(ZERO_ADDRESS):
        tx = contract_functions.addToWhitelist(ZERO_ADDRESS, owner_address)
        print(tx.info())

    with pytest.raises(ValueError):
        contract_functions.mintArtwork(900, new_address)
