# ------------------------------ Documentation ------------------------------ #
# Module:  renee_lane_collection_unit_test.py
# This module contains all the unit tests for The Renee Lane Collection smart
# contracts.
#
#
# Modification History
# 05-31-22 | SRK | Module Created

# -------------------------------- Tasks ----------------------------------- #
# TODO: Write test to ensure functions of ERC721 are available on this contract.
# TODO: Write test to ensure functions of ERC721Royalty are available on this contract.
# TODO: Write test to ensure functions of Ownble are available on this contract.
# TODO: Write a test that confirms the collection `name` is set correctly.
# TODO: Write a test that confirms that the collection `symbol` is set correctly.
# TODO: Write a test that confirms that the `imgNumber` is set correctly for all tokens.
# TODO: Write a test that confirms that the `price` is set correctly for all tokens.
# TODO: Write a test that confirms that the `currentTokenId` is set correctly for all tokens.
# TODO: Write a test that confirms that the `lastTokenId` is set correctly for all tokens.
# TODO: Write a test that confirms that the `mintingPayoutAddress` is set correctly for all tokens.
# TODO: Write a test that confirms that the `royaltyPayoutAddress` is set correctly for all tokens.
# TODO: Write a test that confirms the number passed to the function is the number that is used to for minting. (This is probably better done as an integration test with the frontend.)
# TODO: Write a test to confirm the minting function will revert if the image number passed is out side of the range (1-50).
# TODO: Write a test that confirms that `imageGallery[_imageNumber].currentTokenId` and `_newTokenId` are the same.
# TODO: Write a test that confirms that the minting function will revert  if `_newTokenId` is greater than `imageGallery[_imageNumber].lastTokenId`.
# TODO: Write a test that confirms that the minting function will revert if `msg.value` is less than `imageGallery[_imageNumber].price`.
# TODO: Write a function that confirms that the minting function mints the correct image.
# TODO: Write a test that confirms the minting function assigns the correct tokenId.
# TODO: Write a test that confirms the minted token has the correct `imageGallery[_imageNumber].royaltyPayoutAddress`.
# TODO: Write a test that confirms the minted token has the correct basis points for royalty split.
# TODO: Write a test that confirms that after minting `imageGallery[_imageNumber].currentTokenId` has been correctly incremented by 1.
# TODO: Write a test that confirms that the `_burn` function burns the correct token.
# TODO: Write a test that confirms that the correct token's royalty information is erased after burning.
# TODO: Write a test that confirms that `_baseURI` returns the expected address.
# TODO: Write a test that confirms once a token is minted that the metadata for that token is created correctly.


# ------------------------------- Resources -------------------------------- #
from scripts.deploy_renee_coins import deploy_contract
from scripts.helpful_scripts import get_account
from brownie import accounts, config, network, ReneeLaneCollection, reverts

# ------------------------------- Variables -------------------------------- #

# ---------------------------- Contract Tests ------------------------------ #
def test_contract_can_deploy():
    # Arrange
    account = get_account()
    # Act
    reneeLaneCollection = ReneeLaneCollection.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(
        f"\nThe Renee Lane Collection contract was deployed to: {reneeLaneCollection.address}.\n"
    )
    # Assert
    assert reneeLaneCollection.address != 0


# ----------------------------- Main Function ------------------------------ #
