// SPDX-License-Identifier: MIT
// ------------------------------ Documentation --------------------------- //
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

// -------------------------------- Tasks --------------------------------- //
// Todo: Update minting functions and counters to model the collection.
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
// ------------------------------ Resources ------------------------------- //
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

struct Kennel {
    uint64 stBernard;
    uint64 shibaInu;
    uint64 pug;
    uint64 padding;
}

// ------------------------------ Contract -------------------------------- //
contract ScottsPuppyMill is ERC721 {
    // We will be creating NFTs for 3 breeds of puppies, St. Bernards,
    //Shiba Inus, and Pugs. These Kennel variables will be used to create
    //the unique tokenId for each minted puppy.
    //St. Bernard Token IDs: 1-100;
    //Shiba Inu Token IDs: 101-200;
    //Pug Token IDs: 201-300;
    //Using unique TokenIds like this will allow metadata to be pre-uploaded to IPFS.

    Kennel public kennel;

    constructor() ERC721("Scott Dogs", "SDOG") {
        //Initalize the breed Kennels.
        kennel.stBernard = 1;
        kennel.shibaInu = 1;
        kennel.pug = 1;
    }

    // ------------------------------ Functions ------------------------------ //
    /** 
    This function will mint a new St. Bernard Puppy NFT. The transaction will 
    revert if there are already 100 St. Bernards. The tokenURI will be 
    generated using the newTokenId and the ipfs address.
    */
    function createStBernard() public returns (uint256) {
        require(
            kennel.stBernard <= 100,
            "No more St. Bernard Puppies Available!"
        );
        uint256 newTokenId = kennel.stBernard;
        _safeMint(msg.sender, newTokenId);
        kennel.stBernard = kennel.stBernard + 1;
        return newTokenId;
    }

    /** 
    This function will mint a new Shiba Inu Puppy NFT. The transaction will 
    revert if there are already 100 St. Bernards. The tokenURI will be 
    generated using the newTokenId and the ipfs address.
    */
    function createShibaInu() public returns (uint256) {
        require(kennel.shibaInu <= 100, "No more Shiba Inu Puppies Available!");
        uint256 newTokenId = kennel.shibaInu + 100;
        _safeMint(msg.sender, newTokenId);
        kennel.shibaInu = kennel.shibaInu + 1;
        return newTokenId;
    }

    /** 
    This function will mint a new Shiba Inu Puppy NFT. The transaction will 
    revert if there are already 100 St. Bernards. The tokenURI will be 
    generated using the newTokenId and the ipfs address.
    */
    function createPug() public returns (uint256) {
        require(kennel.pug <= 100, "No more Pug Puppies Available!");
        uint256 newTokenId = kennel.pug + 200;
        _safeMint(msg.sender, newTokenId);
        kennel.pug = kennel.pug + 1;
        return newTokenId;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/";
    }

    // ? Why is this function here? - I feel like there was an error that
    // ? required me to put it in but it serves no actual purpose as far as
    // ? minting ERC-721s go in this contract. Metadata is being hosted
    // ? off-chain through IPFS.
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
