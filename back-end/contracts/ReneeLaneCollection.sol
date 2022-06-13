/// SPDX-License-Identifier: MIT
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
 * @notice This is a bespoke smart contract written to manage NFTs for The
 * Renee Lane Collection, a 50 piece art gallery created by women artists
 * from all over the world. Funds invested into this collection will be used
 * to finance an independent film being produced by Ms. Viola Voltairine and
 * ArtVamp Productions.
 *
 * @notice This contract mints a limited number of tokens per image, sets
 * royalties via the ERC-2981 standard, accept payments for minting and
 * disperses 10% of those funds directly to wallets owned by the artists
 * when funds are withdrawn. It also maintains a list of addresses of anyone
 * who mints an image so they can permanently retain the benefits associated
 * with investing in this collection.
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
 * 05-18-2022 | SRK | mintImage() gas optimization pass.
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
 */

//* ----------------------------- Statistics ------------------------------ //
/**
  * Current Statistics as of 0.4.0 Alpha - Optmizer: 1000 Runs
  * Deployment Cost  |   5,517,795 Gas   | Approx: $331.07
  * 1st Minting Cost |     249,379 Gas   | Approx:  $14.96
  * Additional Mints |     116,244 Gas   | Approx:   $6.97
  * Withdraw Funds   |      38,509 Gas   | Approx:   $2.31

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
  * Todo: Update _baseURI to new IPFS metdata address.
  * Todo: Gas Optimization Passes.
  * Todo: Clean up code and make self-documenting.

*/

//* ------------------------------ Resources ------------------------------ //

pragma solidity 0.8.14;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";

//* ------------------------------ Contract ------------------------------- //

