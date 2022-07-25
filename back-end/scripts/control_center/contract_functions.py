#
#* ----------------------------- Documentation ------------------------------ #
# Module:  contract_functions_RLC.py
# This module will contain all the functions that will be used to interact
# with the Renee Lane Collection Smart Contract. They will be built in such a
# way that they can be used in other scripts and modules.
#
#
# Modification History
# 07-03-2022 | SRK | Module Created.
# 07-27-2022 | SRK | All contract functions added.

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import config, Contract, network, ReneeLaneCollection, ZERO_ADDRESS
from web3 import Web3
#* ------------------------------ Variables -------------------------------- #
contract_address = "0xd732dEC77Bd7725C55A8325D762904876CE8aDB0"
contract_network = "rinkeby"
contract_container = ReneeLaneCollection
owner_address = "0x0715534cc021ddc49915ac27f8ebcde8f5c99b35"
#* ---------------------------- Main Function ------------------------------ #

#* ----------------------------- Functions --------------------------------- #


def load_contract(contract_address: str = contract_address) -> Contract:
    """Returns contract object from the specified address via Etherscan API
    and loads it as a Contract object.

    Args:
        contract_address (str, optional): The address of the contract you wish
        to load.. Defaults to contract_address.

    Returns:
        Contract: Contract object for the specified contract.
    """
    contract = Contract.from_explorer(
        contract_address)
    return contract


def deploy_contract(contract_container):
    """Deploys a contract to the active network based on the specified brownie
    contract_container and returns it as an active object.

    Args:
        contract_container (_type_): _description_

    Returns:
        _type_: _description_
    """
    account = get_account()
    contract = contract_container.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    return contract


def explore_contract(contract: Contract) -> list:

    contract_info = dir(contract)


#* ----------------------- Contract Read Functions ------------------------- #


def PROJECT_WALLET_ADDRESS(contract) -> str:
    """Returns the address of the project wallet.

    Returns:
        project_wallet_address str: The wallet address where the project's cut
        of profits will be deposited.
    """

    project_wallet_address = contract.PROJECT_WALLET_ADDRESS()

    return project_wallet_address


def artGallery_mapping(contract, image_number: int = None) -> dict:
    """Returns the properties of the specified image from the artGallery
    mapping of the contract as a dictionary.

    Returns:
        image_properties (Dict): Dictionary object containing the Image
        Number, Price (In Ether), Next Token ID, Tokens Remaining, and
        Artist ID.
    """

    if image_number is None:
        image_number: int = int(
            input("Which image would you like the properties of? ")
        )

    raw_properties = contract.artGallery(image_number)

    image_properties = {}
    image_properties["Image Number"] = raw_properties[0]
    image_properties["Price (in Ether)"] = Web3.fromWei(
        raw_properties[1], "ether")
    image_properties["Next Token ID"] = raw_properties[2]
    image_properties["Tokens Remaining"] = (
        raw_properties[3] - raw_properties[2]) + 1
    image_properties["Artist"] = raw_properties[4]

    return raw_properties


def artist_mapping(contract, artist_id: int = None) -> dict:
    """Returns the properties of the specified artist from the artist mapping.

    Args:
        artist_id (int, optional): The numeric ID of the artist (1-5).
        Defaults to None.

    Returns:
        artist_properties (dict): Dictionary object containing the Artist's
        Direct Address, and Royalty Address.
    """

    if artist_id is None:
        artist_id = int(
            input("Which artist would you like the properties of? (1-5)"))
    artist_properties = {}

    raw_properties = contract.artist(artist_id)

    artist_properties["Direct Address"] = raw_properties[0]
    artist_properties["Royalty Address"] = raw_properties[1]

    return artist_properties


def balanceOf(contract, address: str = None) -> int:
    """Returns the number of tokens owned by the specified address.

    Args:
        address (str, optional): The wallet address which you wish to retrieve
        the information from. Defaults to None.

    Returns:
        number_of_tokens int: The number of tokens owned by the specified
        address.
    """

    if address is None:
        address = str(input("Which address would you like to check? "))

    number_of_tokens = contract.balanceOf(address)

    return number_of_tokens


