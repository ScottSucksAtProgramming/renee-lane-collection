#
# * ------------------------------ Documentation ------------------------------ #
#
# Module:  renee_coins_airDropCoins_test.py
# This module contains the unit tests for the airdropCoins() function of the
# Renee Coins smart contract.
#
# Modification History
# 06-15-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks ----------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ airdropCoins() can only be called by the owner.
# ✓ airdropCoins() mints the correct amount of Renee Coins.
# ✓ airdropCoins() mints to the correct wallet.
# ✓ airdropCoins() cannot exceed the cap.

# * ------------------------------- Resources -------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts

# * ------------------------------- Variables -------------------------------- #
deployer_account = get_account()
contractObject = ReneeCoins

# * ------------------------- airdropCoins() Tests --------------------------- #


def test_tests_are_set_up():
    """Tests to see if the tests are set up correctly."""
    # Arrange
    if deployer_account == None:
        raise Exception("Deployer account is not set.")
    if contractObject == None:
        raise Exception("Contract object is not set.")
    # Act
    # Assert
    assert True


def test_airDropCoins_can_only_called_by_owner():
    """Test to see if airdropCoins() can only be called by the owner. Test 
    will pass if transaction called by not_owner reverts."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    not_owner = get_account(1)
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        reneeCoins.airdropCoins(
            not_owner,
            10_000,
            {"from": not_owner}
        )


def test_airdropCoins_mints_amount_expected():
    """Test to see if airdropCoins() mints the correct amount of Renee 
    Coins. Test will pass if total supply of Renee Coins is equal to amount 
    airDropped."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    # Act
    expected_amount = 10_000
    recipient_account = get_account(1)
    reneeCoins.airdropCoins(
        recipient_account,
        expected_amount,
        {"from": deployer_account}
    )
    # Assert
    assert reneeCoins.totalSupply() == expected_amount


def test_airdropCoins_mints_to_correct_wallet():
    """Test to see if airdropCoins() mints to the correct wallet. Test will 
    pass if balance of Renee Coins in recipient's wallet is equal to amount 
    airDropped."""
    # Arrange
    reneeCoins = ReneeCoins.deploy({"from": deployer_account})
    # Act
    expected_amount = 50_000
    recipient = get_account(1)
    reneeCoins.airdropCoins(
        recipient,
        expected_amount,
        {"from": deployer_account}
    )
    # Assert
    assert reneeCoins.balanceOf(recipient) == expected_amount


def test_airdropCoins_cannot_exceed_cap():
    """Test to see if airdropCoins() cannot exceed the cap. Test will pass if 
    transaction trying to mint Renee Coins exceeds the cap."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    expected_amount = 2_000_000
    additional_amount = 100
    recipient = get_account(1)
    contract.createCoins(expected_amount, {"from": deployer_account})
    # Act and Assert
    with reverts("ERC20Capped: cap exceeded"):
        contract.airdropCoins(
            recipient,
            additional_amount,
            {"from": deployer_account}
        )
