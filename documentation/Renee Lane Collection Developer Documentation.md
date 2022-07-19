# Resources

@notice Pragma statements tell the compiler to use the version of solidity this
contract was designed for.

@notice Import statements allow the contract to access features of other
contracts. Specifically OpenZeppelin's ERC721, ERC721Royalty, and Ownable
libraries.

# Contract

@notice The contract statement defines the contract's name, and the libraries
that it uses.

@notice The Renee Lane Collection inherits OpenZeppelin's ERC721,
ERC721Royalty, and Ownable extensions to ensure compliance to the current
standards and provide a strong security basis with code that has been vetted
elsewhere.

# Data Structures

@notice Data structures are used to store data in the contract. They represent
real world objects in the code. In this contract there are structures which
represent pieces of artwork and the artists. There are additional structures
which represent collection investors, the art gallery where the collection is
managed, a whitelist of people who can invest in the collection early, and a
ledger which tracks the collection's payouts owed to the artists and the
project owner.

## Structs

@notice Structs represent items with specific properties. This contract uses
two structs to define the Artwork and the Artists.

@notice The Artwork struct is used to define the properties that each piece of
Artwork in this collection must have. In this case each piece of artwork has an
imageNumber (1 through 50), a price in wei, a currentTokenID number a
lastTokenID number and an artistID number (1-5).

@notice The Artist struct is used to define the properties for each artist. In
this case each artist has a directAddress where they will be paid their portion
of the minting proceeds and a RoyaltyAddress where proceed from secondary sales
will be split between the artist and the project.

## Arrays

@notice Arrays are used to store collections of items.

@notice The investorList array is used to permanently store the addresses of
anyone who mints a art piece from this collection. This array is used in the
printInvestorList() function.

## Mappings

@notice Mappings are gas efficient ways to store collections of items. They are
similar to Arrays but only return specific information based on a key (or
question) provided to them.

@notice The artGallery mapping stores information about each piece of artwork
using the Artwork struct. When given an image number (1 through 50)the mapping
will return the imageNumber, price, currentTokenID,lastTokenID, and artistID
for that piece of art.

@notice The artist Mapping stores information about each artist. When given an
artistID (1-5) it will return the directAddress and royaltyAddress for that
artist.

@notice The isInvestor mapping stores information about each investor. When
given a wallet address it will return True if that address has minted a piece
of art from this collection. If they have not it will return False.

@notice The isWhitelisted mapping stores the whitelist status of addresses.
These are addresses that are allowed to mint tokens prior to the collection
launch. When given a wallet address it will return True if that address is
whitelisted. If they are not it will return False.

@notice The payoutsOwed mapping stores the payouts owed to each artist and to
the project owner. When given a wallet address this mapping will return the
amount of ether (in wei) that is owed to that address.

## State Variables

@notice The PROJECT_OWNER_ADDRESS is address of the project owner. It cannot be
changed after the contract is deployed. Funds owed to the project owner are
paid to this address.

# Events

@notice Events are used to log important updates about what The Renee Lane
Collection is doing. When an event is triggered it will log the information
permanently on the blockchain.

@notice The NewInvestorAdded event is triggered when a new investor is added to
the investor list and mapping. It logs the investor's address and the token ID
of the first piece of art they minted. @notice The NewInvestorAdded event is
triggered when addNewInvestor() function is called.

@notice The PaymentSplit event is triggered when a minting payment is received
and split between the artist and the project owner. It logs the amount of ether
(in wei) that is due to the artist and the amount that is due to the project
owner.

@notice The PaymentSplit event is triggered when the splitPayment() function is
called.

@notice The PayoutSent event is triggered when a payout is sent from the
contract. It logs the address of the person who initiated the payout, the
address of the recipient and the amount of ether (in wei) that was sent.

@notice The PayoutSent event is triggered when the withdrawPayout() or
forcePayment() functions are called.

# Constructor

@notice The constructor helps set up the initial state of the smart contract.
It is called when the contract is deployed.

@notice It first sets the name of the Art Collection and the Symbol the tokens
will have.

@notice Here the constructor populates the artist mapping by assigning the
direct and royalty addresses to each artist by their ID number.

@notice Here the constructor populates the artGallery mapping by creating
Artwork objects for each image in the collection. The image number, price,
starting token ID, and artist who created the image are all assigned. The
lastTokenID is also set which limits the number of tokens that can be minted
for that piece of art.

# External Functions

@notice External functions can ONLY be called from other contracts, or users.

### purchaseArtwork()

@notice The purchaseArtwork() function was renamed to purchaseArtwork() to
better fit the theme of the project. The minter must specify the number of the
image they wish to purchase, and pay the correct amount of Ether.

@notice The function will check to see if the minter is authorized to mint the
image by checking the isWhitelisted mapping. It insures that the minter has
selected an art piece contained within the collection and that there are still
editions of that art piece available.