def getApproved(contract, token_id: str = None) -> str:
    """_summary_

    Args:
        token_id (str, optional): The Token ID of the token you want to see
        the approved addresses for. Defaults to None.

    Returns:
         approved_address (str): The address of anyone approved to use the
         token.
    """

    if token_id == None:
        token_id = int(input("Which token ID would you like to check? "))
    approved_address = contract.getApproved(token_id)

    if approved_address == ZERO_ADDRESS:
        approved_address = "No one"

    return approved_address


def getContractBalance(contract, ) -> int:
    """Returns the balance of Ether currently stored in the contract.

    Returns:
        contract_balance (int): The amount of ether (in Wei) stored in the
        contract.
    """

    contract_balance = contract.getContractBalance()

    return contract_balance


def investorList_array(contract, investor_index: int) -> str:
    """Returns the list of investors from the contract.

    Returns:
        address (str): The wallet address who have invested in the
        contract at the specified index.
    """

    investor_address = contract.investorList(investor_index)

    return investor_address


def isApprovedForAll(contract, token_owner_address: str = None, approvee_address: str = None) -> bool:
    """Returns whether or not the approvee's address is approved for tokens of a particular owner.

    Args:
        token_owner_address (str): The wallet address of the owner of the
        tokens.

        approvee_address (str): Address of the person who's approval is being
        checked.

    Returns:
        approval_status bool: True if the approvee is approved for the tokens,
        otherwise false.
    """

    if token_owner_address is None:
        token_owner_address = str(
            input("What is the address of the owner of the tokens? "))
    if approvee_address is None:
        approvee_address = str(
            input("What is the address of the person who's approval is being checked? "))

    approval_status = contract.isApprovedForAll(
        token_owner_address, approvee_address)

    return approval_status


def isInvestor(contract, wallet_address: str = ZERO_ADDRESS) -> bool:
    """Returns whether or not the specified wallet address is an investor.

    Args:
        wallet_address (str, optional): Address which is being checked for
        it's investor status. Defaults to the Zero Address.

    Returns:
        investor_status (bool): Returns True if the address is an investor,
        otherwise returns False.
    """

    investor_status = contract.isInvestor(wallet_address)

    return investor_status


def isWhitelisted(contract, wallet_address: str = ZERO_ADDRESS) -> bool:
    """Returns whether or not the specified wallet address is on the
    whitelist.

    Args:
        wallet_address (str, optional): The address to be checked against the
        whitelist. Defaults to ZERO_ADDRESS.

    Returns:
        bool: True if the address is on the whitelist, otherwise false.
    """

    whitelisted_status = contract.isWhitelisted(wallet_address)

    return whitelisted_status


def name(contract, ) -> str:
    """Returns the name of the collection of tokens.

    Returns:
        (str): The name of the collection of tokens.
    """

    name = contract.name()

    return name


def owner(contract, ) -> str:
    """Returns the wallet address of the owner of the contract.

    Returns:
        str: The wallet address of the owner of the contract.
    """

    owner = contract.owner()

    return owner


def ownerOf(contract, token_ID: int = None) -> str:
    """Returns the wallet address of the owner of the specified token.

    Args:
        token_ID (int, optional): The Token ID of the token you're looking
        for. Defaults to None.

    Returns:
        owner_of_token str: Wallet address of the owner of the specified
    """

    owner_of_token = contract.ownerOf(token_ID)

    return owner_of_token


def payoutsOwed(contract, wallet_address: str) -> int:
    """Returns the amount of Ether (in Wei) owed to the specified wallet
    address.

        Args:
            wallet_address (str): The wallet address of the person who's
            payouts are being checked.

        Returns:
            payouts_owed (int): The amount of Ether (in wei) owed to the
            specified wallet address.
        """

    payouts_owed = contract.payoutsOwed(wallet_address)

    return payouts_owed


def printInvestorList(contract,) -> list[str]:
    """Returns the list of investors from the contract.

    Returns:
        investor_list (list[str]): The list of investors from the contract.
    """

    investor_list = contract.printInvestorList()

    return investor_list


