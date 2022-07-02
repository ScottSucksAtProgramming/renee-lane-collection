Update to 0.5.0 alpha

# Version 0.5.0 alpha Changes

Very happy to release the 0.5.0 alpha version of The Renee Lane Collection.

This is the last release for initial development. Updates are listed below for
both contracts. The next release will be the initial beta release where both
contracts will be up for user and integration testing prior to the full launch.

<!-- TABLE OF CONTENTS -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a  href="#reneelanecollection-contract">ReneeLaneCollection Contract</a>
            <ul>
                <li><a  href="#general-code-changes">General Code Changes</a></li>
                <li><a  href="#license">License</a></li>
                <li><a  href="#general-documentation-changes">General Documentation Changes</a></li>
                <li><a href="#resources">Resources</a></li>
                <ul>
                    <li><a href="#pragma">Pragma</a></li>
                    <li><a href="#libraries">Libraries</a></li></ul>
                <li><a href="#contract">Contract</a></li>
                <li><a href="#data-structures">Data Structures</a></li>
                <li><a href="#events">Events</a></li>
                <li><a href="#constructor">Constructor</a></li>
                <li><a href="#functions">Functions</a></li>
                <ul>
                    <li><a href="#external-functions">External Functions</a></li>
                    <li><a href="#onlyowner-functions">OnlyOwner Functions</a></li>
                    <li><a href="#public-functions">Public Functions</a></li>
                    <li><a href="#internal-functions">Internal Functions</a></li>
            </ul>
            <li><a href="#removed-items">Removed Items</a></li>
        <li><a  href="#reneecoins-contract">ReneeCoins Contract</a>
            <ul>
                <li><a  href="#general-code-changes">General Code Changes</a></li>
                <li><a  href="#license">License</a></li>
                <li><a  href="#general-documentation-changes">General Documentation Changes</a></li>
                <li><a href="#resources">Resources</a></li>
                <ul>
                    <li><a href="#pragma">Pragma</a></li>
                    <li><a href="#libraries">Libraries</a></li></ul>
                <li><a href="#contract">Contract</a></li>
                <li><a href="#constructor">Constructor</a></li>
                <li><a href="#functions">Functions</a></li>
                <ul>
                    <li><a href="#external-functions">External Functions</a></li>
                    <li><a href="#onlyowner-functions">OnlyOwner Functions</a></li>
                    <li><a href="#public-functions">Public Functions</a></li>
                    <li><a href="#internal-functions">Internal Functions</a></li>
            </ul>
            <li><a href="#removed-items">Removed Items</a></li>
    </ol>
</details><br/>

<!-- ReneeLaneCollection.sol -->

# ReneeLaneCollection Contract

This is the main contract for The Renee Lane Artwork NFT Collection.

## General Code Changes

The code was refactored to follow the solidity Style Guide including the
reorganization of functions which are now ordered by visibility instead of
category.

## License

The MIT License (MIT) is unchanged.

## General Documentation Changes

Comments and in-contract documentation was expanded to include more information
and to stick with the NatSpec documentation standard. These comments are
written mostly for the end users who may be interested in seeing what each
piece of the code is doing to ensure that it can be relied on to work as
advertised. There is some developer information as well which will be expanded
in future releases.

### Documentation

Updated for the new release.

### Modification History

Updates added for the new release.

### Statistics

New functions added to the table. New USD Costs were calculated based on the
updated gas usage and current Gas and Ether prices.

### Tasks

The task list was updated for the current release.

## Resources

### Pragma

Changed to be exactly 0.8.15 for increased security.

### Libraries

Imports for this contract are unchanged.

## Contract

The contract section is unchanged.

## Data Structures

### Artwork Struct

The Image struct was renamed to Artwork to better reflect the theme of the
project. The information stored in the struct has not changed.

### Artist Struct

The Artist struct has not been changed. It stores the artist's direct wallet
address as well as the address of the MoneyPipe contract responsible for
splitting the artist's and project's royalty earnings.

### investorList Array

The investorList array stores the addresses of the investors who have minted a
piece of artwork from this collection. This array may be removed in later
versions as a way to save gas.

### artGallery Mapping

