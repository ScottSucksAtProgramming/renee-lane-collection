// SPDX-License-Identifier: MIT

//* ----------------------------- Documentation --------------------------- //
// Module:  ReneeLaneCollection.sol
// This is a smart contract which creates ERC-721 non-fungible tokens. It was
// originally written as a test contract used in the Scott's Puppy Mill
// project. It is being repurposed and expanded upon for use in the Renee Lane Collection.
//
// Current Statistics as of 0.2.0 Alpha - Optmizer: 1000 Runs
// Deployment Cost  |   6,165,943 Gas   | Approx: $370.00
// 1st Minting Cost |     127,008 Gas   | Approx:   $7.62
// Additional Mints |     107,343 Gas   | Approx:   $6.44
//
//
// Modification History
// 04-28-2022 | SRK | Project Created.
// 04-30-2022 | SRK | Added counters to a struct to help save gas.
// 05-03-2022 | SRK | Code imported into Renee Lane Collection Project.
// 05-09-2022 | SRK | Minting Function Completed.
// 05-10-2022 | SRK | Contract Ownership Functionality Added.
// 05-15-2022 | SRK | Royalty Functionality Added.
// 05-15-2022 | SRK | Version 0.1.0 Alpha released.
// 05-18-2022 | SRK | mintImage() gas optimization pass.
// 05-19-2022 | SRK | Implemented Minting and Royalty Payouts.
// 05-19-2022 | SRK | Version 0.2.0 Alpha released.

//* ------------------------------- Tasks --------------------------------- //
// Update minting functions and counters to model the collection. - Complete (05/09/2022)
// Add access control support. - Complete (05/10/2022)
// Add royalty support. - Complete (05/15/2022)
// Add Withdraw Payment functionality. - Complete (5/19/2022)
// Implement Minting Payment Splits.  - Complete (5/19/2022)
// Implement Royalty Payment Splits.  - Complete (5/19/2022)
// Create/Add MoneyPipe Contract Address for Royalty Splits.  - Complete (5/19/2022)
// Todo: Update _baseURI to new IPFS metdata address.
// Todo: Add Investor List functionality.
// Todo: Gas Optimization Passes.
// Todo: Clean up code and make self-documenting.

//* ----------------------------- Resources ------------------------------- //
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";

