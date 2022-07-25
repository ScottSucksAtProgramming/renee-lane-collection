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
from brownie import accounts, config, ZERO_ADDRESS, Contract
from control_center import contract_functions
import pytest
from web3 import Web3
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
# Artist attempts to check their payouts balance. Sees they are owed money and
# retrieves their payment.

def load_contract():
    contract = Contract.from_explorer(
        "0xd732dEC77Bd7725C55A8325D762904876CE8aDB0")
    return contract


def test_artist_checks_payout_balance_and_withdraws_payment(load_wallets, contract=load_contract()):
    (wallets, owner_address, project_wallet_address, artist_1_address,
     artist_2_address, artist_3_address, artist_4_address,
     artist_5_address, investor_1_address, investor_2_address,
     investor_3_address, investor_4_address) = load_wallets

    amount_owed = get_amount_owed(artist_1_address, investor_2_address)
    current_balance = artist_1_address.balance()

    print(f"{artist_1_address} is owed {amount_owed} Ether.")
    print(
        f"Attempting to withdraw payment. Expected payment is {amount_owed}.")
    transaction = contract_functions.withdrawPayout(contract, artist_1_address)
    print("Withdrawal complete.")

    new_balance = artist_1_address.balance()

    assert new_balance == current_balance + amount_owed


def get_amount_owed(contract, artist_1_address, investor_2_address):
    amount = Web3.fromWei(
        contract_functions.payoutsOwed(contract, artist_1_address), "ether")

    if amount == 0:
        print(
            f"No payouts owed to {artist_1_address}. Sending purchase transaction.")
        purchase = contract_functions.purchaseArtwork(
            contract, 1, investor_2_address)
        print(f"Purchase complete.")
        amount = Web3.fromWei(
            contract_functions.payoutsOwed(contract, artist_1_address), 'ether')
    return amount