the imageGallery mapping was renamed to artGallery to better reflect the theme
of this project. It stores an Artwork object for each image in the collection
and will return the artwork information when given the image's number (1-50)

### artist Mapping

The artist mapping is unchanged. It stores an Artist object for each artist and
returns the artist's information when given the artist's ID number (1-5).

### isInvestor Mapping

The isInvestor mapping is unchanged. It stores a boolean value for wallet
addresses. The isInvestor mapping will return true for any wallet address that
has previously minted a piece of artwork from this collection. If the address
has not minted a piece of artwork, the mapping will return false.

### isWhitelisted Mapping

The isWhitelisted mapping was added in this release. This mapping stores a
boolean value for wallet addresses. The isWhitelisted mapping will return true
for any wallet address that has been whitelisted for this collection. If the
address has not been whitelisted, the mapping will return false.

This mapping may be changed in future version to accomodate a Merkle Tree
design to lower gas usage.

### payoutOwed Mapping

The payoutOwed mapping is unchanged from the previous release. It stores the
amount of Ether owed to each artist and the project wallet based on their
wallet address. Each time a piece of artwork is minted, the price of that image
is split between the project and the artist. The mapping will return the amount
of Ether owed (in Wei) to the address provided.

### PROJECT_WALLET_ADDRESS

The projectWAlletAddress variable was renamed to PROJECT_WALLET_ADDRESS to make
it easier identifiable as a constant. This variable stores the address of the
wallet where the project's earnings are sent.

## Events

Three new events were created to ensure logging is accurate.

This contract contains the following events:

-   NewInvestorAdded
-   PaymentSplit
-   PayoutSent

### NewInvestorAdded Event

This event is triggered when a new investor is added to isInvestor mapping and
investorList array. It logs the address of the investor as well as the token ID
they have minted.

The NewInvestorAdded event is triggered when addNewInvestor() function is
called.

### PaymentSplit Event

This event is triggered when a minting payment is received and then split
between the Artist and Project. It logs the value received by the contract, the
address of the artist who is due the payment, the amount of Ether (in Wei) of
the Artist's cut, and the amount of Ether (in Wei) of the Project's cut.

The PaymentSplit event is trigged when the splitPayment() function is called.

### PayoutSent Event

The PayoutSent event is triggered when a payout is sent from the contract. It
logs the address of the person who initiated the payout, the address of the
recipient and the amount of ether (in wei) that was sent.

The payoutMade event is triggered when the withdrawPayout() or forcePayment()
functions are called.

## Constructor

No changes to the constructor in this release.

## Functions

Functions have been reorganized to follow the solidity Style Guide and are now
ordered by visibility.

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

## External Functions

### mintArtwork() Function

The mintImage() function was renamed to mintArtwork() to better fit the theme
of the project. The minter must specify the number of the image they wish to
purchse, and pay the correct amount of Ether.

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
added to the investorList and isInvestor mapping.

The payment received from the minter is split between the artist and the
PROJECT_WALLET_ADDRESS using the splitPayment() function. These payouts can be
withdrawn later.

Finally the mintArtwork() function increments the currentTokenID for that
artpiece removing one edition of that image from the amount available.

### withdrawPayout() Function

The previous payArtist() and payoutFunds() functions have been removed and
replaced by the withdrawPayout() and forcePayment() functions.

The withdrawPayout() function allows the caller to withdraw the Ether owed to
them. This function can be called by anyone but will revert if no money is owed
to them or if there is no Ether stored in the contract. When called by the
owner they payment will be disbursed to the PROJECT_WALLET_ADDRESS, otherwise
payment will be disbursed to the caller's address.

Once the payment has been sent the PayoutSent event is triggered to log the
payout. The balance owed to that address is set to 0.

## OnlyOwner Functions

### addToWhitelist() Function

The addToWhitelist() function allows the contract owner to authorize new
addresses to mint tokens early by setting their address to return True from the
isWhitelisted mapping.

The function will first check to ensure the address is not already whitelisted.
This function can only be called by the owner.

Important Note: If the owner adds the Zero Address to the whitelist the
mintArtwork() function will allow ALL addresses to mint artwork.

