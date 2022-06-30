//* SPDX-License-Identifier: MIT
/**
 * ___________________________________________________________________________
 * ___________________▄▄Æ█▀▀▀███Æ▄▄,_______,▄▄Æ▀██▀▀▀██▄▄_____________________
 * _______"▌^^^^^^▐█▀▀█^^█▀^^█▀^▀█▌╚▀▀▀""▀▀▀▀█▌^▀█^^^█^^█▀▀█▌^^^^^^^Γ_________
 * ________ ┐____▄▀█__╟▌_█___█>^_.─^``,,,_`"¬- `~█__ █_▐▌_ █╙█____,`__________
 * _________ \_ █▌_ █__█_╟▌,^ -`,⌐`__ ______ "-_*,`w]▌_█__█`_ █__/____________
 * ___________▐█ ▀▄_╙█_╟▌▐▀_⌐ ⌐ _______________ "▄",└▌▐▌_▓▀_▄▀_█▌_____________
 * ___________█▀█,_▀▄╙▌_█_┌_▄▄¬`___``¬,_,~^`____`¬▓_\_█_▐▌▄█ ,▄▀█_____________
 * __________▐▌_ ╬▀▓▄██▄ ╒_╛╙╕_______,^__-_______ ╨╨_\_¥██▄█▀╟__╟▌____________
 * __________█▀▀▀██▄▄▀█▌_─⌠_ _\___________ _____, ,_▐_b █▀▄▄▓▓▀▀╙█____________
 * __________█▄▄▄▄▄█▄██⌐j_▌__'_"___ _╒███▌__┌__╒ ,____│_████▄▄▄▄▄█____________
 * __________╟▌___,▄█▌_▌j_▌___ _ ç[__└███▀____Æ_'___ _╠_▌╠▀▄▄___]█____________
 * __________ █▄█▀`__▄█▌_▌╘_____ `▌_________,▀ _____⌠_⌐]█▄__└▀█▄█⌐____________
 * ___________╙▌__▄█▀`_╟▄└_%______└\_______,\______┌_Å_█_ ╙█▄__▐▌_____________
 * ____________▀█▀ _,▄▀└╙▄ ┐'______┌^_____/_______ƒ_┘_╛└▀█▄_ ▀██______________
 * _____________╙█▄▀╙__,▓▀█_²_'._____ ┐__∩_ ___,* / ▄▀█▄__└▀█▓▀_______________
 * ______________ █▄_▄█╙_,▓█*_`≈,`≈.,_`¼╛__.-^ -^_/██,_╙▀▄_╓█_________________
 * _▄█▀▀▀▀▄________╙█▄_▄█▀_▄█▌▐▌._`"~-----─¬` ,╤▌╙█▄_╙▀▄_╓█▀________▄█▀▀▀▓▄___
 * ▓▌_____█⌐_________╙█▄,▓▀`▄██ __  `"¬¬¬"``___ ██▄ ▀█,▄█╙_________ █_____╙█__
 * █_____╒█____________ ▀█▄▀╓█`½_______________╒ █▄▀██▀_____________╙⌐____ █__
 * └█_____________________,██▄__\_____________/__▄██▄_____________________█▀__
 * _ ▀▓,_______________,▄▀╙__ ╙▀█▓___________▓█▀╙___╙▀█▄_______________,▓▀____
 * _____▀▀█▄▄▄▄▄▄▄▄Æ▀▀▀__________ ╙█████████▀__________ ╙▀▀█▄▄▄▄▄▄▄▄█▀▀`______
 * ________________________________ ███████___________________________________
 * __________________________________╙████____________________________________
 * ___________________________________╙██_____________________________________
 * ____________________________________ ______________________________________
 * ___________________________________________________________________________
 *      Surrender   |   Submit  |   Sacrifice   |   Serve   |   Survive
 */

