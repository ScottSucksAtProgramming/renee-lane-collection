// SPDX-License-Identifier: MIT

//* ----------------------------- Documentation --------------------------- //
// Module:  ReneeLaneCollection.sol
// This is a smart contract which creates ERC-721 non-fungible tokens. It was
// originally written as a test contract used in the Scott's Puppy Mill
// project. It is being repurposed and expanded upon for use in the Renee Lane Collection.
//
// Current Statistics as of 0.1.0 alpha
// Deployment Cost  |   4,407,964 Gas
// 1st Minting Cost |     101,137 Gas
// Additional Mints |      84,037 Gas
//
//
// Modification History
// 04-28-2022 | SRK | Project Created.
// 04-30-2022 | SRK | Added counters to a struct to help save gas.
// 05-03-2022 | SRK | Code imported into Renee Lane Collection Project.
// 05-09-2022 | SRK | Minting Function Completed.
// 05-10-2022 | SRK | Contract Ownership Functionality Added.
// 05-15-2022 | SRK | Royalty Functionality Added.
// 05-15-2022 | SRK | Version 0.1.0 alpha created.
// 05-18-2022 | SRK | mintImage() gas optimization pass.

//* ------------------------------- Tasks --------------------------------- //
// Update minting functions and counters to model the collection. - Complete (05/09/2022)
// Add access control support. - Complete (05/10/2022)
// Add royalty support. - Complete (05/15/2022)
// Todo: Add Investor List functionality.
// Todo: Add Withdraw Payment functionality.
// Todo: Implement Minting Payment Splits
// Todo: Create MoneyPipe Contracts for each Artist with a 50/50 split between
// Todo: the Artist and Ms. Viola's Wallet.
// Todo: Implement Royalty Payment Splits
// Todo: Create/Add MoneyPipe Contract Address for Royalty Splits
// Todo: Update _baseURI to new IPFS metdata address.
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
    }

    //! This will be updated when we get actual moneypipe contracts set.
    address dummyMoneypipeAddress = 0x0A098Eda01Ce92ff4A4CCb7A4fFFb5A43EBC70DC;
    //* ---------------------------- Mappings ----------------------------- //
    // Stores Image objects for each image by imageNumber.
    mapping(uint256 => Image) imageGallery;

    //* ------------------------------ Events ----------------------------- //

    //* --------------------------- Contructor ---------------------------- //
    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        // Initializes Image Struct Objects. I couldn't come up with a
        // better way to do this math. This works.
        imageGallery[1] = Image(1, 12, 1, 20);
        for (uint64 index = 2; index <= 10; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 12,
                currentTokenId: imageGallery[index - 1].currentTokenId + 20,
                lastTokenId: imageGallery[index - 1].lastTokenId + 20
            });
        }
        for (uint64 index = 11; index <= 20; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 24,
                currentTokenId: imageGallery[index - 1].currentTokenId + 20,
                lastTokenId: imageGallery[index - 1].lastTokenId + 20
            });
        }
        imageGallery[21] = Image(21, 36, 401, 410);
        for (uint64 index = 22; index <= 30; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 36,
                currentTokenId: imageGallery[index - 1].currentTokenId + 10,
                lastTokenId: imageGallery[index - 1].lastTokenId + 10
            });
        }
        imageGallery[31] = Image(31, 48, 501, 505);
        for (uint64 index = 32; index <= 40; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 48,
                currentTokenId: imageGallery[index - 1].currentTokenId + 5,
                lastTokenId: imageGallery[index - 1].lastTokenId + 5
            });
        }
        imageGallery[41] = Image(41, 60, 551, 553);
        for (uint64 index = 42; index <= 50; index++) {
            imageGallery[index] = Image({
                imgNumber: index,
                price: 60,
                currentTokenId: imageGallery[index - 1].currentTokenId + 3,
                lastTokenId: imageGallery[index - 1].lastTokenId + 3
            });
        }
    }

    //* ----------------------- Minting Functions ------------------------- //

    /**
        This function will mint a token of the specified image passed to it. 
        Will revert if there are no tokens left for that image.

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
        _safeMint(msg.sender, _newTokenId);
        _setTokenRoyalty(_newTokenId, dummyMoneypipeAddress, 1000);
        imageGallery[_imageNumber].currentTokenId = _newTokenId + 1;
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