### removeFromWhitelist() Function

The removeFromWhitelist() function allows the contract owner to deauthorize an
address from minting tokens early by setting their address to return False from
the isWhitelisted mapping.

The function will first check to ensure the address is currently on the
whitelist.

### forcePayment() Function

The previous payArtist() and payoutFunds() functions have been removed and
replaced by the withdrawPayout() and forcePayment() functions.

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

No changes have been made to the getContractBalance() function.

The getContractBalance() function returns the current balance of Ether (in Wei)
currently stored in the contract.

### printInvestorList() Function

No changes have been made to the printInvestorList() function.

The printInvestosList() function returns the list of investor addresses from
the investorList array.

### supportsInterface() Function

No changes have been made to the supportsInterface() function.

The supportsInterface() function returns 'true' for supported interfaces.
Returns 'false' if the interface is not supported.

### tokenURI() Function

The tokenURI() function returns the Token URI for the specified tokenID. It
will revert if the tokenID provided does not exist.

A guard check which prevented the \_baseURI() from being empty was removed. As
this will not be possible for this collection.

## Internal Functions

Internal functions can only be called by the contract itself. They are not
available to users, the owner, or other contracts. This contract contains the
following:

### addNewInvestor() Function

The addNewInvestor() function will add a new investor to the investorList and
set their isInvestor mapping result to true.

This function emits the NewInvestorAdded event.

### \_baseURI() Function

No changes have been made to the \_baseURI() function for this release.

The \_baseURI() function returns the IPFS address where this collection's
metadata and assets are stored.

### \_burn() Function

No changes have been made to the \_burn() function for this release.

The \_burn() function is used to burn a token. This is function which is
required by the libraries this contract uses to interact with the blockchain
but there is no way to call this function (or to burn tokens) for artwork from
this collection.

If a token is burned it will be removed from the collection, the royalty
information will be erased.

Important: Burning a token is irreversible. If you burn your token it can NEVER
be recovered.

### SplitPayment() Function

This function was added in this release.

The splitPayment() function splits payments received during the minting
process. The artist receives 10% of the payment, and the project receives the
remaining 90%.

This function emits the PayoutSent event.

# Removed Items

The following items were removed from this contract for the 0.5.0 alpha
release.

### isInvestor() Function Removed

The isInvestor() function was removed from the contract. The isInvestor mapping
has been declared public and replaces this function.

### checkArtistBalances() Function Removed

The checkArtistBalances() function was removed from the contract. The
payoutOwed mapping has been declared public and replaces this function.

# ReneeCoins Contract

This is the main contract for ERC-20 Renee Coins social currency.

### General Code Changes

The code was refactored to follow the solidity Style Guide including the
reorganization of functions which are now ordered by visibility instead of
category.

### License

The MIT License (MIT) is unchanged.

## General Documentation Changes

Comments and in-contract documentation was expanded to include more information
and to stick with the NatSpec documenation standard. These comments are written
mostly for the end users who may be interested in seeing what each piece of the
code is doing to ensure that it can be relied on to work as advertised. There
is some developer information as well which will be expanded in future
releases.d

### Documentation

Updated for the new release.

### Modification History

Updates added for the new release.

### Statistics

New functions added to the table. New USD Costs were calculated based on the
updated gas usage and current Gas and Ether prices.

### Tasks

The task list was updated for the current release.

## Resources

### Pragma

Changed to be exactly 0.8.15 for increased security.

### Libraries

Imports for this contract are unchanged.

## Contract

The contract section is unchanged.

## Data Structures

There are no custom data structures for this contact.

## Events

There are no events for this contract.

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

## External Functions

There are no external functions for this contract.

## OnlyOwner Functions

### createCoins() Function

When this contract is initially deployed, there are 0 Renee Coins in existence.
New Renee Coins must be 'minted' in order to create them. createCoins() serves
as the mintingfunction for this contract. It can be called only by the owner
and allows them to mint as many Renee Coins as they like, up to the cap.

This function will ONLY create coins in the Owner's wallet. The airdropCoins()
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

# Items Removed

No items were moved for this release

# README.md

The readme file was updated to reflect this release.