//* ---------------------------- Documentation ---------------------------- //
/**
 * @title The Renee Lane Collection
 * @author Scott Kostolni
 *
 * @notice Version 0.5.0 Alpha
 *
 * @notice This is a bespoke ERC-721 smart contract written to manage creation
 * and tracking of Non-Fungible Tokens for the Renee Lane Collection, a
 * 50-piece collection of artwork inspired by the author Ms. Renee Lane. The
 * artwork featured in this collection is being sold as limited edition
 * digital prints tracked on the blockchain. The proceeds from this project
 * are being split between the artists and the film-producer, Ms. Viola
 * Voltairine, who is bringing Ms. Renee Lane's book to life as an independent
 * film.
 *
 * @notice This contract allows for the minting of a limited number of
 * tokens for each piece of artwork in The Renee Lane Collection. The artwork
 * is tracked on the blockchain using the ERC-721 standard. Royalties are
 * paid to the artist for each piece minted, as well as through secondary
 * marketplace sales of the artwork. Royalty information is baked into the
 * tokens via the ERC-2981 standard. Metadata for these tokens are securely
 * stored off-chain in IPFS and cannot be altered later.
 *
 * @notice Investors who mint artwork from this collection are stored
 * permanently in the contract's storage so investors will always maintain
 * their benefits even if their artwork is sold or transferred.
 *
 * @notice OpenZeppelin's ERC7211, ERC721Royalties and Ownable contracts were
 * used to provide the standard NFT functionality using secure and tested
 * libraries.
 */

//* ------------------------ Modification History ------------------------- //
/**
 * 04-28-2022 | SRK | Project Created.
 * 04-30-2022 | SRK | Added counters to a struct to help save gas.
 * 05-03-2022 | SRK | Code imported into Renee Lane Collection Project.
 * 05-09-2022 | SRK | Minting Function Completed.
 * 05-10-2022 | SRK | Contract Ownership Functionality Added.
 * 05-15-2022 | SRK | Royalty Functionality Added.
 * 05-15-2022 | SRK | Version 0.1.0 Alpha released.
 * 05-18-2022 | SRK | mintArtwork() gas optimization pass.
 * 05-19-2022 | SRK | Implemented Minting and Royalty Payouts.
 * 05-19-2022 | SRK | Version 0.2.0 Alpha released.
 * 06-02-2022 | SRK | Implemented Investor List functionality.
 * 06-02-2022 | SRK | Version 0.3.0 Alpha released.
 * 06-06-2022 | SRK | Updated to pull-style payouts.
 * 06-06-2022 | SRK | Updated documentation to NatSpec standard.
 * 06-06-2022 | SRK | Version 0.4.0 Alpha released.
 * 06-07-2022 | SRK | Updated to follow Solidity and Project Style Guides.
 * 06-10-2022 | SRK | Adjusted Image prices for readability.
 * 06-12-2022 | SRK | Updated fund withdrawal with more secure logic.
 * 06-27-2022 | SRK | Updated to follow Solidity and Project Style Guides.
 * 06-27-2022 | SRK | Refactored to follow Solidity and Project Style Guides.
 * 06-27-2022 | SRK | Documentation and Comments Updated.
 *
 * 06-27-2022 | SRK | Version 0.5.0 Alpha released.
 */

