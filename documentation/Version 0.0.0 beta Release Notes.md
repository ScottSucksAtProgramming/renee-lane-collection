Update to 0.0.0 beta

# Version 0.0.0 beta Changes

Very happy to release the 0.0.0 beta version of The Renee Lane Collection. The
initial feature development of these contracts has completed and it is being
moved to a testing phase on the Rinkeby Testnet.

Updates are listed below for both contracts. The next release will be the
initial beta release where both contracts will be up for user and integration
testing prior to the full launch.

# ReneeLaneCollection.sol

This is the main contract for The Renee Lane Artwork NFT Collection.

### General Code Changes

Code changes performed for this release were only for updating hardcoded
addresses built into the code. No feature changes, or other refactoring was
done between version 0.5.0 alpha and version 0.0.0 beta.

### License

The MIT License (MIT) is unchanged.

## General Documentation Changes

No major changes to documentation for this release. Comments comply is NatSpec
standard and are written to explain the code in the simplest terms so curious
users can understand what is going on.

### Documentation

Version updated

### Modification History

Modification history from alpha version was removed.

### Statistics

Statistics updated.

### Tasks

The task list was updated for the beta testing phase.

## Resources

### Pragma

Still using solidity version 0.8.15.

### Libraries

Imports for this contract are unchanged.

Contract Imports:

-   OpenZeppelin's ERC721.sol
-   OpenZeppelin's ERC721Royalty.sol
-   OpenZeppelin's Ownable.sol

## Contract

The contract section is unchanged.

## Data Structures

PROJECT_WALLET_ADDRESS was updated.

-   Structs
    -   Artwork Struct
    -   Artist Struct
-   Arrays
    -   investorList Array
-   Mappings
    -   artGallery Mapping
    -   artist Mapping
    -   isinvestor Mapping
    -   isWhitelisted Mapping
    -   payoutsOwed Mapping
-   State Variables - PROJECT_WALLET_ADDRESS

<details>

### Artwork Struct

The Artwork struct is used to define the properties that each piece of Artwork
in this collection must have. In this case each piece of artwork has an
imageNumber (1 through 50), a price in wei, a currentTokenID number a
lastTokenID number and an artistID number (1-5).

### Artist Struct

The Artist struct is used to define the properties for each artist. In this
case each artist has a directAddress where they will be paid their portion of
the minting proceeds and a RoyaltyAddress where proceed from secondary sales
will be split between the artist and the project.

### investorList Array

The investorList array is used to permanently store the addresses of anyone who
mints a art piece from this collection. This array is used in the
printInvestorList() function.

### artGallery Mapping

The artGallery mapping stores information about each piece of artwork using the
Artwork struct. When given an image number (1 through 50)the mapping will
return the imageNumber, price, currentTokenID,lastTokenID, and artistID for
that piece of art.

### artist Mapping

The artist Mapping stores information about each artist. When given an artistID
(1-5) it will return the directAddress and royaltyAddress for that artist.

### isInvestor Mapping

The isInvestoryapping stores information about each investor. When given a
wallet address it will return True if that address has minted a piece of art
from this collection. If they have not it will return False.

### isWhitelisted Mapping

The isWhitelisted mapping stores the whitelist status of addresses. These are
addresses that are allowed to mint tokens prior to the collection launch. When
given a wallet address it will return True if that address is whitelisted. If
they are not it will return False.

This mapping may be changed in future version to accomodate a Merkle Tree
design to lower gas usage.

### payoutOwed Mapping

The payoutsOwed mapping stores the payouts owed to each artist and to the
project owner. When given a wallet address this mapping will return the amount
of ether (in wei) that is owed to that address.

### PROJECT_WALLET_ADDRESS

The PROJECT_OWNER_ADDRESS is address of the project owner. It cannot be changed
after the contract is deployed. Funds owed to the project owner are paid to
this address.

</details><br/>

## Events

No Changes in this release.

This contract contains the following events:

-   NewInvestorAdded
-   PaymentSplit
-   PayoutSent

<details>

### NewInvestorAdded Event

The NewInvestorAdded event is triggered when a new investor is added to the
investor list and mapping. It logs the investor's address and the token ID of
the first piece of art they minted.