def symbol(contract,) -> str:
    """Returns the symbol of the collection of tokens.

    Returns:
        (str): The symbol of the collection of tokens.
    """

    symbol = contract.symbol()

    return symbol


def tokenURI(contract, token_id: int) -> str:
    """Returns the URI of the specified token.

        Args:
            token_id (int): The ID of the token you're looking for.

        Returns:
            token_uri (str): The URI of the specified token.
        """

    token_URI = contract.tokenURI(token_id)

    return token_URI

#* ----------------------- Contract Write Functions ------------------------ #


def addToWhitelist(contract, _address: str, sender_address: str):
    """Adds the specified address to the whitelist.

    Args:
        _address (str): The address to be added to the whitelist.

        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.addToWhitelist(_address, {'from': sender_address})

    return transaction


def removeFromWhitelist(contract, _address, sender_address):
    """Removes the specified address from the whitelist.

    Args:
        _address (str): The address to be removed from the whitelist.

        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.removeFromWhitelist(
        _address, {'from': sender_address}
    )

    return transaction


def approve_address_for_tokenId(contract, to: str, tokenID: int, sender_address: str):
    """Approves the specified address to use the specified token.

    Args:
        to (str): The address to be approved to use the specified
        token.

        tokenId (int): The ID of the token you're approving to use.

        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.approve(to, tokenID, {'from': sender_address})
    return transaction


def forcePayment(contract, _addressToBePayed: str, sender_address: str):
    """Forces a payout to the specified address. Can only be called by owner.

    Args:
        _addressToBePayed (str): The address to be forced to pay their
        payouts.

        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.forcePayment(
        _addressToBePayed, {'from': sender_address})
    return transaction


def purchaseArtwork(contract, _imageNumber: int, sender_address: str):
    """Mints a new artwork token..

    Args:
        _imageNumber (int): The number of the artwork you're minting.

        sender_address (str): The address of the person who's minting the
        token.

    """
    image_price = artGallery_mapping(_imageNumber)[1]

    transaction = contract.mintArtwork(
        _imageNumber, {'from': sender_address, "value": image_price}
    )
    return transaction


def renounceOwnership(contract, sender_address):
    """Renounces ownership of the contract.

    Args:
        sender_address (str): The wallet address of the sender of the transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.renounceOwnership({'from': sender_address})
    return transaction


def safeTransferFrom(contract, sender_address: str, to: str, tokenID: int):
    """Transfer token from one address to another.

    Args:
        sender_address (str): Address of the sender of the transaction and 
        token.

        to (str): Address of the recipient of the token.

        tokenID (int): ID number of the token being transferred.

    Returns:
        transaction: The transaction object.
    """

    transaction = contract.safeTransferFrom(
        sender_address, to, tokenID, {"from": sender_address})

    return transaction


def setApprovalForAll(contract, approvee: str, approved: bool, sender_address: str):
    """Sets the approval for all tokens to the specified address.

    Args:
        approvee (str): The address of the person who is getting approved.

        approved (bool): Whether or not the operation is approved.

        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.setApprovalForAll(
        approvee, approved, {'from': sender_address})

    return transaction


def transferFrom(contract, sender_address: str, to: str, tokenID: int):
    """Transfer token from one address to another.

    Args:
        sender_address (str): Address of the sender of the transaction and 
        token.

        to (str): Address of the recipient of the token.

        tokenID (int): ID number of the token being transferred.

    Returns:
        transaction: The transaction object.
    """

    transaction = contract.transferFrom(
        sender_address, to, tokenID, {"from": sender_address})

    return transaction


def transferOwnership(contract, newOwner: str, sender_address: str):
    """Transfer ownership of the contract.

    Args:
        newOwner (str): Address of the person who is being made owner.
        sender_address (str): address of the transaction sender.

    Returns:

        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.transferOwnership(
        newOwner, {'from': sender_address})

    return transaction


def withdrawPayout(contract, sender_address: str):
    """Withdraws the payout from the contract.

    Args:
        sender_address (str): The wallet address of the sender of the
        transaction.

    Returns:
        transaction (str): The transaction hash of the transaction.
    """

    transaction = contract.withdrawPayout({'from': sender_address})

    return transaction