//* ----------------------------- Contract -------------------------------- //
contract ReneeLaneCollection is ERC721, ERC721Royalty, Ownable {
    //* ---------------------------- Variables ---------------------------- //
    // Image information stored here. Packages into single 256byte container
    // when compiled.
    struct Image {
        uint64 imgNumber;
        uint64 price;
        uint64 currentTokenId;
        uint64 lastTokenId;
        address mintingPayoutAddress;
        address royaltyPayoutAddress;
    }

    //* ---------------------------- Mappings ----------------------------- //
    // Stores Image objects for each image by imageNumber.
    mapping(uint256 => Image) imageGallery;

    //* ------------------------------ Events ----------------------------- //

    //* --------------------------- Contructor ---------------------------- //
    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        // Initializes Image Struct Objects. I couldn't come up with a
        // better way to do this math. This works.
        //! All of these addresses must be changed for the production version
        //! or your Ether will be lost.
        imageGallery[1] = Image(
            1,
            120000000000000000,
            1,
            20,
            0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2,
            0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
        );
        for (uint64 index = 2; index <= 10; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 120000000000000000,
                currentTokenId: imageGallery[index - 1].currentTokenId + 20,
                lastTokenId: imageGallery[index - 1].lastTokenId + 20,
                mintingPayoutAddress: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2,
                royaltyPayoutAddress: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
            });
        }
        for (uint64 index = 11; index <= 20; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 240000000000000000,
                currentTokenId: imageGallery[index - 1].currentTokenId + 20,
                lastTokenId: imageGallery[index - 1].lastTokenId + 20,
                mintingPayoutAddress: 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db,
                royaltyPayoutAddress: 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db
            });
        }
        imageGallery[21] = Image(
            21,
            360000000000000000,
            401,
            410,
            0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB,
            0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB
        );
        for (uint64 index = 22; index <= 30; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 360000000000000000,
                currentTokenId: imageGallery[index - 1].currentTokenId + 10,
                lastTokenId: imageGallery[index - 1].lastTokenId + 10,
                mintingPayoutAddress: 0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB,
                royaltyPayoutAddress: 0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB
            });
        }
        imageGallery[31] = Image(
            31,
            480000000000000000,
            501,
            505,
            0x617F2E2fD72FD9D5503197092aC168c91465E7f2,
            0x617F2E2fD72FD9D5503197092aC168c91465E7f2
        );
        for (uint64 index = 32; index <= 40; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 480000000000000000,
                currentTokenId: imageGallery[index - 1].currentTokenId + 5,
                lastTokenId: imageGallery[index - 1].lastTokenId + 5,
                mintingPayoutAddress: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2,
                royaltyPayoutAddress: 0x617F2E2fD72FD9D5503197092aC168c91465E7f2
            });
        }
        imageGallery[41] = Image(
            41,
            600000000000000000,
            551,
            553,
            0x17F6AD8Ef982297579C203069C1DbfFE4348c372,
            0x17F6AD8Ef982297579C203069C1DbfFE4348c372
        );
        for (uint64 index = 42; index <= 50; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 600000000000000000,
                currentTokenId: imageGallery[index - 1].currentTokenId + 3,
                lastTokenId: imageGallery[index - 1].lastTokenId + 3,
                mintingPayoutAddress: 0x17F6AD8Ef982297579C203069C1DbfFE4348c372,
                royaltyPayoutAddress: 0x17F6AD8Ef982297579C203069C1DbfFE4348c372
            });
        }
    }

    //* ----------------------- Minting Functions ------------------------- //

    /**
        This function will mint a token of the specified image passed to it. 
        It wll revert if the image number is out side of this collection, if 
        there are no tokens left for that image, or if the minter failed to 
        send enough ether to cover the price.

        Following the minting the royalty information is set via the 
        _setTokenRoyalty() function inherited from OpenZeppelin's ERC721Royalty 
        extension.

        Finally, The price of the image is then transferred to a MoneyPipe 
        contract which pays out 90% to the project and a 10% commision back to 
        the artist.

        Arguments:
            - _imageNumber - The number of the image the user wants to mint (1-50).
    */
    function mintImage(uint256 _imageNumber) public payable {
        require(
            _imageNumber > 0 && _imageNumber < 51,
            "The image you have selected does not exist in this collection."
        );
        uint64 _newTokenId = imageGallery[_imageNumber].currentTokenId;
        require(
            _newTokenId <= imageGallery[_imageNumber].lastTokenId,
            "No more editions of this image are available."
        );
        require(
            msg.value >= imageGallery[_imageNumber].price,
            "You didn't send enough Ether."
        );
        _safeMint(msg.sender, _newTokenId);
        _setTokenRoyalty(
            _newTokenId,
            imageGallery[_imageNumber].royaltyPayoutAddress,
            1000
        );
        payable(imageGallery[_imageNumber].mintingPayoutAddress).transfer(
            msg.value
        );
        imageGallery[_imageNumber].currentTokenId = _newTokenId + 1;
    }

    //* ------------------------ Assistant Functions -------------------------- //
    // Various functions used for testing. Likely to be removed later.

    function getImageInfo(uint256 _imageNumber)
        public
        view
        returns (
            uint64 imgNumber,
            uint64 price,
            uint64 currentTokenId,
            uint64 lastTokenId,
            address mintingPayoutAddress,
            address royaltyPayoutAddress
        )
    {
        return (
            imageGallery[_imageNumber].imgNumber,
            imageGallery[_imageNumber].price,
            imageGallery[_imageNumber].currentTokenId,
            imageGallery[_imageNumber].lastTokenId,
            imageGallery[_imageNumber].mintingPayoutAddress,
            imageGallery[_imageNumber].royaltyPayoutAddress
        );
    }

    function getContractStoredBalance()
        public
        view
        onlyOwner
        returns (uint256 ContractBalance)
    {
        return address(this).balance;
    }

    //* ----------------------- Royalty Functions ------------------------- //
    function _burn(uint256 tokenId)
        internal
        virtual
        override(ERC721, ERC721Royalty)
    {
        super._burn(tokenId);
        _resetTokenRoyalty(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    //* ----------------------- Metadata Functions ------------------------ //
    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"; // Old URI
    }

    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        string memory baseURI = _baseURI();
        return
            bytes(baseURI).length > 0
                ? string(
                    abi.encodePacked(
                        baseURI,
                        Strings.toString(tokenId),
                        ".json"
                    )
                )
                : "";
    }
}
