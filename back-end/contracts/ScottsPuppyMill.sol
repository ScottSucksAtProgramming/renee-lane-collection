// SPDX-License-Identifier: MIT

//* ----------------------------- Documentation --------------------------- //
// Module:  ScottsPuppyMill.sol
// This is a smart contract which creates ERC-721 non-fungible tokens. It was
// originally written as a test contract used in the Scott's Puppy Mill
// project. It is being repurposed and expanded upon for use in the Renee Lane Collection.
//
//
//
//
// Modification History
// 04-28-2022 | SRK | Project Created.
// 04-30-2022 | SRK | Added counters to a struct to help save gas.
// 05-03-2022 | SRK | Code imported into Renee Lane Collection Project.
// 05-09-2022 | SRK | Minting Function

//* ------------------------------- Tasks --------------------------------- //
// Update minting functions and counters to model the collection. - Complete (05/09/2022)
// Todo: Add royalty support.
// Todo: Add access control support.
// Todo: Add functionality for the investor list.
// Todo: Add functionality to accept and withdraw payments.
// Todo: Implement Minting Payment Splits
// Todo: Implement Royalty Payment Splits
// Todo: Update _baseURI to new IPFS metdata address.
// Todo: Gas Optimization.
// Todo: Ensure code is written for self-documentation. Comments are
// Todo: adjusted to provide additional information. Context available in
// Todo: design document.

//* ----------------------------- Resources ------------------------------- //
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

//* ----------------------------- Contract -------------------------------- //
contract ReneeLaneCollection is ERC721 {
    // Image information stored here. Packages into single 256byte container
    // when compiled.
    struct Image {
        uint64 imgNumber;
        uint64 price;
        uint64 currentTokenId;
        uint64 lastTokenId;
    }
    // Stores Image objects for each image by imageNumber.
    mapping(uint256 => Image) imageGallery;

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

        Returns:
            - newTokenId - The tokenId of the token which was last created.
    */
    function mintImage(uint256 _imageNumber) public returns (uint256) {
        require(
            imageGallery[_imageNumber].currentTokenId <=
                imageGallery[_imageNumber].lastTokenId,
            "No more editions of this image are available."
        );
        uint256 newTokenId = imageGallery[_imageNumber].currentTokenId;
        _safeMint(msg.sender, newTokenId);
        imageGallery[_imageNumber].currentTokenId =
            imageGallery[_imageNumber].currentTokenId +
            1;
        return newTokenId;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"; // Old URI
    }

    //* ----------------------- Other Functions ------------------------- //
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
