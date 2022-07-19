// SPDX-License-Identifier: MIT
/**
 *  ___________________________________________________________________________
 *  ___________________▄▄Æ█▀▀▀███Æ▄▄,_______,▄▄Æ▀██▀▀▀██▄▄_____________________
 *  _______"▌^^^^^^▐█▀▀█^^█▀^^█▀^▀█▌╚▀▀▀""▀▀▀▀█▌^▀█^^^█^^█▀▀█▌^^^^^^^Γ_________
 *  ________ ┐____▄▀█__╟▌_█___█>^_.─^``,,,_`"¬- `~█__ █_▐▌_ █╙█____,`__________
 *  _________ \_ █▌_ █__█_╟▌,^ -`,⌐`__ ______ "-_*,`w]▌_█__█`_ █__/____________
 *  ___________▐█ ▀▄_╙█_╟▌▐▀_⌐ ⌐ _______________ "▄",└▌▐▌_▓▀_▄▀_█▌_____________
 *  ___________█▀█,_▀▄╙▌_█_┌_▄▄¬`___``¬,_,~^`____`¬▓_\_█_▐▌▄█ ,▄▀█_____________
 *  __________▐▌_ ╬▀▓▄██▄ ╒_╛╙╕_______,^__-_______ ╨╨_\_¥██▄█▀╟__╟▌____________
 *  __________█▀▀▀██▄▄▀█▌_─⌠_ _\___________ _____, ,_▐_b █▀▄▄▓▓▀▀╙█____________
 *  __________█▄▄▄▄▄█▄██⌐j_▌__'_"___ _╒███▌__┌__╒ ,____│_████▄▄▄▄▄█____________
 *  __________╟▌___,▄█▌_▌j_▌___ _ ç[__└███▀____Æ_'___ _╠_▌╠▀▄▄___]█____________
 *  __________ █▄█▀`__▄█▌_▌╘_____ `▌_________,▀ _____⌠_⌐]█▄__└▀█▄█⌐____________
 *  ___________╙▌__▄█▀`_╟▄└_%______└\_______,\______┌_Å_█_ ╙█▄__▐▌_____________
 *  ____________▀█▀ _,▄▀└╙▄ ┐'______┌^_____/_______ƒ_┘_╛└▀█▄_ ▀██______________
 *  _____________╙█▄▀╙__,▓▀█_²_'._____ ┐__∩_ ___,* / ▄▀█▄__└▀█▓▀_______________
 *  ______________ █▄_▄█╙_,▓█*_`≈,`≈.,_`¼╛__.-^ -^_/██,_╙▀▄_╓█_________________
 *  _▄█▀▀▀▀▄________╙█▄_▄█▀_▄█▌▐▌._`"~-----─¬` ,╤▌╙█▄_╙▀▄_╓█▀________▄█▀▀▀▓▄___
 *  ▓▌_____█⌐_________╙█▄,▓▀`▄██ __  `"¬¬¬"``___ ██▄ ▀█,▄█╙_________ █_____╙█__
 *  █_____╒█____________ ▀█▄▀╓█`½_______________╒ █▄▀██▀_____________╙⌐____ █__
 *  └█_____________________,██▄__\_____________/__▄██▄_____________________█▀__
 *  _ ▀▓,_______________,▄▀╙__ ╙▀█▓___________▓█▀╙___╙▀█▄_______________,▓▀____
 *  _____▀▀█▄▄▄▄▄▄▄▄Æ▀▀▀__________ ╙█████████▀__________ ╙▀▀█▄▄▄▄▄▄▄▄█▀▀`______
 *  ________________________________ ███████___________________________________
 *  __________________________________╙████____________________________________
 *  ___________________________________╙██_____________________________________
 *  ____________________________________ ______________________________________
 *  ___________________________________________________________________________
 *       Surrender   |   Submit  |   Sacrifice   |   Serve   |   Survive
 */

//* ----------------------------- Documentation --------------------------- //
/**
 * @title Renee Coins
 * @author Scott Kostolni
 *
 * @dev Version 0.0.0 beta
 *
 * @dev This is a bespoke ERC-20 Contract that provides the social currency, 
 * Renee Coins, which grants benefits to investors and artists of The Renee 
 * Lane NFT Collection. For more information, see the README.md file located 
 * at: https://bit.ly/rl_readme, as well as additional documentation located 
 * at: https://bit.ly/rl_docs.

//* ------------------------------- Tasks --------------------------------- //
/**
 * ✓ Deploy Renee Coin Contract for User Beta Testing. - Complete (6/26/2022)
 * ✓ Complete final unit testing.
 * Todo: Build Python Scripts for managing the contract.
 * Todo: Get feedback from beta testers.
 * Todo: Complete integration testing.
 * Todo: Resolve any issues with the contract.
 * Todo: Update code for production release.
 * Todo: Release version 1.0.0
 * Todo: Celebrate?!
 */

pragma solidity 0.8.15;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReneeCoins is ERC20, ERC20Burnable, ERC20Capped, Ownable {
    constructor() ERC20("Renee Coins", "RC") ERC20Capped(2000000) {}

    function createCoins(uint256 amountOfCoinsToCreate) external onlyOwner {
        _mint(msg.sender, amountOfCoinsToCreate);
    }

    function airdropCoins(
        address recipientAddress,
        uint256 amountOfCoinsToAirdrop
    ) external onlyOwner {
        _mint(recipientAddress, amountOfCoinsToAirdrop);
    }

    function decimals()
        public
        view
        virtual
        override
        returns (uint8 decimalPlaces)
    {
        return 0;
    }

    function _mint(address recipientAddress, uint256 amountOfCoinsToCreate)
        internal
        virtual
        override(ERC20, ERC20Capped)
    {
        require(
            ERC20.totalSupply() + amountOfCoinsToCreate <= cap(),
            "ERC20Capped: cap exceeded"
        );
        super._mint(recipientAddress, amountOfCoinsToCreate);
    }
}
