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

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from scripts.helpful_scripts import get_account
from brownie import config, Contract, network, ReneeLaneCollection, ZERO_ADDRESS
from web3 import Web3
#* ------------------------------ Variables -------------------------------- #
contract_address = "0xd732dEC77Bd7725C55A8325D762904876CE8aDB0"
contract_network = "rinkeby"
contract_container = ReneeLaneCollection
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


def PROJECT_WALLET_ADDRESS() -> str:
    """Returns the address of the project wallet.

    Returns:
        project_wallet_address str: The wallet address where the project's cut
        of profits will be deposited.
    """

    contract = load_contract()
    project_wallet_address = contract.PROJECT_WALLET_ADDRESS()

    return project_wallet_address


def artGallery_mapping(image_number: int = None) -> dict:
    """Returns the properties of the specified image from the artGallery
    mapping of the contract as a dictionary.

    Returns:
        image_properties (Dict): Dictionary object containing the Image
        Number, Price (In Ether), Next Token ID, Tokens Remaining, and
        Artist ID.
    """

    contract = load_contract()
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

    return image_properties


def artist_mapping(artist_id: int = None) -> dict:
    """Returns the properties of the specified artist from the artist mapping.

    Args:
        artist_id (int, optional): The numeric ID of the artist (1-5).
        Defaults to None.

    Returns:
        artist_properties (dict): Dictionary object containing the Artist's
        Direct Address, and Royalty Address.
    """

    contract = load_contract()
    if artist_id is None:
        artist_id = int(
            input("Which artist would you like the properties of? (1-5)"))
    artist_properties = {}

    raw_properties = contract.artist(artist_id)

    artist_properties["Direct Address"] = raw_properties[0]
    artist_properties["Royalty Address"] = raw_properties[1]

    return artist_properties


def balanceOf(address: str = None) -> int:
    """Returns the number of tokens owned by the specified address.

    Args:
        address (str, optional): The wallet address which you wish to retrieve
        the information from. Defaults to None.

    Returns:
        number_of_tokens int: The number of tokens owned by the specified
        address.
    """

    contract = load_contract()
    if address is None:
        address = str(input("Which address would you like to check? "))

    number_of_tokens = contract.balanceOf(address)

    return number_of_tokens


def getApproved(token_id: str = None) -> str:
    """_summary_

    Args:
        token_id (str, optional): The Token ID of the token you want to see
        the approved addresses for. Defaults to None.

    Returns:
         approved_address (str): The address of anyone approved to use the
         token.
    """

    contract = load_contract()
    if token_id == None:
        token_id = int(input("Which token ID would you like to check? "))
    approved_address = contract.getApproved(token_id)

    if approved_address == ZERO_ADDRESS:
        approved_address = "No one"

    return approved_address


def getContractBalance() -> int:
    """Returns the balance of Ether currently stored in the contract.

    Returns:
        contract_balance (int): The amount of ether (in Wei) stored in the
        contract.
    """

    contract = load_contract()

    contract_balance = contract.getContractBalance()

    return contract_balance


def investorList_array(investor_index: int) -> str:
    """Returns the list of investors from the contract.

    Returns:
        address (str): The wallet address who have invested in the
        contract at the specified index.
    """

    contract = load_contract()
    investor_address = contract.investorList(investor_index)

    return investor_address


def isApprovedForAll(token_owner_address: str = None, approvee_address: str = None) -> bool:
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

    contract = load_contract()
    if token_owner_address is None:
        token_owner_address = str(
            input("What is the address of the owner of the tokens? "))
    if approvee_address is None:
        approvee_address = str(
            input("What is the address of the person who's approval is being checked? "))

    approval_status = contract.isApprovedForAll(
        token_owner_address, approvee_address)

    return approval_status


def isInvestor(wallet_address: str = ZERO_ADDRESS) -> bool:
    """Returns whether or not the specified wallet address is an investor.

    Args:
        wallet_address (str, optional): Address which is being checked for
        it's investor status. Defaults to the Zero Address.

    Returns:
        investor_status (bool): Returns True if the address is an investor,
        otherwise returns False.
    """

    contract = load_contract()

    investor_status = contract.isInvestor(wallet_address)

    return investor_status


def isWhitelisted(wallet_address: str = ZERO_ADDRESS) -> bool:
    """Returns whether or not the specified wallet address is on the
    whitelist.

    Args:
        wallet_address (str, optional): The address to be checked against the
        whitelist. Defaults to ZERO_ADDRESS.

    Returns:
        bool: True if the address is on the whitelist, otherwise false.
    """

    contract = load_contract()

    whitelisted_status = contract.isWhitelisted(wallet_address)

    return whitelisted_status


def name() -> str:
    """Returns the name of the collection of tokens.

    Returns:
        (str): The name of the collection of tokens.
    """

    contract = load_contract()

    name = contract.name()

    return name


def owner() -> str:
    """Returns the wallet address of the owner of the contract.

    Returns:
        str: The wallet address of the owner of the contract.
    """

    contract = load_contract()

    owner = contract.owner()

    return owner


def ownerOf(token_ID: int = None) -> str:
    """Returns the wallet address of the owner of the specified token.

    Args:
        token_ID (int, optional): The Token ID of the token you're looking
        for. Defaults to None.

    Returns:
        owner_of_token str: Wallet address of the owner of the specified
    """

    contract = load_contract()

    owner_of_token = contract.ownerOf(token_ID)

    return owner_of_token


def payoutsOwed(wallet_address: str) -> int:
    """Returns the amount of Ether (in Wei) owed to the specified wallet
    address.

        Args:
            wallet_address (str): The wallet address of the person who's
            payouts are being checked.

        Returns:
            payouts_owed (int): The amount of Ether (in wei) owed to the
            specified wallet address.
        """

    contract = load_contract()

    payouts_owed = contract.payoutsOwed(wallet_address)

    return payouts_owed


def printInvestorList() -> list[str]:
    """Returns the list of investors from the contract.

    Returns:
        investor_list (list[str]): The list of investors from the contract.
    """

    contract = load_contract()

    investor_list = contract.printInvestorList()

    return investor_list


def symbol() -> str:
    """Returns the symbol of the collection of tokens.

    Returns:
        (str): The symbol of the collection of tokens.
    """

    contract = load_contract()

    symbol = contract.symbol()

    return symbol


def tokenURI(token_id: int) -> str:
    """Returns the URI of the specified token.

        Args:
            token_id (int): The ID of the token you're looking for.

        Returns:
            token_uri (str): The URI of the specified token.
        """

    contract = load_contract()

    token_URI = contract.tokenURI(token_id)

    return token_URI

#* ----------------------- Contract Write Functions ------------------------ #
