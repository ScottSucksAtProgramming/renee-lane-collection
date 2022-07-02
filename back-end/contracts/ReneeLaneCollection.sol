// SPDX-License-Identifier: MIT
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
 * @notice Version 0.5.0 alpha
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
 * 06-29-2022 | SRK | Added Whitelist Functionality.
 * 06-30-2022 | SRK | Version 0.5.0 Alpha released.
 */

//* ----------------------------- Statistics ------------------------------ //
/**
 * @notice Current Gas Usage for version 0.5.0 Alpha - Optmizer: 1,000 Runs
 * ├─ deployment             -  avg: 5993711  avg (confirmed): 5993711  low: 5993711  high: 5993711 USD: $113.82
 * ├─ constructor            -  avg: 4882094  avg (confirmed): 4882094  low: 4882094  high: 4882094 USD:  $92.71
 * ├─ mintArtwork            -  avg:  139811  avg (confirmed):  153717  low:   22479  high:  211063 USD:   $4.01
 * ├─ addToWhitelist         -  avg:   43341  avg (confirmed):   44218  low:   22728  high:   44439 USD:   $0.84
 * ├─ withdrawPayout         -  avg:   26814  avg (confirmed):   29073  low:   21398  high:   48446 USD:   $0.92
 * ├─ transferOwnership      -  avg:   26474  avg (confirmed):   30154  low:   22794  high:   30154 USD:   $0.57
 * ├─ printInvestorList      -  avg:   24716  avg (confirmed):   24716  low:   23203  high:   26195 USD:   $0.50
 * ├─ name                   -  avg:   24519  avg (confirmed):   24519  low:   24519  high:   24519 USD:   $0.47
 * ├─ symbol                 -  avg:   24495  avg (confirmed):   24495  low:   24495  high:   24495 USD:   $0.47
 * ├─ tokenURI               -  avg:   24221  avg (confirmed):   25059  low:   22548  high:   25609 USD:   $0.49
 * ├─ artGallery             -  avg:   23456  avg (confirmed):   23456  low:   23456  high:   23456 USD:   $0.44
 * ├─ artist                 -  avg:   23280  avg (confirmed):   23280  low:   23280  high:   23280 USD:   $0.45
 * ├─ forcePayment           -  avg:   23139  avg (confirmed):   23076  low:   22752  high:   23656 USD:   $0.44
 * ├─ royaltyInfo            -  avg:   23020  avg (confirmed):   23020  low:   23014  high:   23026 USD:   $0.43
 * ├─ isInvestor             -  avg:   22751  avg (confirmed):   22751  low:   22751  high:   22763 USD:   $0.43
 * ├─ isWhitelisted          -  avg:   22742  avg (confirmed):   22742  low:   22742  high:   22742 USD:   $0.43
 * ├─ payoutsOwed            -  avg:   22741  avg (confirmed):   22741  low:   22741  high:   22741 USD:   $0.42
 * ├─ ownerOf                -  avg:   22484  avg (confirmed):   22484  low:   22484  high:   22484 USD:   $0.42
 * ├─ PROJECT_WALLET_ADDRESS -  avg:   22190  avg (confirmed):   22190  low:   22190  high:   22190 USD:   $0.42
 * ├─ owner                  -  avg:   22140  avg (confirmed):   22140  low:   22140  high:   22140 USD:   $0.41
 * ├─ supportsInterface      -  avg:   21903  avg (confirmed):   21903  low:   21795  high:   21958 USD:   $0.42
 * ├─ getContractBalance     -  avg:   21358  avg (confirmed):   21358  low:   21358  high:   21358 USD:   $0.41
 * ├─ removeFromWhitelist    -  avg:   20416  avg (confirmed):   14749  low:   14749  high:   23706 USD:   $0.45
 * └─ renounceOwnership      -  avg:   18500  avg (confirmed):   14775  low:   14775  high:   22226 USD:   $0.42
 * Note: USD Calculations based on Gas Price: 35 Wei and Ethereum price: $1208 from 6-26-2022.
 * Formula: TransactionCost =  (Gas (High) * Gas Price * Etherum USD Price) / 1,000,000,000
 */