contract ReneeLaneCollection is ERC721, ERC721Royalty, Ownable {
    //* -------------------------- Structs -------------------------------- //
    // Image information stored here. Packages into single 256byte container
    // when compiled.
    struct Image {
        uint64 imgNumber;
        uint64 price;
        uint64 currentTokenID;
        uint64 lastTokenID;
        uint256 artistID;
    }

    struct Artist {
        address directAddress;
        address royaltyAddress;
    }

    //* --------------------------- Arrays -------------------------------- //
    address[] public investorList;

    //* -------------------------- Mappings ------------------------------- //
    // Stores Image objects for each image by imageNumber.
    mapping(uint256 => Image) imageGallery;

    // Stores a list of investors
    mapping(address => bool) investors;

    mapping(uint256 => Artist) artist;

    mapping(address => uint256) payoutsOwed;
    //* -------------------------- Variables ------------------------------ //
    // Stores the project's Wallet Address.
    address PROJECT_WALLET_ADDRESS = (
        0xdD870fA1b7C4700F2BD7f44238821C26f7392148
    );

    //* --------------------------- Events -------------------------------- //

    //* ------------------------- Constructor ----------------------------- //
    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        //Intialize Artist
        artist[1] = Artist({
            directAddress: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2,
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

        // Initializes Image Struct Objects. I couldn't come up with a
        // better way to do this math. This works.
        imageGallery[1] = Image(1, .12 ether, 1, 20, 1);
        for (uint64 index = 2; index <= 10; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: .12 ether,
                currentTokenID: imageGallery[index - 1].currentTokenID + 20,
                lastTokenID: imageGallery[index - 1].lastTokenID + 20,
                artistID: 1
            });
        }
        for (uint64 index = 11; index <= 20; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: .24 ether,
                currentTokenID: imageGallery[index - 1].currentTokenID + 20,
                lastTokenID: imageGallery[index - 1].lastTokenID + 20,
                artistID: 2
            });
        }
        imageGallery[21] = Image(21, .36 ether, 401, 410, 3);
        for (uint64 index = 22; index <= 30; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: .36 ether,
                currentTokenID: imageGallery[index - 1].currentTokenID + 10,
                lastTokenID: imageGallery[index - 1].lastTokenID + 10,
                artistID: 3
            });
        }
        imageGallery[31] = Image(31, .48 ether, 501, 505, 4);
        for (uint64 index = 32; index <= 40; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: .48 ether,
                currentTokenID: imageGallery[index - 1].currentTokenID + 5,
                lastTokenID: imageGallery[index - 1].lastTokenID + 5,
                artistID: 4
            });
        }
        imageGallery[41] = Image(41, .6 ether, 551, 553, 5);
        for (uint64 index = 42; index <= 50; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: .6 ether,
                currentTokenID: imageGallery[index - 1].currentTokenID + 3,
                lastTokenID: imageGallery[index - 1].lastTokenID + 3,
                artistID: 5
            });
        }
    }

    //* ---------------------- Minting Functions -------------------------- //

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
     * @notice Finally, The price of the image is then transferred to a
     * MoneyPipe contract which pays out 90% to the project and a 10%
     * commision back to the artist.
     *
     * @param _imageNumber The number of the image the user wants to mint
     * (1-50).
     */
    function mintImage(uint256 _imageNumber) public payable {
        require(
            _imageNumber > 0 && _imageNumber < 51,
            "The image you have selected does not exist in this collection."
        );
        uint64 _newTokenID = imageGallery[_imageNumber].currentTokenID;
        require(
            _newTokenID <= imageGallery[_imageNumber].lastTokenID,
            "No more editions of this image are available."
        );
        require(
            msg.value >= imageGallery[_imageNumber].price,
            "You didn't send enough Ether."
        );
        Artist memory _artist = artist[imageGallery[_imageNumber].artistID];
        int256 _artistCut = int256(msg.value) / 10**1;
        int256 _projectCut = int256(msg.value) - _artistCut;
        payoutsOwed[_artist.directAddress] += uint256(_artistCut);
        payoutsOwed[PROJECT_WALLET_ADDRESS] += uint256(_projectCut);
        _safeMint(msg.sender, _newTokenID);
        _setTokenRoyalty(_newTokenID, _artist.royaltyAddress, 1000);
        if (!investors[msg.sender]) {
            investors[msg.sender] = true;
            investorList.push(msg.sender);
        }
        imageGallery[_imageNumber].currentTokenID = _newTokenID + 1;
    }

    //* --------------------- Metadata Functions -------------------------- //
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
            bytes(baseURI).length > 0
                ? string(
                    abi.encodePacked(
                        baseURI,
                        Strings.toString(tokenID),
                        ".json"
                    )
                )
                : "";
    }

    //* --------------------- Investor Functions -------------------------- //
    /**
     * @notice The isInvestor() function will check to see if a specified
     * address is listed as an original investor in this collection.
     *
     * @param _possibleInvestor Wallet address of possible investor.
     *
     * @return isAnInvestor True/False value
     *
     */
    function isInvestor(address _possibleInvestor)
        public
        view
        returns (bool isAnInvestor)
    {
        return investors[_possibleInvestor];
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

    //* ------------------ Administrative Functions ----------------------- //
    /**
     * @notice The checkArtisBalances() function will return the current
     * balance of Ether (from the Artist struct) owed to the specified
     * artist.
     *
     * @param _artistID - The numberic identifier for the artist (1-5).
     *
     * @return balanceOwed - The amount of Ether (in Wei) owed to the artist.
     *
     */
    function checkArtisBalances(uint256 _artistID)
        public
        view
        returns (uint256 balanceOwed)
    {
        return payoutsOwed[artist[_artistID].directAddress];
    }

    /**
     * @notice The withdrawFunds() function can be called by anyone, it will
     * check to see if the caller's wallet address is owed any funds. If so
     * those funds will paid out and the balance of that wallet address will
     * be set to 0. If no money is owed to that address the transaction is 
     * reverted.
     *
     *
     */
    function withdrawFunds() public {
        require(payoutsOwed[msg.sender] > 0, "No funds owed to this wallet.");
        require(address(this).balance > 0, "No Funds to Pay Out");
        payable(msg.sender).transfer(payoutsOwed[msg.sender]);
        payoutsOwed[msg.sender] = 0;
    }

    /**
     * @notice The payArtist() function pays out the balance owed to the
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
     * @notice The getImageInfo() function returns the image information for
     * a specified image.
     *
     * @notice This information comes from both the Image Struct and the
     * Artist Struct.
     *
     * @param _imageNumber The number of the image (1-50) you wish to
     * obtain information about.
     *
     * @return imgNumber The image number.
     * @return price The minimum price of the image (in wei).
     * @return currentTokenID The next token Id to be minted.
     * @return artistID The number (1-5) of the artist who created the
     * image.
     * @return artistWalletAddress The address of the artist's wallet.
     * @return royaltyPayoutAddress The address where royalties are paid
     * (Moneypipe Splitter).
     */
    function getImageInfo(uint256 _imageNumber)
        public
        view
        returns (
            uint64 imgNumber,
            uint64 price,
            uint64 currentTokenID,
            uint256 artistID,
            address artistWalletAddress,
            address royaltyPayoutAddress
        )
    {
        return (
            imageGallery[_imageNumber].imgNumber,
            imageGallery[_imageNumber].price,
            imageGallery[_imageNumber].currentTokenID,
            imageGallery[_imageNumber].artistID,
            artist[imageGallery[_imageNumber].artistID].directAddress,
            artist[imageGallery[_imageNumber].artistID].royaltyAddress
        );
    }

    /**
     * @notice The getContractBalance() function returns current amount of
     * Ether stored in the contract.
     *
     * @return ContractBalance The amount of Ether (in Wei)
     *
     */
    function getContractBalance()
        public
        view
        onlyOwner
        returns (uint256 ContractBalance)
    {
        return address(this).balance;
    }

    //* ---------------------- Royalty Functions -------------------------- //
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
}
