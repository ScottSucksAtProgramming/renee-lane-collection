# Renee Lane Collection User Documentation

    ___________________________________________________________________________
    ___________________▄▄Æ█▀▀▀███Æ▄▄,_______,▄▄Æ▀██▀▀▀██▄▄_____________________
    _______"▌^^^^^^▐█▀▀█^^█▀^^█▀^▀█▌╚▀▀▀""▀▀▀▀█▌^▀█^^^█^^█▀▀█▌^^^^^^^Γ_________
    ________ ┐____▄▀█__╟▌_█___█>^_.─^``,,,_`"¬- `~█__ █_▐▌_ █╙█____,`__________
    _________ \_ █▌_ █__█_╟▌,^ -`,⌐`__ ______ "-_*,`w]▌_█__█`_ █__/____________
    ___________▐█ ▀▄_╙█_╟▌▐▀_⌐ ⌐ _______________ "▄",└▌▐▌_▓▀_▄▀_█▌_____________
    ___________█▀█,_▀▄╙▌_█_┌_▄▄¬`___``¬,_,~^`____`¬▓_\_█_▐▌▄█ ,▄▀█_____________
    __________▐▌_ ╬▀▓▄██▄ ╒_╛╙╕_______,^__-_______ ╨╨_\_¥██▄█▀╟__╟▌____________
    __________█▀▀▀██▄▄▀█▌_─⌠_ _\___________ _____, ,_▐_b █▀▄▄▓▓▀▀╙█____________
    __________█▄▄▄▄▄█▄██⌐j_▌__'_"___ _╒███▌__┌__╒ ,____│_████▄▄▄▄▄█____________
    __________╟▌___,▄█▌_▌j_▌___ _ ç[__└███▀____Æ_'___ _╠_▌╠▀▄▄___]█____________
    __________ █▄█▀`__▄█▌_▌╘_____ `▌_________,▀ _____⌠_⌐]█▄__└▀█▄█⌐____________
    ___________╙▌__▄█▀`_╟▄└_%______└\_______,\______┌_Å_█_ ╙█▄__▐▌_____________
    ____________▀█▀ _,▄▀└╙▄ ┐'______┌^_____/_______ƒ_┘_╛└▀█▄_ ▀██______________
    _____________╙█▄▀╙__,▓▀█_²_'._____ ┐__∩_ ___,* / ▄▀█▄__└▀█▓▀_______________
    ______________ █▄_▄█╙_,▓█*_`≈,`≈.,_`¼╛__.-^ -^_/██,_╙▀▄_╓█_________________
    _▄█▀▀▀▀▄________╙█▄_▄█▀_▄█▌▐▌._`"~-----─¬` ,╤▌╙█▄_╙▀▄_╓█▀________▄█▀▀▀▓▄___
    ▓▌_____█⌐_________╙█▄,▓▀`▄██ __  `"¬¬¬"``___ ██▄ ▀█,▄█╙_________ █_____╙█__
    █_____╒█____________ ▀█▄▀╓█`½_______________╒ █▄▀██▀_____________╙⌐____ █__
    └█_____________________,██▄__\_____________/__▄██▄_____________________█▀__
    _ ▀▓,_______________,▄▀╙__ ╙▀█▓___________▓█▀╙___╙▀█▄_______________,▓▀____
    _____▀▀█▄▄▄▄▄▄▄▄Æ▀▀▀__________ ╙█████████▀__________ ╙▀▀█▄▄▄▄▄▄▄▄█▀▀`______
    ________________________________ ███████___________________________________
    __________________________________╙████____________________________________
    ___________________________________╙██_____________________________________
    ____________________________________ ______________________________________
    ___________________________________________________________________________
         Surrender   |   Submit  |   Sacrifice   |   Serve   |   Survive

The Renee Lane Collection is a 50-piece collection of artwork inspired by the
author Ms. Renee Lane. The artwork featured in this collection is being sold as
limited edition digital prints tracked on the blockchain. Proceeds from this
project are being split between the artists and the film-producer, Ms. Viola
Voltairine, who is bringing Ms. Renee Lane's book to life as an independent
film.

