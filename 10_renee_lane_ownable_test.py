# ------------------------------ Documentation ------------------------------ #
# Module:  NAME.py
# DESCRIPTION
#
#
# Modification History
# DATE INITIAL UPDATE.

# -------------------------------- Tasks ----------------------------------- #

# ------------------------------- Resources -------------------------------- #

# ------------------------------- Variables -------------------------------- #

# ------------------------------ Functions --------------------------------- #

# ----------------------------- Main Function ------------------------------ #


def test_owner_returns_expected_value():
    # Arrange
    owner = get_account()
    # Act
    contract = ReneeCoins.deploy({"from": owner})
    # Assert
    assert contract.owner() == owner


def test_owner_can_renounceOwnership():
    # Arrange
    owner = get_account()
    contract = ReneeCoins.deploy({"from": owner})
    # Act
    contract.renounceOwnership()
    # Assert
    assert contract.owner() == ZERO_ADDRESS


def test_renounceOwnership_can_only_be_called_by_owner():
    # Arrange
    owner = get_account()
    contract = ReneeCoins.deploy({"from": owner})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.renounceOwnership({"from": get_account(2)})


def test_owner_can_transferOwnership():
    # Arrange
    owner = get_account()
    new_owner = get_account(1)
    contract = ReneeCoins.deploy({"from": owner})
    # Act
    contract.transferOwnership(get_account(1))
    # Assert
    assert contract.owner() == new_owner


def test_transferOwnership_can_only_be_called_by_owner():
    # Arrange
    owner = get_account()
    contract = ReneeCoins.deploy({"from": owner})
    # Act and Assert
    with reverts("Ownable: caller is not the owner"):
        contract.transferOwnership(get_account(7), {"from": get_account(2)})
