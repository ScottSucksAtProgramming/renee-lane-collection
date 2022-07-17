#
#* ----------------------------- Documentation ------------------------------ #
# Module:  test_contract_Functions_RLC.py
# Unit tests for the contract_functions_RLC.py module.
#
#
# Modification History
# 07/03/2022 | SRK | Module Created.

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import ZERO_ADDRESS, ReneeLaneCollection, network, Contract
from web3 import Web3
from control_center import contract_functions
import pytest
#* ------------------------------ Variables -------------------------------- #

#* ------------------------------- Fixtures -------------------------------- #


@pytest.fixture
def load_contract():
    contract = Contract.from_explorer(
        "0xd732dEC77Bd7725C55A8325D762904876CE8aDB0")
    return contract


#* ------------------------------- Tests ----------------------------------- #

#* ----------------------------- Functions --------------------------------- #


def test_PROJECT_WALLET_ADDRESS_returns_address():
    # Arrange
    # Act
    # Assert
    assert contract_functions.PROJECT_WALLET_ADDRESS(
    ) != ZERO_ADDRESS


def test__artGallery_mapping_returns_dict():
    # Arrange
    # Act
    # Assert
    assert contract_functions.artGallery_mapping(40) != None


def test_artist_mapping_returns_addresses():
    # Arrange
    # Act
    # Assert
    assert contract_functions.artist_mapping(3) != None


def test_balanceOf_returns_number_of_tokens():
    # Arrange
    account = get_account()
    # Act
    # Assert
    assert contract_functions.balanceOf(account) != None


def test_getApproved_returns_address():
    # Arrange
    # Act
    # Assert
    assert contract_functions.getApproved(
        1) != None


def test_getContractBalance_returns_ether():
    # Arrange
    # Act
    # Assert
    assert contract_functions.getContractBalance() != None


def test_investorList_array_returns_array():
    # Arrange
    # Act
    # Assert
    assert contract_functions.investorList_array(0) != ZERO_ADDRESS


def test_isApprovedForAll_returns_bool():
    # Arrange
    # Act
    approval_status = contract_functions.isApprovedForAll(
        get_account(), get_account())
    # Assert
    assert approval_status == False or approval_status == True


def test_isInvestor_returns_bool():
    # Arrange
    # Act
    # Assert
    assert contract_functions.isInvestor(get_account(
    )) == True or contract_functions.isInvestor(get_account()) == False


def test_isWhitelisted_returns_bool():
    # Arrange
    # Act
    whitelist_status = contract_functions.isWhitelisted(get_account())
    # Assert
    assert whitelist_status == True or whitelist_status == False


def test_name_returns_string():
    # Arrange
    # Act
    # Assert
    assert contract_functions.name() != None


def test_owner_returns_address():
    # Arrange
    # Act
    # Assert
    assert contract_functions.owner() != ZERO_ADDRESS


def test_ownerOf_returns_string():
    # Arrange
    # Act
    # Assert
    assert contract_functions.ownerOf(1) != ZERO_ADDRESS


def test_PayoutsOwed_returns_int():
    # Arrange
    # Act
    # Assert
    assert contract_functions.payoutsOwed(
        contract_functions.artist_mapping(1)["Direct Address"]) != None


def test_printInvestorList_returns_list():
    # Arrange
    # Act
    # Assert
    assert contract_functions.printInvestorList() != None


def test_symbol_returns_string():
    # Arrange
    # Act
    # Assert
    assert contract_functions.symbol() != None


def test_tokenURI_returns_string():
    # Arrange
    # Act
    # Assert
    assert contract_functions.tokenURI(1) != None

#* ----------------------- Contract Write Functions ------------------------ #


def test_addToWhitelist_adds_correct_address():
    # Arrange
    new_address = get_account(7)

    # Act
    # Assert
    assert contract_functions.addToWhitelist(get_account()) == True
