#
#* ----------------------------- Documentation ------------------------------ #
# Module: mint_and_transfer_test.py
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
from configparser import NoSectionError
from brownie import accounts, config, ZERO_ADDRESS
from control_center import contract_functions
import pytest
#* ------------------------------ Variables -------------------------------- #
token_id = None
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
# Todo: Investor mints 1st token.


def test_token_is_created_when_minted(load_wallets):
    global token_id
    (wallets, owner_address, project_wallet_address, artist_1_address,
        artist_2_address, artist_3_address, artist_4_address,
        artist_5_address, investor_1_address, investor_2_address,
        investor_3_address, investor_4_address) = load_wallets

    user_account = investor_1_address

    print(f"Attempting to mint token for {user_account}")
    transaction = contract_functions.mintArtwork(25, user_account)
    transaction.wait(1)
    print(f"Transaction Completed.")
    print(transaction.info())

    token_id = transaction.events["Transfer"]["tokenId"]

    print("Testing Token ID.")
    assert transaction.events["Transfer"]["tokenId"] > 0
    print("Testing token creator address.")
    assert transaction.events["Transfer"]["from"] == ZERO_ADDRESS
    print("Testing token owner address.")
    assert user_account == contract_functions.ownerOf(token_id)
    return (transaction, token_id)

# Todo: Investor 1 transfers token to Investor 2


def test_token_can_transfer(load_wallets):
    global token_id
    (wallets, owner_address, project_wallet_address, artist_1_address,
        artist_2_address, artist_3_address, artist_4_address,
        artist_5_address, investor_1_address, investor_2_address,
        investor_3_address, investor_4_address) = load_wallets

    sender = investor_1_address
    recipient = investor_2_address
    print(f"Attempting to transfer token {token_id} to {recipient}")

    transaction = contract_functions.safeTransferFrom(
        sender, recipient, token_id)
    transaction.wait(1)
    print(f"Transaction Completed.")
    print(transaction.info())

    token_id = transaction.events["Transfer"]["tokenId"]

    print("Testing that owner of token is set to new address.")
    assert recipient == contract_functions.ownerOf(token_id)

    return (transaction, token_id)
