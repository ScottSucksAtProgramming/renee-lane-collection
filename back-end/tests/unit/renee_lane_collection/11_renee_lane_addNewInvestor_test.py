#
# * ------------------------------ Documentation ---------------------------- #
# Module:  11_renee_lane_addNewInvestor_test.py
# This module contains all the unit tests for addNewInvestor() function in The
# Renee Lane Collection smart contract.
#
#
# Modification History
# 06-29-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# * Expected Behaviors:
# ✓ Test addNewInvestor() function updates investor mapping for new investors.
# ✓ Test addNewInvestor() function updates investor list for new investors.
# ✓ Test AddNewInvestor() function not called if address already an investor.
# ✓ Test addNewInvestor() function logs correctly.


# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account, generate_random_string
from brownie import ZERO_ADDRESS, ReneeLaneCollection, reverts
from web3 import Web3
import pytest

# * ------------------------------- Variables ------------------------------ #


@pytest.fixture
def contract_setup_with_open_minting():
    """Setup for the contract. Whitelists the Zero address."""
    deployer_account = get_account()
    contract = ReneeLaneCollection.deploy(
        {"from": deployer_account})
    contract.addToWhitelist(ZERO_ADDRESS)
    return contract
# *  ---------------------- addNewInvestor() Tests -------------------------- #


def test_investors_map_is_updated_if_minter_is_not_yet_an_investor(contract_setup_with_open_minting):
    """Tests to see if the investors map is updated if the minter is not yet
    on the list. Test will pass if the minter address is not in mapping
    before transaction and is successfully added to the investor mapping
    after transaction complete."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()

    investor_address = get_account(2)
    initial_investor_status = contract.isInvestor(investor_address)
    if initial_investor_status == True:
        assert False
    # Act
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    # Assert
    assert initial_investor_status == False and contract.isInvestor(
        investor_address)


def test_investor_list_is_updated_if_minter_is_not_yet_an_investor(contract_setup_with_open_minting):
    """Tests to see if the investor list is updated if the minter is not yet
    an investor. Test will pass if investor address is not in list before
    transaction and is successfully added to the investor list after
    transaction is complete."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()

    other_address = get_account(7)
    investor_address = get_account(1)
    for i in range(2):
        contract.mintArtwork(
            1, {"value": Web3.toWei(0.12, "ether"), "from": other_address}
        )
    initial_investor_list = contract.printInvestorList()
    # Act
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    # Assert
    assert (investor_address not in initial_investor_list) and (
        investor_address in contract.printInvestorList())


def test_investor_not_added_if_already_an_investor(contract_setup_with_open_minting):
    """Tests to see if the addNewInvestor() function is called if the minter 
    is already an investor. Test will pass if minter address returns true in 
    mapping and if no NewInvestorAdded event is emitted."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()

    investor_address = get_account(2)
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    initial_investor_status = contract.isInvestor(investor_address)
    if initial_investor_status == False:
        assert False
    # Act
    tx = contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    # Assert
    assert (
        initial_investor_status == True
    ) and (
        "NewInvestorAdded" not in tx.events
    )


def test_NewInvestorAdded_event_is_emitted_when_addNewInvestor_is_called(contract_setup_with_open_minting):
    """Tests to see if the addNewInvestor function correctly emits the
    NewInvestorAdded event."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()

    investor_address = get_account(2)
    initial_investor_status = contract.isInvestor(investor_address)
    if initial_investor_status == True:
        assert False
    # Act
    tx = contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    # Assert
    assert "NewInvestorAdded" in tx.events


def test_addNewInvestor_logs_investor_address_correctly(contract_setup_with_open_minting):
    """Tests to see if the addNewInvestor function correctly emits the
    NewInvestorAdded event."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()

    investor_address = get_account(2)
    initial_investor_status = contract.isInvestor(investor_address)
    if initial_investor_status == True:
        assert False
    # Act
    tx = contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    loggedAddress = tx.events["NewInvestorAdded"]["investorAddress"]
    # Assert
    assert investor_address == loggedAddress


def test_addNewInvestor_logs_tokenID_correctly(contract_setup_with_open_minting):
    """Tests to see if the addNewInvestor function correctly emits the
    NewInvestorAdded event."""
    # Arrange
    contract = contract_setup_with_open_minting
    deployer_account = get_account()
    investor_address = get_account(2)
    expected_tokenId = "3"

    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": deployer_account}
    )
    contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": deployer_account}
    )
    initial_investor_status = contract.isInvestor(investor_address)
    if initial_investor_status == True:
        assert False
    # Act
    tx = contract.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    loggedTokenID = tx.events["NewInvestorAdded"]["tokenID"]
    # Assert
    assert expected_tokenId == loggedTokenID
