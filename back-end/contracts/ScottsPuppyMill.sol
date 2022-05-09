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
    // The Renee Lane Collection contains 50 pieces of artwork with varying
    // prices, and supply for minting. To save gas fees metadata will uploaded
    // to IPFS separately and organized by tokenId.
    //
    // Supply of 20
    // TokenId 01-20: Image 1       TokenId 21-40: Image 2
    // TokenId 41-60: Image 3       TokenId 61-80: Image 4
    // TokenId 81-100: Image 5      TokenId 101-120: Image 6
    // TokenId 121-140: Image 7     TokenId 141-160: Image 8
    // TokenId 161-180: Image 9     TokenId 181-200: Image 10
    // TokenId 201-220: Image 11    TokenId 221-240: Image 12
    // TokenId 241-260: Image 13    TokenId 261-280: Image 14
    // TokenId 281-300: Image 15    TokenId 301-320: Image 16
    // TokenId 321-340: Image 17    TokenId 341-360: Image 18
    // TokenId 361-380: Image 19    TokenId 381-400: Image 20

    // Supply of 10
    // TokenId 401-410: Image 21    TokenId 411-420: Image 22
    // TokenId 421-430: Image 23    TokenId 431-440: Image 24
    // TokenId 441-450: Image 25    TokenId 451-460: Image 26
    // TokenId 461-470: Image 27    TokenId 471-480: Image 28
    // TokenId 481-490: Image 29    TokenId 491-500: Image 30

    // Supply of 5
    // TokenId 501-505: Image 31    TokenId 506-510: Image 32
    // TokenId 511-515: Image 33    TokenId 516-520: Image 34
    // TokenId 521-525: Image 35    TokenId 526-530: Image 36
    // TokenId 531-535: Image 37    TokenId 536-540: Image 38
    // TokenId 541-545: Image 39    TokenId 546-550: Image 40

    // Supply of 3
    // TokenId 551-553: Image 41    TokenId 554-556: Image 42
    // TokenId 557-559: Image 43    TokenId 560-562: Image 44
    // TokenId 563-565: Image 45    TokenId 566-568: Image 46
    // TokenId 569-571: Image 47    TokenId 572-574: Image 48
    // TokenId 575-577: Image 49    TokenId 578-580: Image 45

    struct Image {
        uint64 id;
        uint64 price;
        uint64 supplyLimit;
        uint64 counter;
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
