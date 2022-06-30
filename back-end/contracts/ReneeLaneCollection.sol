// SPDX-License-Identifier: MIT
pragma solidity 0.8.15;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReneeLaneCollection is ERC721, ERC721Royalty, Ownable {
    struct Artwork {
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

    address[] public investorList;

    mapping(uint256 => Artwork) public artGallery;

    mapping(address => bool) public isInvestor;

    mapping(uint256 => Artist) public artist;

    mapping(address => uint256) public payoutsOwed;

    address public PROJECT_WALLET_ADDRESS = (
        0xdD870fA1b7C4700F2BD7f44238821C26f7392148
    );

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

    function mintArtwork(uint256 _imageNumber) public payable {
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

    function printInvestorList()
        public
        view
        returns (address[] memory allInvestors)
    {
        return investorList;
    }

    function withdrawPayout() public {
        require(address(this).balance > 0, "No money in contract.");
        require(payoutsOwed[msg.sender] > 0, "No funds owed to this wallet.");
        payable(msg.sender).transfer(payoutsOwed[msg.sender]);
        payoutsOwed[msg.sender] = 0;
    }

    function forcePayment(address _address) public onlyOwner {
        require(payoutsOwed[_address] > 0, "No money owed to this address.");
        payable(_address).transfer(uint256(payoutsOwed[_address]));
        payoutsOwed[_address] = 0;
    }

    function getContractBalance()
        public
        view
        returns (uint256 contractBalance)
    {
        return address(this).balance;
    }

    function supportsInterface(bytes4 interfaceID)
        public
        view
        override(ERC721, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceID);
    }

    //* --------------------- Internal Functions -------------------------- //

    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/bafybeiff5pj3vrijyvbbizpdekt467lexwexa5s4old5rantfvbpk5eb3e/"; // Old URI
    }

    function _burn(uint256 tokenID)
        internal
        virtual
        override(ERC721, ERC721Royalty)
    {
        super._burn(tokenID);
        _resetTokenRoyalty(tokenID);
    }

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

    function addNewInvestor(address _minterAddress, uint64 _tokenID) internal {
        isInvestor[_minterAddress] = true;
        investorList.push(_minterAddress);
        emit NewInvestorAdded(_minterAddress, _tokenID);
    }
}