The NewInvestorAdded event is triggered when addNewInvestor() function is
called.

### PaymentSplit Event

The PaymentSplit event is triggered when a minting payment is received and
split between the artist and the project owner. It logs the amount of ether (in
wei) that is due to the artist and the amount that is due to the project owner.

The PaymentSplit event is trigged when the splitPayment() function is called.

### PayoutSent Event

The PayoutSent event is triggered when a payout is sent from payout, the
address of the recipient and the amount of ether (in wei) the contract. It logs
the address of the person who initiated the that was sent.

The PayoutSent event is triggered when the withdrawPayout() or forcePayment()
functions are called.

</details><br/>

## Constructor

All direct and royalty addresses were updated during this release.

## Functions

The \_baseURI function was changed this release.

This contract contains the following:

-   External Functions

    -   mintArtwork()
    -   withdrawPayout()

-   OnlyOwner Functions

    -   addToWhitelist()
    -   removeFromWhitelist()
    -   forcePayment()

-   Public Functions

    -   getContractBalance()
    -   printInvestorList()
    -   supportsInterface()
    -   tokenURI()

-   Internal Functions
    -   addNewInvestor()
    -   baseURI()
    -   \_burn()
    -   splitPayment()

<details>

## External Functions

### mintArtwork() Function

The mintImage() function was renamed to mintArtwork() to better fit the theme
of the project. The minter must specify the number of the image they wish to
purchase, and pay the correct amount of Ether.

The function will check to see if the minter is authorized to mint the image by
checking the isWhitelisted mapping. It insures that the minter has selected an
art piece contained within the collection and that there are still editions of
that artpiece available.

If all checks are passed the token will be minted and assigned to the minter
via the \_safeMint() function inherited from OpenZeppelin's ERC721 contract.
Royalty preferences for that token are set using the \_setTokenRoyalty()
function inherited from OpenZeppelin's ERC721Royalty contract and by using the
ERC2981 royalty standard.

If this is the first artpiece purchased by the minter their address will be
dded to the investorList and isInvestor mapping. @notice The payment received
from the minter is split between the artist and the PROJECT_WALLET_ADDRESS
using the splitPayment() function. These payouts can be withdrawn later.

Finally the mintArtwork() function increments the currentTokenID for that
artpiece removing one edition of that image from the amount available.

### withdrawPayout() Function

The withdrawPayout() function allows the caller to withdraw the Ether owed to
them. This function can be called by anyone but will revert if no money is owed
to them or if there is no Ether stored in the contract. When called by the
owner the payment will be disbursed to the PROJECT_WALLET_ADDRESS, otherwise
payment will be disbursed to the caller's address.

Once the payment has been sent the PayoutSent event is triggered to log the
payout. The balance owed to that address is set to 0.

## OnlyOwner Functions

### addToWhitelist() Function

The addToWhitelist() function allows the contract owner to authorize new
addresses to mint tokens early by setting their address to return True from the
isWhitelisted mapping. @notice The function will first check to ensure the
address is not already whitelisted. This function can only be called by the
owner.

Note: If the owner adds the Zero Address to the whitelist the mintArtwork()
function will allow ALL addresses to mint artwork.

### removeFromWhitelist() Function

The removeFromWhitelist() function allows the contract owner to deauthorize an
address from minting tokens early by setting their address to return False from
the isWhitelisted mapping.

The function will first check to ensure the address is currently on the
whitelist. This function can only be called by the owner.

### forcePayment() Function

The forcePayment() function allows the contract owner to force a payment to be
sent to an address they specify. This function can only be called by the owner
and is designed to be used in a situation where the artist cannot request their
own payout using the withdrawPayout() function.

Important: This function is less secure than withdrawPayout() and should only
be used when absolutely necessary. It does not follow the recommended pull
design pattern.

This function will revert if no payment is owed to the specified address, or
when the caller is not the owner. After paying the specified address, a
PayoutSent event is triggered and the balance owed to that address is set to 0.

## Public Functions

### getContractBalance() Function

The getContractBalance() function returns the current balance of Ether (in Wei)
currently stored in the contract.

### printInvestorList() Function

The printInvestosList() function returns the list of investor addresses from
the investorList array.

