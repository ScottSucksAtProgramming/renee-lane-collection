#
# * ------------------------------ Documentation --------------------------- #
#
# Module:  09_renee_count_burn_test.py
# This module contains the unit tests for the ERC-20 transfer behavior of the
# Renee Coins contract.
#
#
# Modification History
# 06-26-2022 | SRK | Module Created
# 06-28-2022 | SRK | Tests and documentation updated.

# * -------------------------------- Tasks --------------------------------- #
# * Expected Behaviors:
# ✓ Tests setup is complete.
# ✓ Token owner can burn tokens.
# ✓ Burn reverts if balance below amount.
# ✓ Burn logs are correct.
# ✓ BurnFrom can burn tokens from approved address.
# ✓ BurnFrom reverts if spender not approved.
# ✓ BurnFrom logs are correct.

# * ------------------------------- Resources ------------------------------ #
from scripts.helpful_scripts import get_account
from brownie import ReneeCoins, reverts, ZERO_ADDRESS

# * ------------------------------- Variables ------------------------------ #
deployer_account = get_account()
contractObject = ReneeCoins

# * ---------------------------- Burn Functions ---------------------------- #


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


def test_token_owner_can_burn_tokens():
    """Test to see if owner of tokens can burn tokens. Test will pass if
    balance of owner and total supply are reduced by 5."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act
    amount_to_be_burnt = 5
    contract.burn(amount_to_be_burnt)
    # Assert
    assert contract.balanceOf(
        deployer_account) == 95 and contract.totalSupply() == 95


def test_burn_reverts_if_balance_below_amount():
    """Test to see if burn reverts if burn amount greater than balance owned.
    Test will pass if transaction reverts."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act
    amount_to_be_burnt = 200
    with reverts("ERC20: burn amount exceeds balance"):
        contract.burn(amount_to_be_burnt)


def test_burn_logs_from_correctly():
    """Test to see if burn logs from address correctly. Test will pass if log
    from address is correct."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burn(amount_to_be_burnt)
    # Assert
    assert expected_from == tx.events["Transfer"]["from"]


def test_burn_logs_to_correctly():
    """Test to see if burn logs to address correctly. Test will pass if log
    to address is correct."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burn(amount_to_be_burnt)
    # Assert
    assert expected_to == tx.events["Transfer"]["to"]


def test_burn_logs_value_correctly():
    """Test to see if burn logs value correctly. Test will pass if log
    value is correct."""
    # Arrange
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burn(amount_to_be_burnt)
    # Assert
    assert expected_value == tx.events["Transfer"]["value"]


def test_spender_can_burnFrom_approved_tokens():
    """Test to see if spender can burnFrom approved tokens. Test will pass if 
    balance of token owner and total supply are reduced by 10."""
    # Arrange
    spender = get_account(1)
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    contract.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    contract.burnFrom(deployer_account, amount_to_be_burnt, {"from": spender})
    # Assert
    assert contract.balanceOf(
        deployer_account) == 90 and contract.totalSupply() == 90


def test_burnFrom_reverts_if_spender_not_approved():
    """Tests to see if account can call burnFrom if not approve. Test will
    pass if transaction reverts."""
    # Arrange
    spender = get_account(1)
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    # Act and Assert
    amount_to_be_burnt = 10
    with reverts("ERC20: insufficient allowance"):
        contract.burnFrom(deployer_account,
                          amount_to_be_burnt, {"from": spender})


def test_burnFrom_logs_from_correctly():
    """Test to see if burnFrom logs from address correctly. Test will pass if log
    from address is correct."""
    # Arrange
    spender = get_account(1)
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    contract.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burnFrom(
        deployer_account, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_from == tx.events["Transfer"]["from"]


def test_burnFrom_logs_to_correctly():
    """Test to see if burnFrom logs to address correctly. Test will pass if log
    to address is correct."""
    # Arrange
    spender = get_account(1)
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    contract.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burnFrom(
        deployer_account, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_to == tx.events["Transfer"]["to"]


def test_burnFrom_logs_value_correctly():
    """Test to see if burnFrom logs value correctly. Test will pass if log
    value is correct."""
    # Arrange
    spender = get_account(1)
    contract = contractObject.deploy({"from": deployer_account})
    contract.createCoins(100)
    contract.approve(spender, 10)
    # Act
    amount_to_be_burnt = 10
    expected_to = ZERO_ADDRESS
    expected_from = deployer_account
    expected_value = amount_to_be_burnt
    tx = contract.burnFrom(
        deployer_account, amount_to_be_burnt, {"from": spender})
    # Assert
    assert expected_value == tx.events["Transfer"]["value"]