//* ----------------------------- Statistics ------------------------------ //
/**
 * @notice Current Gas Usage for version 0.5.0 Alpha - Optmizer: 1,000 Runs
 * ├─ deployment             -  avg: 5532461  avg (confirmed): 5532461  low: 5532461  high: 5532461  USD: $305.90
 * ├─ constructor            -  avg: 4687035  avg (confirmed): 4687035  low: 4687035  high: 4687035  USD: $259.16
 * ├─ mintArtwork            -  avg:  123686  avg (confirmed):  130520  low:   21629  high:  206497  USD:  $11.42
 * ├─ printInvestorList      -  avg:   24771  avg (confirmed):   24771  low:   23158  high:   26150  USD:   $1.45
 * ├─ name                   -  avg:   24519  avg (confirmed):   24519  low:   24519  high:   24519  USD:   $1.36
 * ├─ symbol                 -  avg:   24517  avg (confirmed):   24517  low:   24517  high:   24517  USD:   $1.36
 * ├─ tokenURI               -  avg:   24263  avg (confirmed):   25111  low:   22570  high:   25667  USD:   $1.42
 * ├─ artGallery             -  avg:   23478  avg (confirmed):   23478  low:   23478  high:   23478  USD:   $1.30
 * ├─ artist                 -  avg:   23280  avg (confirmed):   23280  low:   23280  high:   23280  USD:   $1.29
 * ├─ royaltyInfo            -  avg:   23026  avg (confirmed):   23026  low:   23026  high:   23026  USD:   $1.27
 * ├─ isInvestor             -  avg:   22707  avg (confirmed):   22707  low:   22707  high:   22707  USD:   $1.26
 * ├─ payoutsOwed            -  avg:   22696  avg (confirmed):   22696  low:   22696  high:   22696  USD:   $1.25
 * ├─ forcePayment           -  avg:   22602  avg (confirmed):   22003  low:   22003  high:   23653  USD:   $1.31
 * ├─ ownerOf                -  avg:   22506  avg (confirmed):   22506  low:   22506  high:   22506  USD:   $1.24
 * ├─ PROJECT_WALLET_ADDRESS -  avg:   22212  avg (confirmed):   22212  low:   22212  high:   22212  USD:   $1.23
 * ├─ supportsInterface      -  avg:   21903  avg (confirmed):   21903  low:   21795  high:   21958  USD:   $1.21
 * ├─ getContractBalance     -  avg:   21293  avg (confirmed):   21293  low:   21293  high:   21293  USD:   $1.18
 * └─ withdrawPayout         -  avg:   21158  avg (confirmed):   20609  low:   20609  high:   22258  USD:   $1.23
 * Note: USD Calculations based on Gas Price: 46 Wei and Ethereum price: $1202 from 6-27-2022.
 * Formula: TransactionCost =  (Gas (High) * Gas Price * Etherum USD Price) / 1,000,000,000
 */

//* ------------------------------- Tasks --------------------------------- //
/**
  * Update minting functions and counters to model the collection. - Complete 
  * (05/09/2022)
  * Add access control support. - Complete (05/10/2022)
  * Add royalty support. - Complete (05/15/2022)
  * Add Withdraw Payment functionality. - Complete (5/19/2022)
  * Implement Minting Payment Splits.  - Complete (5/19/2022)
  * Implement Royalty Payment Splits.  - Complete (5/19/2022)
  * Create/Add MoneyPipe Contract Address for Royalty Splits.  - Complete 
  * (5/19/2022)
  * Add Investor List functionality. - Complete (6/02/2022)
  * Clean up code and make self-documenting. - Complete (6/27/2022)
  * Todo: Update _baseURI to new IPFS metdata address.
  * Todo: Gas Optimization Passes.

*/

//* ------------------------------ Resources ------------------------------ //
/**
 * @notice Pragma statements tell the compiler to use the version of
 * solidity this contract was designed for.
 */
pragma solidity 0.8.15;

/**
 * @notice Import statements allow the contract to access features of
 * other contracts. Specifically OpenZeppelin's ERC721, ERC721Royalty, and
 * Ownable libraries.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

//* ------------------------------ Contract ------------------------------- //
/**
 * @notice the contract statement defines the contract's name, and the
 * libraries that it uses.
 */
