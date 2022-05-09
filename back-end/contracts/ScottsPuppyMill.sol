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

//* ------------------------------- Tasks --------------------------------- //
// Todo: Update minting functions and counters to model the collection. - In Progress (05/05/2022)
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
    // We will be creating NFTs for 3 breeds of puppies, St. Bernards,
    //Shiba Inus, and Pugs. These Counter variables will be used to create
    //the unique tokenId for each minted puppy.
    //St. Bernard Token IDs: 1-100;
    //Shiba Inu Token IDs: 101-200;
    //Pug Token IDs: 201-300;
    //Using unique TokenIds like this will allow metadata to be pre-uploaded to IPFS.

    struct Image {
        uint64 id;
        uint64 price;
        uint64 supplyLimit;
        uint64 padding;
    }

    mapping(uint256 => Image) images;

    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        for (uint256 index = 1; index <= 10; index++) {
            images[index] = Image(index, 12, 20);
        }
        for (uint256 index = 11; index <= 20; index++) {
            images[index] = Image(index, 24, 20);
        }
        for (uint256 index = 21; index <= 30; index++) {
            images[index] = Image(index, 36, 10);
        }
        for (uint256 index = 31; index <= 40; index++) {
            images[index] = Image(index, 48, 5);
        }
        for (uint256 index = 41; index <= 50; index++) {
            images[index] = Image(index, 60, 3);
        }
    }

    //* ----------------------- Minting Functions ------------------------- //

    function mintImage(uint256 _imgId) public returns (uint256) {
        require(
            counter.imageOne <= 100,
            "No more editions of this image are available."
        );
        uint256 newTokenId = counter.imageOne;
        _safeMint(msg.sender, newTokenId);
        counter.imageOne = counter.imageOne + 1;
        return newTokenId;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/";
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
