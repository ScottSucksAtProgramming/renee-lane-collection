# ------------------------------ Documentation ------------------------------ #
# Module:  getBalance_RLC.py
# This script will get the balance of ether in the Renee Lane Collection smart
# contract. As well as the current payouts owed.
#
#
# Modification History
# 07-03-2022 | SRK | Module created.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #
from brownie import config, network, ReneeLaneCollection, ZERO_ADDRESS
from scripts.helpful_scripts import get_account
from web3 import Web3

# ------------------------------- Variables -------------------------------- #

# ----------------------------- Main Function ------------------------------ #


def main():
    artist_id_list = [_ for _ in range(1, 6)]
    address_dict = {}
    payouts_owed_dict = {}

    contract_current_balance = get_contract_balance()

    address_dict["The Owner"] = get_PROJECT_WALLET_ADDRESS()
    for artist_id in artist_id_list:
        address_dict[f"Artist {artist_id} "] = get_artist_direct_address(
            artist_id)
    for (artist, address) in address_dict.items():
        if artist == 0:
            payouts_owed_dict["Project Owner"] = get_payouts_owed(address)
        payouts_owed_dict[artist] = get_payouts_owed(address)
    print(f"The Contract Currently has {contract_current_balance} Ether.")
    print("-------------------------------------------\n")
    print_payouts(payouts_owed_dict, contract_current_balance)
    return artist_id_list, address_dict, contract_current_balance

# ------------------------------ Functions --------------------------------- #


def get_PROJECT_WALLET_ADDRESS() -> str:
    """returns the address of the project's wallet

    Returns:
        project_wallet_address (str): The address of the projects Wallet.
    """
    reneeLaneCollection = ReneeLaneCollection[-1]
    project_wallet_address = reneeLaneCollection.PROJECT_WALLET_ADDRESS()
    return project_wallet_address


def get_artist_direct_address(artist_id: int) -> str:
    """Returns the direct address of the artist specified by artist_id.

    Args:
        artist_id (int): The id of the artist (1-5)

    Returns:
        artist_direct_address str: _description_
    """
    reneeLaneCollection = ReneeLaneCollection[-1]
    artist_results = reneeLaneCollection.artist(artist_id)
    artist_direct_address = artist_results[0]
    return artist_direct_address


def get_contract_balance() -> int:
    """Returns the balance of the Renee Lane Collection smart contract.

    Returns: balance (int): The balance of the Renee Lane Collection
    smart contract."""
    reneeLaneCollection = ReneeLaneCollection[-1]
    balance = Web3.fromWei(reneeLaneCollection.getContractBalance(), "ether")
    return balance


def get_payouts_owed(direct_address) -> int:
    """Returns the payouts owed to the artist specified by direct_address.

    Args:
        direct_address (str): The direct address.

    Returns:
        payouts_owed (int): The payouts owed to the specified address.
    """
    reneeLaneCollection = ReneeLaneCollection[-1]
    payouts_owed = Web3.fromWei(
        reneeLaneCollection.payoutsOwed(direct_address), "ether")
    return payouts_owed


def print_payouts(payouts_owed_dict, contract_current_balance):
    for (artist, payouts_owed) in payouts_owed_dict.items():
        print(f"{artist} is owed: {payouts_owed} Ether.")


# ----------------------------- Tests ------------------------------ #
def test_can_build_artist_id_list():
    # Arrange
    # Act
    # Assert
    assert main()[0] == [1, 2, 3, 4, 5]


def test_can_build_address_dict():
    # Arrange
    # Act
    # Assert
    assert main()[1] != [None, None, None, None, None]


def test_returns_current_contract_balance():
    # Arrange
    # Act
    # Assert
    assert main()[2] >= 0