ReneeLaneCollection.sol is a bespoke ERC-721 smart contract written in Solidity
to manage the creation and tracking of Non-Fungible Tokens for the collection.

This documentation file will cover the basic features of the smart contract,
describe its intended use, and provide an overview of the philosophy behind its
creation. A key principle in the design of this contract (and its sister
contract ReneeCoins.sol) is transparency and trust: If you are interested in
understanding how this contract works with an in depth review of its source
code the final section of this document contains a line by line review of this
contract.

## ReneeLaneCollection.sol

Contract Name: The Renee Lane Collection

Author: Scott Kostolni

Version: 0.0.1 beta

This contract allows for the minting of a limited number of tokens for each
piece of artwork in The Renee Lane Collection. The artwork is tracked on the
blockchain using the ERC-721 standard. Royalties are paid to the artist for
each piece minted, as well as through secondary marketplace sales of the
artwork. Royalty information is baked into the tokens via the ERC-2981
standard. Metadata for these tokens are securely stored off-chain in IPFS and
cannot be altered later.

Investors who mint artwork from this collection are stored permanently in the
contract's storage so investors will always maintain their benefits even if
their artwork is sold or transferred.

OpenZeppelin's ERC7211, ERC721Royalties and Ownable contracts were used to
provide the standard NFT functionality using secure and tested libraries.

## Statistics

### Gas Usage

    Current Gas Usage for version 0.0.0 beta - Optimizer: 1,000 Runs
    ├─ deployment             -  avg: 5993711  low: 5993711  high: 5993711 USD: $113.82
    ├─ constructor            -  avg: 4882094  low: 4882094  high: 4882094 USD:  $92.71
    ├─ mintArtwork            -  avg:  139811  low:   22479  high:  211063 USD:   $4.01
    ├─ addToWhitelist         -  avg:   43341  low:   22728  high:   44439 USD:   $0.84
    ├─ withdrawPayout         -  avg:   26814  low:   21398  high:   48446 USD:   $0.92
    ├─ transferOwnership      -  avg:   26474  low:   22794  high:   30154 USD:   $0.57
    ├─ printInvestorList      -  avg:   24716  low:   23203  high:   26195 USD:   $0.50
    ├─ name                   -  avg:   24519  low:   24519  high:   24519 USD:   $0.47
    ├─ symbol                 -  avg:   24495  low:   24495  high:   24495 USD:   $0.47
    ├─ tokenURI               -  avg:   24221  low:   22548  high:   25609 USD:   $0.49
    ├─ artGallery             -  avg:   23456  low:   23456  high:   23456 USD:   $0.44
    ├─ artist                 -  avg:   23280  low:   23280  high:   23280 USD:   $0.45
    ├─ forcePayment           -  avg:   23139  low:   22752  high:   23656 USD:   $0.44
    ├─ royaltyInfo            -  avg:   23020  low:   23014  high:   23026 USD:   $0.43
    ├─ isInvestor             -  avg:   22751  low:   22751  high:   22763 USD:   $0.43
    ├─ isWhitelisted          -  avg:   22742  low:   22742  high:   22742 USD:   $0.43
    ├─ payoutsOwed            -  avg:   22741  low:   22741  high:   22741 USD:   $0.42
    ├─ ownerOf                -  avg:   22484  low:   22484  high:   22484 USD:   $0.42
    ├─ PROJECT_WALLET_ADDRESS -  avg:   22190  low:   22190  high:   22190 USD:   $0.42
    ├─ owner                  -  avg:   22140  low:   22140  high:   22140 USD:   $0.41
    ├─ supportsInterface      -  avg:   21903  low:   21795  high:   21958 USD:   $0.42
    ├─ getContractBalance     -  avg:   21358  low:   21358  high:   21358 USD:   $0.41
    ├─ removeFromWhitelist    -  avg:   20416  low:   14749  high:   23706 USD:   $0.45
    └─ renounceOwnership      -  avg:   18500  low:   14775  high:   22226 USD:   $0.42
    Note: USD Calculations based on Gas Price: 35 Wei and Ethereum price: $1208 from 6-26-2022.
    Formula: TransactionCost =  (Gas (High) * Gas Price * Ethereum USD Price) / 1,000,000,000