### supportsInterface() Function

The supportsInterface() function returns 'true' for supported interfaces.
Returns 'false' if the interface is not supported.

### tokenURI() Function

The tokenURI() function returns the Token URI for the specified tokenID. It
will revert if the tokenID provided does not exist.

## Internal Functions

Internal functions can only be called by the contract itself. They are not
available to users, the owner, or other contracts. This contract contains the
following:

### addNewInvestor() Function

The addNewInvestor() function will add a new investor to the investorList and
set their isInvestor mapping result to true.

Note: This function emits the NewInvestorAdded event.

### \_baseURI() Function

This function was changed to add the new metadata IPFS Address.

The \_baseURI() function returns the IPFS address where this collection's
metadata and assets are stored.

### \_burn() Function

The \_burn() function is used to burn a token. This is function which is
required by the libraries this contract uses to interact with the blockchain
but there is no way to call this function (or to burn tokens) for artwork from
this collection.

Important: If a token is burned it will be removed from the collection, the
royalty information will be erased. @notice Burning a token is irreversible. If
you burn your token it can NEVER be recovered.

### SplitPayment() Function

The splitPayment() function splits payments received during the minting
process. The artist receives 10% of the payment, and the project receives the
remaining 90%.

This function emits the PayoutSplit event.

</details><br/>

# Items Removed

No items were removed for this update.

# ReneeCoins.sol

This is the contract for ERC-20 Renee Coins social currency.

### General Code Changes

Code changes performed for this release were only for updating hardcoded
addresses built into the code. No feature changes, or other refactoring was
done between version 0.5.0 alpha and version 0.0.0 beta.

### License

The MIT License (MIT) is unchanged.

## General Documentation Changes

No major changes to documentation for this release. Comments comply is NatSpec
standard and are written to explain the code in the simplest terms so curious
users can understand what is going on.

### Documentation

Version updated

### Modification History

Modification history from alpha version was removed.

### Statistics

Statistics updated.

### Tasks

The task list was updated for the beta testing phase.

## Resources

### Pragma

Still using solidity version 0.8.15.

### Libraries

Imports for this contract are unchanged.

Contract Imports:

-   OpenZeppelin's ERC20.sol
-   OpenZeppelin's ERC20Burnable.sol
-   OpenZeppelin's ERC20BCapped.sol
-   OpenZeppelin's Ownable.sol

## Contract

The contract section is unchanged.

## Data Structures

There are no data structures for this contract.

## Constructor

No changes to the constructor in this release.

## Functions

Functions have been reorganized to follow the solidity Style Guide and are now
ordered by visibility.

This contract contains the following:

-   External Functions

    -   None

-   OnlyOwner Functions

    -   createCoins()
    -   airdropCoins()

-   Public Functions

    -   decimals()

-   Internal Functions
    -   \_mint()

<details>

## External Functions

## OnlyOwner Functions

### createCoins() Function

When this contract is initially deployed, there are 0 Renee Coins in existence.
New Renee Coins must be 'minted' in order to create them. createCoins() serves
as the mintingfunction for this contract. It can be called only by the owner
and allows them to mint as many Renee Coins as they like, up to the cap. This
function will ONLY create coins in the Owner's wallet. The airdropCoins()
function can be used to mint coins directly to someone else's wallet.

### airdropCoins() Function

The airdropCoins() function allows the Owner to mint new Renee Coins directly
into a specified wallet address. This is significantly cheaper than minting and
transferring the coins separately.

This function can ONLY be called by the Owner.

## Public Functions

### decimals() Function

The decimals() function replaces the inherited functions from the ERC20 and
ERC20Capped OpenZeppelin Contracts. For Renee Coins there are 0 decimal places,
these tokens cannot be broken down in smaller increments. This function is
required by the ERC-20 standard.

## Internal Functions

### \_mint() Function

The \_mint() function replaces the inherited functions from the ERC20 and
ERC20Capped Openzepplin Contracts. This is an internal function which can only
be called by the contract itself and is used inside other functions such as
createCoins() and airdropCoins().

</details><br>

# Items Removed

No items were moved for this release

# Python Scripts

Begun creating Python scripts to help manage the contract.

# README.md

The readme file was updated to reflect this release.