@notice If all checks are passed the token will be minted and assigned to the
minter via the \_safeMint() function inherited from OpenZeppelin's ERC721
contract. Royalty preferences for that token are set using the
\_setTokenRoyalty() function inherited from OpenZeppelin's ERC721Royalty
contract and by using the ERC2981 royalty standard.

@notice If this is the first art piece purchased by the minter their address
will be added to the investorList and isInvestor mapping.

@notice The payment received from the minter is split between the artist and
the PROJECT_WALLET_ADDRESS using the splitPayment() function. These payouts can
be withdrawn later.

@notice Finally the purchaseArtwork() function increments the currentTokenID
for that art piece removing one edition of that image from the amount
available.

@param \_imageNumber The number of the image the user wants to mint (1-50).

### withdrawPayment()

@notice The withdrawPayout() function allows the caller to withdraw the Ether
owed to them. This function can be called by anyone but will revert if no money
is owed to them or if there is no Ether stored in the contract. When called by
the owner they payment will be disbursed to the PROJECT_WALLET_ADDRESS,
otherwise payment will be disbursed to the caller's address.

@notice Once the payment has been sent the PayoutSent event is triggered to log
the payout. The balance owed to that address is set to 0.

## OnlyOwner Functions

@notice OnlyOwner functions are only callable by the owner of the contract.
They are subclass of External Functions.

### addToWhitelist()

@notice The addToWhitelist() function allows the contract owner to authorize
new addresses to mint tokens early by setting their address to return True from
the isWhitelisted mapping.

@notice The function will first check to ensure the address is not already
whitelisted. This function can only be called by the owner.

@notice Note: If the owner adds the Zero Address to the whitelist the
purchaseArtwork() function will allow ALL addresses to mint artwork.

@param \_address The address to be added to the whitelist.

### removeFromWhitelist()

@notice The removeFromWhitelist() function allows the contract owner to
unauthorize an address from minting tokens early by setting their address to
return False from the isWhitelisted mapping.

@notice The function will first check to ensure the address is currently on the
whitelist. This function can only be called by the owner.

@param \_address The address to be removed from the whitelist.

### forcePayment()

@notice The forcePayment() function allows the contract owner to force a
payment to be sent to an address they specify. This function can only be called
by the owner and is designed to be used in a situation where the artist cannot
request their own payout using the withdrawPayout() function.

@notice This function is less secure than withdrawPayout() and should only be
used when absolutely necessary. It does not follow the recommended pull design
pattern.

@notice This function will revert if no payment is owed to the specified
address, or when the caller is not the owner. After paying the specified
address, a PayoutSent event is triggered and the balance owed to that address
is set to 0.

@param \_addressToBePayed The address of the wallet payment will be sent to.

# Public Functions

### getContractBalance()

@notice Public functions can be seen and called from other contracts, users as
well as from the contract itself.

@notice The getContractBalance() function returns the current balance of Ether
(in Wei) currently stored in the contract.

@return contractBalance The amount of Ether (in Wei)

### printInvestorList()

@notice The printInvestosList() function returns the list of investor addresses
from the investorList array.

@return allInvestors The address stored on the investorList[] array.

### supportsInterface()

@notice The supportsInterface() function returns 'true' for supported
interfaces. Returns 'false' if the interface is not supported.

@param interfaceID The 4 byte identifier for an interface.

@return bool A True of False value.

### tokenURI()

@notice The tokenURI() function returns the Token URI for the specified
tokenID. It will revert if the tokenID provided does not exist.

@param tokenID - The number of the token for which the URI is being set.

@return string - The full tokenURI address for the specified token.

# Internal Functions

@notice Internal functions are only callable by the contract itself. They are
not available to users, the owner, or other contracts.

### addNewInvestor()

@notice The addNewInvestor() function will add a new investor to the
investorList and set their isInvestor mapping result to true.

@notice This function emits the NewInvestorAdded event.

@param \_minterAddress Wallet address of the person who minted the artwork.

@param \_tokenID the tokenID of the artwork they minted.

### \_baseURI()

@notice The \_baseURI() function returns the IPFS address where this
collection's metadata and assets are stored.

@return string The baseURI address.

### \_burn()

@notice The \_burn() function is used to burn a token. This is function which
is required by the libraries this contract uses to interact with the blockchain
but there is no way to call this function (or to burn tokens) for artwork from
this collection.

@notice If a token is burned it will be removed from the collection, the
royalty information will be erased.

@notice Burning a token is irreversible. If you burn your token it can NEVER be
recovered.

@param tokenID The token ID which is to be destroyed.

### splitPayment()

@notice The splitPayment() function splits payments received during the minting
process. The artist receives 10% of the payment, and the project receives the
remaining 90%.

@notice This function emits the PayoutSplit event.

@param \_artistDirectAddress The address of the artist's wallet.

@param valueSent The amount of Ether received when the artwork was minted.
