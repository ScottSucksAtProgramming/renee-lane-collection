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
understanding how this contract works with an in depth review of it's source
code I invite you to view the [Renee Lane Collections Developer Documentation]

## Smart Contract Details

Contract Name: The Renee Lane Collection

Author: Scott Kostolni

Version: 0.0.1 beta

is a , a

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
