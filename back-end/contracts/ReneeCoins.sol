/// SPDX-License-Identifier: MIT
/*
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
 */

//* ----------------------------- Documentation --------------------------- //
/**
 * @title Renee Coins
 * @author Scott Kostolni
 *
 * @notice Version 1.0.0 Beta.
 *
 * @notice This is a bespoke ERC-20 Contract that provides the social
 * currency, Renee Coins, which grants benefits to investors and artists of
 * The Renee Lane NFT Collection.
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
/*
  06-10-2022 | SRK | Contract Created
  06-10-2022 | SRK | Ownership functionality added.
  06-10-2022 | SRK | Minting functionality added.
  06-10-2022 | SRK | Token Cap functionality added.
  06-10-2022 | SRK | Token burn functionality added.
  06-10-2022 | SRK | airdropReneeCoins() function created.
  06-21-2022 | SRK | Unit Testing of Contract In Progress.
  06-21-2022 | SRK | Contract Ready for Beta Tasting.
 */

//* ------------------------------ Statistics ----------------------------- //
/**
 * @notice Current Gas Useage as of 1.0.0 Beta - Optmizer: 10,000 Runs
 * ReneeCoins <Contract>
 *   ├─ deployment   -  avg: 1347574  avg (confirmed): 1347574  low: 1347574  high: 1347574  USD cost: $29.70
 *   ├─ constructor  -  avg: 1063254  avg (confirmed): 1063254  low: 1063254  high: 1063254  USD cost: $23.43
 *   ├─ airdropCoins -  avg:   53304  avg (confirmed):   68496  low:   22923  high:   68502  USD cost:  $1.51
 *   ├─ createCoins  -  avg:   49957  avg (confirmed):   68005  low:   22422  high:   68009  USD cost:  $1.50
 *   ├─ symbol       -  avg:   24452  avg (confirmed):   24452  low:   24452  high:   24452  USD cost:  $0.54
 *   ├─ balanceOf    -  avg:   22718  avg (confirmed):   22718  low:   22718  high:   22718  USD cost:  $0.50
 *   ├─ owner        -  avg:   22132  avg (confirmed):   22132  low:   22132  high:   22132  USD cost:  $0.49
 *   ├─ totalSupply  -  avg:   22113  avg (confirmed):   22113  low:   22113  high:   22113  USD cost:  $0.49
 *   └─ decimals     -  avg:   21309  avg (confirmed):   21309  low:   21309  high:   21309  USD cost:  $0.47
 * Note: USD Calculations based on Gas Price: 20 Wei and Ethereum price: $1102 from 6-21-2022.
 * Formula: TransactionCost =  (Gas (High) * Gas Price * Etherum USD Price) / 1,000,000,000
 */

//* ------------------------------- Tasks --------------------------------- //
/*
  Todo: Deploy Renee Coin Contract for User Beta Testing.
  Todo: Complete final unit testing.
  Todo: Complete integration testing.
  Todo: Identify and resolve any issues found during testing.
  Todo: Obtain final approval of code.
  Todo: Deploy finalized contract to MainNet for launch.
 */

//* ----------------------------- Resources ------------------------------- //
// Defines the version of solidity this contract was developed for.
pragma solidity 0.8.15;

// Imports code from OpenZeppelin to be used for this contract.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

//* ----------------------------- Contract -------------------------------- //

/**
 * @notice The ReneeCoin Contract inherits OpenZeppelin's ERC20, ERC20Burnable,
 * ERC20Capped and Ownable extenions to ensure compliance to the current
 * standards and provide a strong security basis with code that has been
 * vetted elsewhere.
 */
contract ReneeCoins is ERC20, ERC20Burnable, ERC20Capped, Ownable {
    //* --------------------------- Constructor --------------------------- //
    /**
     * @notice The constructor helps set up the initial state of the smart
     * contract. In the constructor the total number of Renee Coins which
     * can be in circulation at any given time is capped at 2,000,000. This
     * cap is only set during the deployment of this contract and cannot be
     * changed later.
     *
     * @notice The name of the ERC-20 Token and Symbol are also permanently
     * set in the constructor.
     */
    constructor() ERC20("Renee Coins", "RC") ERC20Capped(2000000) {}

    //* ----------------------- Minting Function -------------------------- //
    /**
     * @notice When this contract is initially deployed, there are 0 Renee
     * Coins in existence. New Renee Coins must be 'minted' in order to
     * create them. createCoins() serves as the mintingfunction for this
     * contract. It can be called only by the owner and allows them to mint
     * as many Renee Coins as they like, up to the cap.
     *
     * This function will ONLY create coins in the Owner's wallet. The
     * airdropCoins() function can be used to mint coins directly to someone
     * else's wallet.
     *
     * @param amount The number of coins that are to be minted.
     */
    function createCoins(uint256 amount) public onlyOwner {
        _mint(msg.sender, amount);
    }

    //* -------------------- Administrative Functions --------------------- //
    /**
     * @notice The airdropCoins() function allows the Owner to mint new Renee
     * Coins directly into a specified wallet address. This is significantly
     * cheaper than minting and transferring the coins separately.
     *
     * This function can ONLY be called by the Owner.
     *
     * @param recipient The wallet address of the recipient of the airdrop.
     *
     * @param amount The number of coins that are to be created.
     */
    function airdropCoins(address recipient, uint256 amount) public onlyOwner {
        _mint(recipient, amount);
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