contract ReneeLaneCollection is ERC721, ERC721Royalty, Ownable {
    //* -------------------------- Structs -------------------------------- //
    /**
     * @notice Structs represent items with specific properties. This contract
     * uses two structs to define the Artwork and the Artists.
     */

    /**
     * @notice The Artwork struct is used to define the properties that each piece
     * of Artwork in this collection must have. In this case each piece of artwork
     * has an imageNumber (1 through 50), a price in wei, a currentTokenID number
     * a lastTokenID number and an artistID number (1-5).
     */
    struct Artwork {
        uint64 imgNumber;
        uint64 price;
        uint64 currentTokenID;
        uint64 lastTokenID;
        uint256 artistID;
    }

    /**
     * @notice The Artist struct is used to define the properties for each
     * artist. In this case each artist has a directAddress where they will be
     * paid their portion of the minting proceeds and a RoyaltyAddress where
     * proceed from secondary sales will be split between the artist and the
     * project.
     */
    struct Artist {
        address directAddress;
        address royaltyAddress;
    }

    //* --------------------------- Arrays -------------------------------- //
    /**
     * @notice Arrays are used to store collections of items.
     */

    /**
     * @notice The investorList array is used to permanently store the
     * addresses of anyone who mints a art piece from this collection. This
     * array is used in the printInvestorList() function.
     */
    address[] public investorList;

    //* -------------------------- Mappings ------------------------------- //
    /**
     * @notice Mappings are gas effecient ways to store collections of items.
     * They are similar to Arrays but only return specific information based
     * on a key (or question) provided to them.
     */

    /**
     * @notice The artGallery mapping stores information about each piece of
     * artwork using the Artwork struct. When given an image number
     * (1 through 50)the mapping will return the imageNumber, price,
     * currentTokenID,lastTokenID, and artistID for that piece of art.
     */
    mapping(uint256 => Artwork) public artGallery;

    /**
     * @notice the isInvestoryapping stores information about each investor.
     * When given a wallet address it will return True if that address has
     * minted a piece of art from this collection. If they have not it will
     * return False.
     */
    mapping(address => bool) public isInvestor;

    /**
     * @notice The artist Mapping stores information about each artist. When
     * given an artistID (1-5) it will return the directAddress and
     * royaltyAddress for that artist.
     */
    mapping(uint256 => Artist) public artist;

    /**
     * @notice The payoutsOwed mapping stores the payouts owed to each artist
     * and to the project owner. When given a wallet address this mapping will
     * return the amount of ether (in wei) that is owed to that address.
     */
    mapping(address => uint256) public payoutsOwed;
    /**
     * @notice The isWhitelisted mapping stores the whitelist status of
     * addresses. These are addresses that are allowed to mint tokens prior
     * to the collection launch. When given a wallet address it will return
     * True if that address is whitelisted. If they are not it will return
     * False.
     */
    mapping(address => bool) public isWhitelisted;
    //* ----------------------- State Variables --------------------------- //
    // Stores the project's Wallet Address.
    address public PROJECT_WALLET_ADDRESS = (
        0xdD870fA1b7C4700F2BD7f44238821C26f7392148
    );

    //* --------------------------- Events -------------------------------- //
    event NewInvestorAdded(
        address indexed investorAddress,
        uint256 indexed tokenID
    );

    event PaymentSplit(
        uint256 totalValueReceived,
        address indexed artistAddress,
        int256 indexed artistCut,
        int256 indexed projectCut
    );

    //* ------------------------- Constructor ----------------------------- //
    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        //Intialize artist mapping
        artist[1] = Artist({
            directAddress: 0x33A4622B82D4c04a53e170c638B944ce27cffce3,
            royaltyAddress: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
        });
        artist[2] = Artist({
            directAddress: 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db,
            royaltyAddress: 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db
        });
        artist[3] = Artist({
            directAddress: 0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB,
            royaltyAddress: 0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB
        });
        artist[4] = Artist({
            directAddress: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2,
            royaltyAddress: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2
        });
        artist[5] = Artist({
            directAddress: 0x17F6AD8Ef982297579C203069C1DbfFE4348c372,
            royaltyAddress: 0x17F6AD8Ef982297579C203069C1DbfFE4348c372
        });

        // Initializes Artwork Struct Objects. I couldn't come up with a
        // better way to do this math. This works.
        artGallery[1] = Artwork(1, .12 ether, 1, 20, 1);
        for (uint64 index = 2; index <= 10; index++) {
            artGallery[index] = Artwork({
                imgNumber: index,
                price: .12 ether,
                currentTokenID: artGallery[index - 1].currentTokenID + 20,
                lastTokenID: artGallery[index - 1].lastTokenID + 20,
                artistID: 1
            });
        }
        for (uint64 index = 11; index <= 20; index++) {
            artGallery[index] = Artwork({
                imgNumber: index,
                price: .24 ether,
                currentTokenID: artGallery[index - 1].currentTokenID + 20,
                lastTokenID: artGallery[index - 1].lastTokenID + 20,
                artistID: 2
            });
        }
        artGallery[21] = Artwork(21, .36 ether, 401, 410, 3);
        for (uint64 index = 22; index <= 30; index++) {
            artGallery[index] = Artwork({
                imgNumber: index,
                price: .36 ether,
                currentTokenID: artGallery[index - 1].currentTokenID + 10,
                lastTokenID: artGallery[index - 1].lastTokenID + 10,
                artistID: 3
            });
        }
        artGallery[31] = Artwork(31, .48 ether, 501, 505, 4);
        for (uint64 index = 32; index <= 40; index++) {
            artGallery[index] = Artwork({
                imgNumber: index,
                price: .48 ether,
                currentTokenID: artGallery[index - 1].currentTokenID + 5,
                lastTokenID: artGallery[index - 1].lastTokenID + 5,
                artistID: 4
            });
        }
        artGallery[41] = Artwork(41, .6 ether, 551, 553, 5);
        for (uint64 index = 42; index <= 50; index++) {
            artGallery[index] = Artwork({
                imgNumber: index,
                price: .6 ether,
                currentTokenID: artGallery[index - 1].currentTokenID + 3,
                lastTokenID: artGallery[index - 1].lastTokenID + 3,
                artistID: 5
            });
        }
    }

    //* ---------------------- Public Functions -------------------------- //

    /**
     * @notice This function will mint a token of the specified image passed
     * to it.  It wll revert if the image number is out side of this
     * collection, if there are no tokens left for that image, or if the
     * minter failed to send enough ether to cover the price.
     *
     * @notice Following the minting the royalty information is set via the
     * _setTokenRoyalty() function inherited from OpenZeppelin's
     * ERC721Royalty extension.
     *
     * @notice Finally, The price of the image ii then transferred to a
     * MoneyPipe contract which pays out 90% to the project and a 10%
     * commision back to the artist.
     *
     * @param _imageNumber The number of the image the user wants to mint
     * (1-50).
     */
    function mintArtwork(uint256 _imageNumber) public payable {
        if (isWhitelisted[address(0)] == false) {
            require(
                isWhitelisted[msg.sender] == true,
                "You are not whitelisted"
            );
        }
        require(
            _imageNumber > 0 && _imageNumber < 51,
            "The image you have selected does not exist in this collection."
        );
        uint64 _newTokenID = artGallery[_imageNumber].currentTokenID;
        require(
            _newTokenID <= artGallery[_imageNumber].lastTokenID,
            "No more editions of this image are available."
        );
        require(
            msg.value == artGallery[_imageNumber].price,
            "You didn't send the correct amount of Ether."
        );
        Artist memory _artist = artist[artGallery[_imageNumber].artistID];
        splitPayment(_artist.directAddress, msg.value);
        _safeMint(msg.sender, _newTokenID);
        _setTokenRoyalty(_newTokenID, _artist.royaltyAddress, 1000);
        if (!isInvestor[msg.sender]) {
            addNewInvestor(msg.sender, _newTokenID);
        }
        artGallery[_imageNumber].currentTokenID++;
    }

    /**
     * @notice The tokenURI() function works in conjunction with the
     * _baseURI() function to set the tokenURI address for the specified
     * token.
     *
     * @param tokenID - The number of the token for which the URI is being
     * set.
     *
     * @return string - The full tokenURI address for the specified token.
     *
     */
    function tokenURI(uint256 tokenID)
        public
        view
        virtual
        override
        returns (string memory)
    {
        require(
            _exists(tokenID),
            "ERC721Metadata: URI query for nonexistent token"
        );

        string memory baseURI = _baseURI();
        return
            string(
                abi.encodePacked(baseURI, Strings.toString(tokenID), ".json")
            );
    }

    /**
     * @notice The printInvestorList() function will return each address
     * stored in the investorList[] array.
     *
     * @return allInvestors The address stored on the investorList[] array.
     *
     */
    function printInvestorList()
        public
        view
        returns (address[] memory allInvestors)
    {
        return investorList;
    }

    /**
     * @notice The withdrawPayout() function can be called by anyone, it will
     * check to see if the caller's wallet address is owed any funds. If so
     * those funds will paid out and the balance of that wallet address will
     * be set to 0. If no money is owed to that address the transaction is
     * reverted.
     *
     *
     */
    function withdrawPayout() public {
        require(address(this).balance > 0, "No money in contract.");
        require(payoutsOwed[msg.sender] > 0, "No funds owed to this wallet.");
        payable(msg.sender).transfer(payoutsOwed[msg.sender]);
        payoutsOwed[msg.sender] = 0;
    }

    /**
     * @notice The forcePayment() function pays out the balance owed to the
     * specified artist and sets their owed balance to 0. These balances
     * are stored inside the Artist struct.
     *
     * @notice This is an internal function which is not called on it's
     * own, it is called as part of the payoutFunds() function.
     *
     * @param _address The address of the wallet you want to force payment to.
     *
     */
    function forcePayment(address _address) public onlyOwner {
        require(payoutsOwed[_address] > 0, "No money owed to this address.");
        payable(_address).transfer(uint256(payoutsOwed[_address]));
        payoutsOwed[_address] = 0;
    }

    /**
     * @notice The getContractBalance() function returns current amount of
     * Ether stored in the contract.
     *
     * @return contractBalance The amount of Ether (in Wei)
     *
     */
    function getContractBalance()
        public
        view
        returns (uint256 contractBalance)
    {
        return address(this).balance;
    }

    /**
     * @notice The supportsInterface() function returns 'true' for supported
     * interfaces. Returns 'false' if the interface is not supported.
     *
     * @param interfaceID The 4 byte identifier for an interface.
     *
     * @return bool A True of False value.
     *
     */
    function supportsInterface(bytes4 interfaceID)
        public
        view
        override(ERC721, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceID);
    }

    /**
     * @notice The addToWhitelist() function sets the isWhiteListed mapping to
     * return true for the specified address.
     *
     * @param _address The address you want to add to the whitelist.
     */
    function addToWhitelist(address _address) public onlyOwner {
        require(
            !isWhitelisted[_address],
            "Address is already on the whitelist."
        );
        isWhitelisted[_address] = true;
    }

    function removeFromWhitelist(address _address) public onlyOwner {
        require(isWhitelisted[_address], "Address is not on the whitelist.");
        isWhitelisted[_address] = false;
    }

    //* --------------------- Internal Functions -------------------------- //
    /**
     * @notice The _baseURI() function sets the base IPFS address where this
     * collection's metadata is stored.
     *
     * @return string The baseURI address.
     *
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"; // Old URI
    }

    /**
     * @notice The _burn() function allows token owners to destroy the
     * specified token which they own. The Royalty information for that token
     * will also be removed. WARNING: This is irreversible. If you burn your
     * token it can NEVER be recovered.
     *
     * @param tokenID The token ID which is to be destroyed.
     *
     */
    function _burn(uint256 tokenID)
        internal
        virtual
        override(ERC721, ERC721Royalty)
    {
        super._burn(tokenID);
        _resetTokenRoyalty(tokenID);
    }

    /**
     * @notice The splitPayment() function splits the minting payment
     * between the artist and project wallet.
     *
     * @param _artistDirectAddress The address of the artist's wallet.
     *
     * @param valueSent The amount of Ether paid to mint the artwork.
     *
     */
    function splitPayment(address _artistDirectAddress, uint256 valueSent)
        internal
    {
        int256 _artistCut = int256(valueSent) / 10**1;
        int256 _projectCut = (int256(valueSent) - _artistCut);
        payoutsOwed[_artistDirectAddress] += uint256(_artistCut);
        payoutsOwed[PROJECT_WALLET_ADDRESS] += uint256(_projectCut);
        emit PaymentSplit(
            valueSent,
            _artistDirectAddress,
            _artistCut,
            _projectCut
        );
    }

    /**
     * @notice The addNewInvestor() function adds a new investor to the
     * isInvestor mapping and InvestorList array. This is an internal function
     * which can only be called by the contract itself. It is called as part
     * of the mintArtwork() function.
     *
     * This functions emits the NewInvestorAdded event.
     *
     * @param _minterAddress Wallet address of the person who minted the
     * artwork.
     *
     */
    function addNewInvestor(address _minterAddress, uint64 _tokenID) internal {
        isInvestor[_minterAddress] = true;
        investorList.push(_minterAddress);
        emit NewInvestorAdded(_minterAddress, _tokenID);
    }
}
