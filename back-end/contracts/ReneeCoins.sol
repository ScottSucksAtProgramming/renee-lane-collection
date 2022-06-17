/// SPDX-License-Identifier: MIT
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

//* ----------------------------- Documentation --------------------------- //
/**
 * @title Renee Coins
 * @author Scott Kostolni
 *
 * @notice Version 0.1.0 Alpha.
 *
 * @notice This is a bespoke ERC-20 Contract that provides the social
 * currency, Renee Coins, which grants benefits to investors and artists of
 * The Renee Lane Collection.
 *
 * @notice This contract acts as the ledger for the Renee Coins and allows
 * for Renee Coins to be created, tracked, and transferred or traded between
 * wallets. It uses the OpenZeppelin contracts as a back bone with extension
 * allowing a maximum cap to be specified, and for the owner to destroy or
 * burn their tokens. The OpenZepplin Ownable extension is used to set an
 * Owner for the contract and ensure certain functions are ONLY callable by
 * the Owner.
 */

//* ------------------------- Modification History ------------------------ //
/**
 * 06-10-2022 | SRK | Contract Created
 * 06-10-2022 | SRK | Ownership functionality added.
 * 06-10-2022 | SRK | Minting functionality added.
 * 06-10-2022 | SRK | Token Cap functionality added.
 * 06-10-2022 | SRK | Token burn functionality added.
 * 06-10-2022 | SRK | airdropReneeCoins() function created.
 */

//* ------------------------------ Statistics ----------------------------- //
/**
 * Current Statistics as of 0.1.0 Alpha - Optmizer: 10,000 Runs
 * Deployment Cost                             |   1,345,119 Gas   |   Approx:     $80.71
 * createCoins(From 0)                         |      81,017 Gas   |   Approx:      $4.86
 * createCoins(From Non-Zero)                  |      41,701 Gas   |   Approx:      $2.50
 * burn (Non-Zero to Non-Zero)                 |      38,762 Gas   |   Approx:      $2.33
 * burn (Non-Zero to Zero)                     |      42,072 Gas   |   Approx:      $2.52
 * transfer (Non-Zero => Zero Balance)         |      59,127 Gas   |   Approx:      $3.55
 * transfer (Non-Zero => Non-Zero Balance)     |      39,462 Gas   |   Approx:      $2.38
 * transfer (Zero => Zero Balance)             |      59,127 Gas   |   Approx:      $3.55
 * transfer (Zero => Non-Zero Balance)         |      39,462 Gas   |   Approx:      $2.38
 * Cost to Mint and Then Transfer 10 Tokens (AirDrop) = 41,674 + 59,127 = 100,801 Gas = $6.05
 * Cost of airdropReneeCoins() 10 Tokens = 61,907 Gas = $3.71
 * Cost of airdropReneeCoins() from 0 Balance 10 Tokens = 42,228 Gas = $2.53
 */

//* ------------------------------- Tasks --------------------------------- //
/**
 * Build Basic Contract - Complete (6/10/22)
 * Build Minting function that allows owner to specify number of tokens to
 * mint. - Complete (6/10/22)
 * Set cap to 2,000,000 Tokens - ERC-20Capped OpenZeppelin - Complete
 * (6/10/22)
 * Add Owner Functionality - Ownable Extension OpenZeppelin - Complete
 * (6/10/22)
 * Add burn functionality - Complete (6/10/22)
 * Test build and AirDrop Function. - Complete (6/10/22)
 */

//* ----------------------------- Resources ------------------------------- //

pragma solidity 0.8.15;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

//* ----------------------------- Contract -------------------------------- //

contract ReneeCoins is ERC20, ERC20Burnable, ERC20Capped, Ownable {
    //* --------------------------- Constructor --------------------------- //
    /**
     * @notice In the constructor the total number of Renee Coins which can
     * be in circulation at any given time is capped at 2,000,000. This cap
     * is only set during the deployment of this contract and cannot be
     * changed later.
     */
    constructor() ERC20("Renee Coins", "RC") ERC20Capped(2000000) {}

    //* ----------------------- Minting Function -------------------------- //
    /**
     * @notice The createCoins() function serves as the minting function for
     * this contract. It can be called only by the owner and allows them to
     * mint as many Renee Coins as they like, up to the cap. These function
     * will ONLY create coins in the Owner's wallet. The airdropCoins can be
     * used to send coins to another wallet address.
     *
     * @param amount The number of coins that are to be created.
     */
    function createCoins(uint256 amount) public onlyOwner {
        _mint(msg.sender, amount);
    }

    //* -------------------- Administrative Functions --------------------- //
    /**
     * @notice The airdropCoins() function allows the Owner to create new
     * coins and immediately send them to a specified wallet address. This
     * is significantly cheaper than minting and transferring the coins
     * separately. This function can ONLY be called by the Owner.
     *
     * @param recepient The wallet address of the recipeint of the airdrop.
     *
     * @param amount The number of coins that are to be created.
     */
    function airdropCoins(address recepient, uint256 amount) public onlyOwner {
        _mint(recepient, amount);
    }

    //* ----------------------- Override Functions ------------------------ //
    /**
     * @notice The decimals() function replaces the inherited functions from
     * the ERC20 and ERC20Capped OpenZeppelin Contracts. For Renee Coins
     * there are 0 decimal places, these tokens cannot be broken down in
     * smaller increments. This function is required by the ERC-20 standard.
     *
     * @return decimalPlaces The amount of decimal places that are supported
     * by these tokens.
     */
    function decimals()
        public
        view
        virtual
        override
        returns (uint8 decimalPlaces)
    {
        return 0;
    }

    /**
     * @notice The _mint() function replaces the inherided functions from
     * the ERC20 and ERC20Capped Openzepplin Contracts. This is an internal
     * function which can only be called by the contract itself and is used
     * inside other functions such as createCoins() and airdropCoins().
     *
     * @param account The wallet address to which coins will be minted.
     *
     * @param amount The number of coins that are to be created.
     */
    function _mint(address account, uint256 amount)
        internal
        virtual
        override(ERC20, ERC20Capped)
    {
        require(
            ERC20.totalSupply() + amount <= cap(),
            "ERC20Capped: cap exceeded"
        );
        super._mint(account, amount);
    }
}
