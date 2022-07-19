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
 * @dev Version 0.0.1 beta
 *
 * @dev This is a bespoke ERC-721 smart contract written to manage creation
 * and tracking of Non-Fungible Tokens for the Renee Lane Collection. For more
 * information, see the README.md file located at: https://bit.ly/rl_readme,
 * as well as additional documentation located at: https://bit.ly/rl_docs.
 */

//* ------------------------------- Tasks --------------------------------- //
/**
 * ✓ Release version 0.0.0 beta - Complete (7/3/2022)
 * ✓ Deploy Renee Lane Collection contract for Beta testing. - Complete (7/3/2022)
 * Todo: Build Python Scripts for managaging the contract.
 * Todo: Get feedback from beta testers.
 * Todo: Complete Integration Testing.
 * Todo: Resolve any issues with the contract.
 * Todo: Update code for production release.
 * Todo: Release version 1.0.0
 * Todo: Celebrate?!
 */

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
    mapping(uint256 => Artist) public artist;
    mapping(address => bool) public isInvestor;
    mapping(address => bool) public isWhitelisted;
    mapping(address => uint256) public payoutsOwed;

    address public PROJECT_WALLET_ADDRESS = (
        0xbbd68C8318087E5641b28698C69c779F23E50FFB
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

    event PayoutSent(
        address indexed caller,
        address indexed recipientAddress,
        uint256 indexed amount
    );

    constructor() ERC721("The Renee Lane Collection", "TRLC") {
        artist[1] = Artist({
            directAddress: 0x110969C24Da5268842Fd3756F499299056EB4DBf,
            royaltyAddress: 0xE709Ebdb07B30052D241024b6f9a3cd9482a30Df
        });
        artist[2] = Artist({
            directAddress: 0x3CC74a8eAd939BfC631bad2e010cdE26D6d9f057,
            royaltyAddress: 0x3dC3c88E15e77F6d79A08b94cac30a59d04D1Ec0
        });
        artist[3] = Artist({
            directAddress: 0x58C6558fB57114444f23b77a42b475bBE9146107,
            royaltyAddress: 0xd39e01d5931A81a6ed2C8B77A2c6366b92378686
        });
        artist[4] = Artist({
            directAddress: 0x4cf55451AB4274b043D5d17dd8112ed825E565c9,
            royaltyAddress: 0x47eD0FF0A62383465199428290CFCAc406cCE64E
        });
        artist[5] = Artist({
            directAddress: 0x10B7D462EDe680429344B20f16e3245E01F22FA4,
            royaltyAddress: 0x68a53E615Ea6B30cd27Ae15c6A8D972eE1ff7867
        });

        unchecked {
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
    }

    function purchaseArtwork(uint256 _imageNumber) external payable {
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
        unchecked {
            artGallery[_imageNumber].currentTokenID++;
        }
    }

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

    //! @dev Note: If the owner adds the Zero Address to the whitelist the
    //! purchaseArtwork() function will allow ALL addresses to mint artwork.
    function addToWhitelist(address _address) external onlyOwner {
        require(
            !isWhitelisted[_address],
            "Address is already on the whitelist."
        );
        isWhitelisted[_address] = true;
    }

    function removeFromWhitelist(address _address) external onlyOwner {
        require(isWhitelisted[_address], "Address is not on the whitelist.");
        isWhitelisted[_address] = false;
    }

    //! @dev This function is less secure than withdrawPayout() and should
    //! only be used when absolutely necessary. It does not follow the
    //! recommended pull design pattern.
    function forcePayment(address _addressToBePayed) external onlyOwner {
        uint256 _amountOwed = payoutsOwed[_addressToBePayed];
        require(_amountOwed > 0, "No money owed to this address.");
        payable(_addressToBePayed).transfer(_amountOwed);
        emit PayoutSent(msg.sender, _addressToBePayed, _amountOwed);
        payoutsOwed[_addressToBePayed] = 0;
    }

    function getContractBalance()
        public
        view
        returns (uint256 contractBalance)
    {
        return address(this).balance;
    }

    function printInvestorList()
        public
        view
        returns (address[] memory allInvestors)
    {
        return investorList;
    }

    function supportsInterface(bytes4 interfaceID)
        public
        view
        override(ERC721, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceID);
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

    function addNewInvestor(address _minterAddress, uint64 _tokenID) internal {
        isInvestor[_minterAddress] = true;
        investorList.push(_minterAddress);
        emit NewInvestorAdded(_minterAddress, _tokenID);
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return
            "https://ipfs.io/ipfs/QmNvnTpZVSW9ej8PdS4xzuKDFqCwhFLkhVfTA1JiLBS8EN/"; // Old URI
    }

    //! @dev Burning a token is irreversible. If you burn your token it can
    //! NEVER be recovered.
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
        unchecked {
            payoutsOwed[_artistDirectAddress] += uint256(_artistCut);
            payoutsOwed[PROJECT_WALLET_ADDRESS] += uint256(_projectCut);
        }
        emit PaymentSplit(
            valueSent,
            _artistDirectAddress,
            _artistCut,
            _projectCut
        );
    }
}
