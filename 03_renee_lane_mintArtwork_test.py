#
# * ------------------------------ Documentation ---------------------------- #
# Module:  renee_lane_collection_unit_test.py
# This module contains all the unit tests for mintArtwork() function in The
# Renee Lane Collection smart contract.
#
#
# Modification History
# 06-17-22 | SRK | Module Created

# * -------------------------------- Tasks ---------------------------------- #

# * ------------------------------- Resources ------------------------------- #
from scripts.helpful_scripts import get_account, characters
from brownie import ReneeLaneCollection, reverts
from web3 import Web3
import gc, random, string, pytest

# * ------------------------------- Variables ------------------------------- #


def generate_random_string():
    _string = "".join(random.choice(characters) for i in range(1, 15))
    return _string


# *  ------------------------ mintArtwork() Tests ---------------------------- #
# Todo: Test transaction reverts if _imageNumber is out of range.
def test_mintImage_reverts_when_imageNumber_is_out_of_range(
    _imageNumber=random.randint(51, 9990)
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction reverts, test will pass.\n")
    # Act and Assert
    with reverts():
        reneeLaneCollection.mintArtwork(_imageNumber, {"from": account})
    del _imageNumber


# Todo: Test transaction reverts if _imageNumber is negative.
def test_mintImage_reverts_when_imageNumber_is_negative(
    _imageNumber=random.randint(-9999, -1)
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with pytest.raises(OverflowError):
        reneeLaneCollection.mintArtwork(_imageNumber, {"from": account})
    del _imageNumber


# Todo: Test transaction reverts if _imageNumber is a float.
def test_mintImage_reverts_when_imageNumber_is_float(_imageNumber=random.random()):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an OverflowError, test will pass.\n")
    # Act and Assert
    with reverts("The image you have selected does not exist in this collection."):
        reneeLaneCollection.mintArtwork(_imageNumber, {"from": account})


# Todo: Test transaction reverts if _imageNumber is a string.
def test_mintImage_reverts_when_imageNumber_is_string(
    _imageNumber=generate_random_string(),
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    print(f"\nAttempting to mint imageNumber: {_imageNumber}.")
    print(f"If this transaction raises an TypeError, test will pass.\n")
    # Act and Assert
    with pytest.raises(TypeError):
        reneeLaneCollection.mintArtwork(_imageNumber, {"from": account})


# Todo: Test transaction reverts if no more tokens are available.
def test_mintImage_reverts_if_no_more_tokens_available():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    for i in range(20):
        reneeLaneCollection.mintArtwork(1, {"value": Web3.toWei(0.12, "ether")})
    minted_tokens = reneeLaneCollection.artGallery(1)[2] - 1
    supply = reneeLaneCollection.artGallery(1)[3]
    print(f"\nTokens minted for this image: {minted_tokens}/{supply}.")
    print(f"Attempting to mint one more token.")
    print(f"If this transaction reverts correctly, test will pass.\n")
    # Act and Assert
    with reverts("No more editions of this image are available."):
        reneeLaneCollection.mintArtwork(1, {"value": Web3.toWei(0.12, "ether")})


# Todo: Test transaction reverts if msg.value isn't equal to price.
def test_mintImage_reverts_if_incorrect_value_sent(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    # Act and Asset
    with reverts("You didn't send the correct amount of Ether."):
        reneeLaneCollection.mintArtwork(_imageNumber, {"value": Web3.toWei(1, "ether")})


# Todo: Test payouts owed to artist is adjusted correctly.
def test_artist_payout_calculated_correctly(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    img_price = reneeLaneCollection.artGallery(_imageNumber)[1]
    artist_id = reneeLaneCollection.artGallery(_imageNumber)[4]
    artist_address = reneeLaneCollection.artist(artist_id)[0]
    expected_payout = img_price * 0.1
    # Act
    reneeLaneCollection.mintArtwork(_imageNumber, {"value": img_price})
    # Assert
    print(f"\nThe expected payout for this image is: {expected_payout}.")
    print(
        f"The returned payout for this image is: {reneeLaneCollection.payoutsOwed(artist_address)}.\n"
    )
    assert reneeLaneCollection.payoutsOwed(artist_address) == expected_payout


# Todo: Test payouts owed to project is adjusted correctly.
def test_project_payout_calculated_correctly(
    _imageNumber=random.randint(1, 50),
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    project_address = reneeLaneCollection.PROJECT_WALLET_ADDRESS()
    img_price = reneeLaneCollection.artGallery(_imageNumber)[1]
    artist_payout = img_price * 0.1
    expected_payout = img_price - artist_payout
    # Act
    reneeLaneCollection.mintArtwork(_imageNumber, {"value": img_price})
    # Assert
    print(f"\nThe expected payout for this image is: {expected_payout}.")
    print(
        f"The returned payout for this image is: {reneeLaneCollection.payoutsOwed(project_address)}.\n"
    )
    assert reneeLaneCollection.payoutsOwed(project_address) == expected_payout


# Todo: Test that investors mapping is updated when address is not investor.
def test_investors_map_is_updated_if_minter_is_not_yet_an_investor():
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    investor_address = get_account(2)
    initial_investor_status = reneeLaneCollection.isInvestor(investor_address)
    if initial_investor_status == True:
        return
    else:
        print(
            f"\nThe current investor status of {investor_address} is: {initial_investor_status}."
        )
        print(f"Minting token to {investor_address}.")
    # Act
    reneeLaneCollection.mintArtwork(
        1, {"value": Web3.toWei(0.12, "ether"), "from": investor_address}
    )
    print(
        f"The current investor status of {investor_address} is: {reneeLaneCollection.isInvestor(investor_address)}"
    )
    # Assert
    assert reneeLaneCollection.isInvestor(investor_address)


# Todo: Test that investorList is updated when address is not investor.
def test_investor_list_is_updated_if_minter_is_not_yet_an_investor(
    transactions=random.randint(0, 15), account_num=random.randint(2, 7)
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    other_address = get_account(account_num)
    for i in range(transactions):
        reneeLaneCollection.mintArtwork(
            1, {"value": Web3.toWei(0.12, "ether"), "from": other_address}
        )
    investor_address = get_account(1)
    initial_investor_list = reneeLaneCollection.printInvestorList()
    print(f"\nThe starting investor list contains: {initial_investor_list}.")
    print(f"Minting token to {investor_address}.")
    # Act
    reneeLaneCollection.mintArtwork(
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
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    if _imageNumber <= 20:
        transactions = random.randint(0, 17)
    elif _imageNumber <= 30:
        transactions = random.randint(0, 7)
    elif _imageNumber <= 40:
        transactions = random.randint(0, 3)
    else:
        transactions = random.randint(0, 2)
    for i in range(transactions):
        reneeLaneCollection.mintArtwork(_imageNumber, {"value": price, "from": account})
    original_tokenID = reneeLaneCollection.artGallery(_imageNumber)[2]
    # Act
    reneeLaneCollection.mintArtwork(_imageNumber, {"value": price, "from": account})
    currentTokenID = reneeLaneCollection.artGallery(_imageNumber)[2]
    print(f"\nThe expected new currentTokenID is: {original_tokenID+1}.")
    print(f"The returned new currentTokenID is: {currentTokenID}.\n")
    # Assert
    assert currentTokenID == original_tokenID + 1


# Todo: Test that currentTokenID is not incremented if transaction reverts.
def test_currentTokenID_does_not_increment_if_transaction_reverts(
    _imageNumber=random.randint(1, 50)
):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    if _imageNumber <= 20:
        transactions = random.randint(0, 17)
    elif _imageNumber <= 30:
        transactions = random.randint(0, 7)
    elif _imageNumber <= 40:
        transactions = random.randint(0, 3)
    else:
        transactions = random.randint(0, 2)
    for i in range(transactions):
        reneeLaneCollection.mintArtwork(_imageNumber, {"value": price, "from": account})
    original_tokenID = reneeLaneCollection.artGallery(_imageNumber)[2]
    # Act
    with reverts("You didn't send the correct amount of Ether."):
        reneeLaneCollection.mintArtwork(
            _imageNumber, {"value": price + 1, "from": account}
        )
    currentTokenID = reneeLaneCollection.artGallery(_imageNumber)[2]
    print(f"\nThe expected new currentTokenID is: {original_tokenID}.")
    print(f"The returned new currentTokenID is: {currentTokenID}.\n")
    # Assert
    assert currentTokenID == original_tokenID


# *  --------------------------- Token Tests ------------------------------- #
# Todo: Test that tokens are minted to the correct owner.
def test_token_is_minted_to_expected_owner(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    minter_account = get_account(random.randint(1, 9))
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    # Act
    tx = reneeLaneCollection.mintArtwork(
        _imageNumber, {"value": price, "from": minter_account}
    )
    token_ID = tx.events["Transfer"]["tokenId"]
    owner_of_token = reneeLaneCollection.ownerOf(token_ID)
    print(f"\nThe expected owner of {token_ID} is: {minter_account}.")
    print(f"The returned owner of {token_ID} is: {owner_of_token}.\n")
    # Assert
    assert owner_of_token == minter_account


# Todo: Test that tokens are given the expected tokenID.
def test_token_is_minted_to_with_correct_tokenID(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    minter_account = get_account(random.randint(1, 9))
    expected_token_ID = reneeLaneCollection.artGallery(_imageNumber)[2]
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    # Act
    tx = reneeLaneCollection.mintArtwork(
        _imageNumber, {"value": price, "from": minter_account}
    )
    actual_token_ID = tx.events["Transfer"]["tokenId"]
    print(f"\nThe expected tokenID is: {expected_token_ID}.")
    print(f"The returned tokenID is: {actual_token_ID}.\n")
    # Assert
    assert expected_token_ID == actual_token_ID


# Todo: Test that tokens are given the correct tokenURI.
def test_token_URI_is_set_correctly(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    minter_account = get_account(random.randint(1, 9))
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    token_ID = reneeLaneCollection.artGallery(_imageNumber)[2]
    expected_URI = f"https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/{token_ID}.json"
    # Act
    tx = reneeLaneCollection.mintArtwork(
        _imageNumber, {"value": price, "from": minter_account}
    )
    actual_URI = reneeLaneCollection.tokenURI(token_ID)
    print(f"\nThe expected tokenURI is: {expected_URI}.")
    print(f"The returned tokenURI is: {actual_URI}.\n")
    # Assert
    assert expected_URI == actual_URI


# Todo: Test that tokens are given the correct Royalty Payout Address.
def test_token_royalty_address_is_set_correctly(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    minter_account = get_account(random.randint(1, 9))
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    token_ID = reneeLaneCollection.artGallery(_imageNumber)[2]
    artist_ID = reneeLaneCollection.artGallery(_imageNumber)[4]
    expected_address = reneeLaneCollection.artist(artist_ID)[1]
    secondary_sale_price = Web3.toWei(1, "ether")
    # Act
    tx = reneeLaneCollection.mintArtwork(
        _imageNumber, {"value": price, "from": minter_account}
    )
    actual_address = reneeLaneCollection.royaltyInfo(token_ID, secondary_sale_price)[0]
    print(f"\nThe expected royalty address is: {expected_address}.")
    print(f"The returned royalty address is: {actual_address}.\n")
    # Assert
    assert expected_address == actual_address


# Todo: Test that tokens are given the correct Royalty Basis Points.
def test_token_royalty_address_is_set_correctly(_imageNumber=random.randint(1, 50)):
    # Arrange
    account = get_account()
    reneeLaneCollection = ReneeLaneCollection.deploy({"from": account})
    minter_account = get_account(random.randint(1, 9))
    price = reneeLaneCollection.artGallery(_imageNumber)[1]
    token_ID = reneeLaneCollection.artGallery(_imageNumber)[2]
    artist_ID = reneeLaneCollection.artGallery(_imageNumber)[4]
    secondary_sale_price = Web3.toWei(0.5, "ether")
    expected_royalty_amount = secondary_sale_price * 0.10
    # Act
    tx = reneeLaneCollection.mintArtwork(
        _imageNumber, {"value": price, "from": minter_account}
    )
    actual_royalty_amount = reneeLaneCollection.royaltyInfo(
        token_ID, secondary_sale_price
    )[1]
    print(f"\nThe expected royalty amount is: {expected_royalty_amount}.")
    print(f"The returned royalty amount is: {actual_royalty_amount}.\n")
    # Assert
    assert expected_royalty_amount == actual_royalty_amount
