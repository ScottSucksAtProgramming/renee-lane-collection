#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_collection_unit_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
#
# Modification History
# 05-31-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #
# Write Contract Tests - Completed (6/13/2022)
# Write Constructor Tests - Completed (6/14/2022)
# Todo: Write mintImage() Tests
# Todo: Write tokenURI() Tests
# Todo: Write isInvestor() Tests
# Todo: Write printInvestorList() Tests
# Todo: Write checkArtistBalances() Tests
# Todo: Write withdrawFunds() Tests
# Todo: Write forcePayment() Tests
# Todo: Write getImageInfo() Tests
# Todo: Write getContractBalance() Tests


# * ------------------------------- Resources ------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeLaneCollection, reverts
from brownie.test import given, strategy
from web3 import Web3
import gc, random, string, pytest

# * ------------------------------- Variables ------------------------------- #
letters = [string.ascii_letters, string.punctuation]


def generate_random_string():
    _string = "".join(random.choice(letters) for i in range(1, 3))
    return _string


PROJECT_WALLET_ADDRESS = 0xDD870FA1B7C4700F2BD7F44238821C26F7392148

# *  ------------------------ mintImage() Tests ---------------------------- #
# Todo: Test transaction reverts if _imageNumber is out of range.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.randint(51, 990),
        random.randint(51, 9990),
        random.randint(51, 9990),
    ],
)
def test_mintImage_reverts_when_imageNumber_is_out_of_range(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction reverts, test will pass.\n")
    # Act and Assert
    with reverts():
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})
    del _imageNumber
    gc.collect(generation=2)


# Todo: Test transaction reverts if _imageNumber is negative.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.randint(-9999, -1),
        random.randint(-9999, -1),
        random.randint(-9999, -1),
    ],
)
def test_mintImage_reverts_when_imageNumber_is_negative(_imageNumber):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with pytest.raises(OverflowError):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})
    del _imageNumber
    gc.collect(generation=2)


# Todo: Test transaction reverts if _imageNumber is a float.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.random(),
        random.random(),
        random.random(),
    ],
)
def test_mintImage_reverts_when_imageNumber_is_float(_imageNumber):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with reverts("The image you have selected does not exist in this collection."):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})
    gc.collect(generation=2)


# Todo: Test transaction reverts if _imageNumber is a string.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        generate_random_string(),
        generate_random_string(),
        generate_random_string(),
    ],
)
def test_mintImage_reverts_when_imageNumber_is_string(_imageNumber):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an TypeError, test will pass.\n")
    # Act and Assert
    with pytest.raises(TypeError):
        reneeLaneCollection.mintImage(_imageNumber, {"from": account})
    gc.collect(generation=2)


# Todo: Test _newTokenID is expected value based on _imageNumber parameter.
@pytest.mark.parametrize(
    "transactions",
    [
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10),
    ],
)
def test_newTokenID_is_set_correctly(transactions):
    # Arrange
    gc.collect()
    image = random.randint(1, 10)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    for i in range(transactions):
        reneeLaneCollection.mintImage(image, {"value": Web3.toWei(0.12, "ether")})
    # Act
    expected_tokenID = reneeLaneCollection.imageGallery(image)[2]
    tx_one = reneeLaneCollection.mintImage(image, {"value": Web3.toWei(0.12, "ether")})
    print(f"\nThe expected _newTokenID() is: {expected_tokenID}.")
    print(f"The returned _newTokenID() is: {tx_one.return_value[0]}.")
    # Assert
    assert tx_one.return_value[0] == expected_tokenID
    gc.collect(generation=2)


# Todo: Test transaction reverts if no more tokens are available.
def test_mintImage_reverts_if_no_more_tokens_available():
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    for i in range(20):
        reneeLaneCollection.mintImage(1, {"value": Web3.toWei(0.12, "ether")})
    minted_tokens = reneeLaneCollection.imageGallery(1)[2] - 1
    supply = reneeLaneCollection.imageGallery(1)[3]
    print(f"\nTokens minted for this image: {minted_tokens}/{supply}.")
    print(f"Attempting to mint one more token.")
    print(f"If this transaction reverts correctly, test will pass.\n")
    # Act and Assert
    with reverts("No more editions of this image are available."):
        reneeLaneCollection.mintImage(1, {"value": Web3.toWei(0.12, "ether")})
    gc.collect(generation=2)


# Todo: Test transaction reverts if msg.value isn't equal to price.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.randint(1, 50),
        random.randint(1, 50),
        random.randint(1, 50),
    ],
)
def test_mintImage_reverts_if_incorrect_value_sent(_imageNumber):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act and Asset
    with reverts("You didn't send the correct amount of Ether."):
        reneeLaneCollection.mintImage(_imageNumber, {"value": Web3.toWei(1, "ether")})
    gc.collect(generation=2)


# Todo: Test payouts owed to artist is adjusted correctly.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.randint(1, 50),
        random.randint(1, 50),
        random.randint(1, 50),
    ],
)
def test_artist_payout_calculated_correctly(_imageNumber):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    img_price = reneeLaneCollection.imageGallery(_imageNumber)[1]
    artist_id = reneeLaneCollection.imageGallery(_imageNumber)[4]
    artist_address = reneeLaneCollection.artist(artist_id)[0]
    expected_payout = img_price * 0.1
    # Act
    reneeLaneCollection.mintImage(_imageNumber, {"value": img_price})
    # Assert
    print(f"\nThe expected payout for this image is: {expected_payout}.")
    print(
        f"The returned payout for this image is: {reneeLaneCollection.payoutsOwed(artist_address)}.\n"
    )
    assert reneeLaneCollection.payoutsOwed(artist_address) == expected_payout