//* ------------------------------- Tasks --------------------------------- //
/**
 * Todo: Release version 0.5.0 alpha
 * Todo: Deploy Renee Lane Collection contract for Beta testing.
 * Todo: Begin preparing for beta release.
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
 * @notice The contract statement defines the contract's name, and the
 * libraries that it uses.
 *
 * @notice The Renee Lane Collection inherits OpenZeppelin's ERC721,
 * ERC721Royalty, and Ownable extensions to ensure compliance to the current
 * standards and provide a strong securit basis with code that has been vetted
 * elsewhere.
 */
contract ReneeLaneCollection is ERC721, ERC721Royalty, Ownable {
    //* ------------------------ Data Structures --------------------------- //
    /**
     * @notice Data structures are used to store data in the contract. They
     * represent real world objects in the code. In this contract there are
     * stuctures which represent pieces of artwork and the artists. There are
     * additional structures which represent collection investors, the art
     * gallery where the collection is managed, a whitelist of people who can
     * invest in the collection early, and a ledger which tracks the
     * collection's payouts owed to the artists and the project owner.
     */

    //* --------------------------- Structs -------------------------------- //
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
     * @notice The artist Mapping stores information about each artist. When
     * given an artistID (1-5) it will return the directAddress and
     * royaltyAddress for that artist.
     */
    mapping(uint256 => Artist) public artist;

    /**
     * @notice the isInvestoryapping stores information about each investor.
     * When given a wallet address it will return True if that address has
     * minted a piece of art from this collection. If they have not it will
     * return False.
     */
    mapping(address => bool) public isInvestor;

    /**
     * @notice The isWhitelisted mapping stores the whitelist status of
     * addresses. These are addresses that are allowed to mint tokens prior
     * to the collection launch. When given a wallet address it will return
     * True if that address is whitelisted. If they are not it will return
     * False.
     */
    mapping(address => bool) public isWhitelisted;

    /**
     * @notice The payoutsOwed mapping stores the payouts owed to each artist
     * and to the project owner. When given a wallet address this mapping will
     * return the amount of ether (in wei) that is owed to that address.
     */
    mapping(address => uint256) public payoutsOwed;

    //* ----------------------- State Variables --------------------------- //
    /**
     * @notice The PROJECT_OWNER_ADDRESS is address of the project owner. It
     * cannot be changed after the contract is deployed. Funds owed to the
     * project owner are paid to this address.
     */
    address public PROJECT_WALLET_ADDRESS = (
        0xdD870fA1b7C4700F2BD7f44238821C26f7392148
    );

    //* --------------------------- Events -------------------------------- //
    /**
     * @notice Events are used to log important updates about what The Renee
     * Lane Collection is doing. When an event is triggered it will log the
     * information permanently on the blockchain.
     */

    /**
     * @notice The NewInvestorAdded event is triggered when a new investor is
     * added to the investor list and mapping. It logs the investor's address
     * and the token ID of the first piece of art they minted.
     *
     * @notice The NewInvestorAdded event is triggered when addNewInvestor()
     * function is called.
     */
    event NewInvestorAdded(
        address indexed investorAddress,
        uint256 indexed tokenID
    );
    /**
     * @notice The PaymentSplit event is triggered when a minting payment is
     * received and split between the artist and the project owner. It logs
     * the amount of ether (in wei) that is due to the artist and the amount
     * that is due to the project owner.
     *
     * @notice The PaymentSplit event is trigged when the splitPayment()
     * function is called.
     */
    event PaymentSplit(
        uint256 totalValueReceived,
        address indexed artistAddress,
        int256 indexed artistCut,
        int256 indexed projectCut
    );
    /**
     * @notice the PayoutSent event is triggered when a payout is sent from
     * the contract. It logs the address of the person who initiated the
     * payout, the address of the recipient and the amount of ether (in wei)
     * that was sent.
     *
     * @notice The PayoutSent event is triggered when the withdrawPayout() or
     * forcePayment() functions are called.
     */
    event PayoutSent(
        address indexed caller,
        address indexed recipientAddress,
        uint256 indexed amount
    );

    //* ------------------------- Constructor ----------------------------- //
    /**
     * @notice The constructor helps set up the initial state of the smart
     * contract. It is called when the contract is deployed.
     *
     * @notice It first sets the name of the Art Collection and the Symbol the
     * tokens will have.
     */
    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        /**
         * @notice Here the constructor populates the artist mapping by
         * assigning the direct and royalty addresses to each artist by their
         * ID number.
         */
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

        /**
         * @notice Here the constructor populates the artGallery mapping by
         * creating Artwork objects for each image in the collection. The image
         * number, price, starting token ID, and artist who created the image
         * are all assigned. The lastTokenID is also set which limits the
         * number of tokens that can be minted for that piece of art.
         */
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

    //* --------------------- External Functions -------------------------- //
    /**
     * @notice External functions can ONLY be called from other contracts, or
     * users.
     */

    /**
     * @notice The mintImage() function was renamed to mintArtwork() to better
     * fit the theme of the project. The minter must specify the number of the
     * image they wish to purchse, and pay the correct amount of Ether.
     *
     * @notice The function will check to see if the minter is authorized to
     * mint the image by checking the isWhitelisted mapping. It insures that
     * the minter has selected an art piece contained within the collection
     * and that there are still editions of that artpiece available.
     *
     * @notice If all checks are passed the token will be minted and assigned
     * to the minter via the _safeMint() function inherited from
     * OpenZeppelin's ERC721 contract. Royalty preferences for that token are
     * set using the _setTokenRoyalty() function inherited from OpenZeppelin's
     * ERC721Royalty contract and by using the ERC2981 royalty standard.
     *
     * @notice If this is the first artpiece purchased by the minter their
     * address will be added to the investorList and isInvestor mapping.
     *
     * @notice The payment received from the minter is split between the
     * artist and the PROJECT_WALLET_ADDRESS using the splitPayment()
     * function. These payouts can be withdrawn later.
     *
     * @notice Finally the mintArtwork() function increments the
     * currentTokenID for that artpiece removing one edition of that image
     * from the amount available.
     *
     * @param _imageNumber The number of the image the user wants to mint
     * (1-50).
     */
    function mintArtwork(uint256 _imageNumber) external payable {
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
        _safeMint(msg.sender, _newTokenID);
        _setTokenRoyalty(_newTokenID, _artist.royaltyAddress, 1000);
        if (!isInvestor[msg.sender]) {
            addNewInvestor(msg.sender, _newTokenID);
        }
        splitPayment(_artist.directAddress, msg.value);
        artGallery[_imageNumber].currentTokenID++;
    }

    /**
     * @notice The withdrawPayout() function allows the caller to withdraw the
     * Ether owed to them. This function can be called by anyone but will
     * revert if no money is owed to them or if there is no Ether stored in
     * the contract. When called by the owner they payment will be disbursed
     * to the PROJECT_WALLET_ADDRESS, otherwise payment will be disbursed to
     * the caller's address.
     *
     * @notice Once the payment has been sent the PayoutSent event is
     * triggered to log the payout. The balance owed to that address is set to
     * 0.
     */
    function withdrawPayout() external {
        require(getContractBalance() > 0, "No money in contract.");
        address _address;
        if (msg.sender == owner()) {
            _address = PROJECT_WALLET_ADDRESS;
        } else {
            _address = msg.sender;
        }
        uint256 _amount = payoutsOwed[_address];
        require(_amount > 0, "No funds owed to this wallet.");
        payable(_address).transfer(_amount);
        emit PayoutSent(msg.sender, _address, _amount);
        payoutsOwed[_address] = 0;
    }

    //* -------------------- OnlyOwner Functions -------------------------- //
    /**
     * @notice OnlyOwner functions are only callable by the owner of the
     * contract. They are subclass of External Functions.
     */

    /**
     * @notice The addToWhitelist() function allows the contract owner to
     * authorize new addresses to mint tokens early by setting their address
     * to return True from the isWhitelisted mapping.
     *
     * @notice The function will first check to ensure the address is not
     * already whitelisted. This function can only be called by the owner.
     *
     *! @notice Note: If the owner adds the Zero Address to the whitelist the
     *! mintArtwork() function will allow ALL addresses to mint artwork.
     *
     * @param _address The address to be added to the whitelist.
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(
            !isWhitelisted[_address],
            "Address is already on the whitelist."
        );
        isWhitelisted[_address] = true;
    }

    /**
     * @notice The removeFromWhitelist() function allows the contract owner to
     * deauthorize an address from minting tokens early by setting their
     * address to return False from the isWhitelisted mapping.
     *
     * @notice The function will first check to ensure the address is
     * currently on the whitelist. This function can only be called by the
     * owner.
     *
     * @param _address The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(isWhitelisted[_address], "Address is not on the whitelist.");
        isWhitelisted[_address] = false;
    }

    /**
     * @notice The forcePayment() function allows the contract owner to force
     * a payment to be sent to an address they specify. This function can only
     * be called by the owner and is designed to be used in a situation where
     * the artist cannot request their own payout using the withdrawPayout()
     * function.
     *! @notice This function is less secure than withdrawPayout() and should
     *! only be used when absolutely necessary. It does not follow the
     *! recommended pull design pattern.
     *
     * @notice This function will revert if no payment is owed to the
     * specified address, or when the caller is not the owner. After paying
     * the specified address, a PayoutSent event is triggered and the balance
     * owed to that address is set to 0.
     *
     * @param _addressToBePayed The address of the wallet payment will be sent
     * to.
     *
     */
    function forcePayment(address _addressToBePayed) external onlyOwner {
        uint256 _amountOwed = payoutsOwed[_addressToBePayed];
        require(_amountOwed > 0, "No money owed to this address.");
        payable(_addressToBePayed).transfer(_amountOwed);
        emit PayoutSent(msg.sender, _addressToBePayed, _amountOwed);
        payoutsOwed[_addressToBePayed] = 0;
    }

    //* ---------------------- Public Functions -------------------------- //
    /**
     * @notice Public functions can be seen and called from other contracts,
     * users as well as from the contract itself.
     */

    /**
     * @notice The getContractBalance() function returns the current balance
     * of Ether (in Wei) currently stored in the contract.
     *
     * @return contractBalance The amount of Ether (in Wei)
     */
    function getContractBalance()
        public
        view
        returns (uint256 contractBalance)
    {
        return address(this).balance;
    }

    /**
     * @notice The printInvestosList() function returns the list of investor
     * addresses from the investorList array.
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
     * @notice The tokenURI() function returns the Token URI for the specified
     * tokenID. It will revert if the tokenID provided does not exist.
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

    //* --------------------- Internal Functions -------------------------- //
    /**
     * @notice Internal functions are only callable by the contract itself.
     * They are not available to users, the owner, or other contracts.
     */

    /**
     * @notice The addNewInvestor() function will add a new investor to the
     * investorList and set their isInvestor mapping result to true.
     *
     * @notice This function emits the NewInvestorAdded event.
     *
     * @param _minterAddress Wallet address of the person who minted the
     * artwork.
     *
     * @param _tokenID the tokenID of the artwork they minted.
     */
    function addNewInvestor(address _minterAddress, uint64 _tokenID) internal {
        isInvestor[_minterAddress] = true;
        investorList.push(_minterAddress);
        emit NewInvestorAdded(_minterAddress, _tokenID);
    }

    /**
     * @notice The _baseURI() function returns the IPFS address where this
     * collection's metadata and assets are stored.
     *
     * @return string The baseURI address.
     *
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"; // Old URI
    }

    /**
     * @notice The _burn() function is used to burn a token. This is function
     * which is required by the libraries this contract uses to interact with
     * the blockchain but there is no way to call this function
     * (or to burn tokens) for artwork from this collection.
     *
     * @notice If a token is burned it will be removed from the collection,
     * the royalty information will be erased.
     *
     *! @notice Burning a token is irreversible. If you burn your token it can
     *! NEVER be recovered.
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
     * @notice The splitPayment() function splits payments received during
     * the minting process. The artist receives 10% of the payment, and the
     * project receives the remaining 90%.
     *
     * @notice This function emits the PayoutSplit event.
     *
     * @param _artistDirectAddress The address of the artist's wallet.
     *
     * @param valueSent The amount of Ether received when the artwork was
     * minted.
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
}