# Todo: Test payouts owed to project is adjusted correctly.
@pytest.mark.parametrize(
    "_imageNumber",
    [
        random.randint(1, 50),
        random.randint(1, 50),
        random.randint(1, 50),
    ],
)
def test_project_payout_calculated_correctly(_imageNumber):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    project_address = reneeLaneCollection.PROJECT_WALLET_ADDRESS()
    img_price = reneeLaneCollection.imageGallery(_imageNumber)[1]
    artist_payout = img_price * 0.1
    expected_payout = img_price - artist_payout
    # Act
    reneeLaneCollection.mintImage(_imageNumber, {"value": img_price})
    # Assert
    print(f"\nThe expected payout for this image is: {expected_payout}.")
    print(
        f"The returned payout for this image is: {reneeLaneCollection.payoutsOwed(project_address)}.\n"
    )
    assert reneeLaneCollection.payoutsOwed(project_address) == expected_payout


# Todo: Test that investors mapping is updated when address is not investor.
def test_investors_map_is_updated_if_minter_is_not_yet_an_investor():
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    investor_address = get_account(2)
    initial_investor_status = reneeLaneCollection.investors(investor_address)
    if initial_investor_status == True:
        return
    else:
        print(
            f"\nThe current investor status of {investor_address} is: {initial_investor_status}."
        )
        print(f"Minting token to {investor_address}.")
    # Act
    reneeLaneCollection.mintImage(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    print(
        f"The current investor status of {investor_address} is: {reneeLaneCollection.investors(investor_address)}"
    )
    # Assert
    assert reneeLaneCollection.investors(investor_address)


# Todo: Test that investorList is updated when address is not investor.
def test_investor_list_is_updated_if_minter_is_not_yet_an_investor(
    transactions=random.randint(0, 15), account_num=random.randint(2, 7)
):
    # Arrange
    gc.collect()
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    other_address = get_account(account_num)
    for i in range(transactions):
        reneeLaneCollection.mintImage(
            1, {"value": Web3.toWei(0.12, "ether"), "from": other_address}
        )
    investor_address = get_account(1)
    initial_investor_list = reneeLaneCollection.printInvestorList()
    print(f"\nThe starting investor list contains: {initial_investor_list}.")
    print(f"Minting token to {investor_address}.")
    # Act
    reneeLaneCollection.mintImage(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    print(
        f"The current investor list contains: {reneeLaneCollection.printInvestorList()}"
    )
    # Assert
    assert investor_address in reneeLaneCollection.printInvestorList()


# Todo: Test that investors mapping is not updated when address is already investor.
# Todo: Test that investorList is not updated when address is already investor.
# I don't know how to write these tests to show that there is less gas usage with this check. Don't think it's particularly important, but I might come back to this if I can find a way to have it compare the opCodes.

# Todo: Test that currentTokenID is incremented after successful mint.
def test_currentTokenID_increments_correctly(_imageNumber=random.randint(1, 50)):
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    price = reneeLaneCollection.imageGallery(_imageNumber)[1]
    if _imageNumber <= 20:
        transactions = random.randint(0, 17)
    elif _imageNumber <= 30:
        transactions = random.randint(0, 7)
    elif _imageNumber <= 40:
        transactions = random.randint(0, 3)
    else:
        transactions = random.randint(0, 2)
    for i in range(transactions):
        reneeLaneCollection.mintImage(_imageNumber, {"value": price, "from": account})
    original_tokenID = reneeLaneCollection.imageGallery(_imageNumber)[2]
    # Act
    reneeLaneCollection.mintImage(_imageNumber, {"value": price, "from": account})
    currentTokenID = reneeLaneCollection.imageGallery(_imageNumber)[2]
    print(f"\nThe expected new currentTokenID is: {original_tokenID+1}.")
    print(f"The returned new currentTokenID is: {currentTokenID}.\n")
    # Assert
    assert currentTokenID == original_tokenID + 1


# Todo: Test that currentTokenID is not incremented if transaction reverts.
def test_currentTokenID_does_not_increment_if_transaction_reverts(
    _imageNumber=random.randint(1, 50)
):
    # Arrange
    gc.collect(generation=2)
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    price = reneeLaneCollection.imageGallery(_imageNumber)[1]
    if _imageNumber <= 20:
        transactions = random.randint(0, 17)
    elif _imageNumber <= 30:
        transactions = random.randint(0, 7)
    elif _imageNumber <= 40:
        transactions = random.randint(0, 3)
    else:
        transactions = random.randint(0, 2)
    for i in range(transactions):
        reneeLaneCollection.mintImage(_imageNumber, {"value": price, "from": account})
    original_tokenID = reneeLaneCollection.imageGallery(_imageNumber)[2]
    # Act
    with reverts("You didn't send the correct amount of Ether."):
        reneeLaneCollection.mintImage(
            _imageNumber, {"value": price + 1, "from": account}
        )
    currentTokenID = reneeLaneCollection.imageGallery(_imageNumber)[2]
    print(f"\nThe expected new currentTokenID is: {original_tokenID}.")
    print(f"The returned new currentTokenID is: {currentTokenID}.\n")
    # Assert
    assert currentTokenID == original_tokenID
