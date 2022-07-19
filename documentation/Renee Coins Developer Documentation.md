## Statistics

### Gas Usage

    @notice Current Gas Usage as of 0.0.0 Beta - Optimizer: 1,000 Runs
    ReneeCoins <Contract>
    ├─ deployment             -  avg: 1347574  avg (confirmed): 1347574  low: 1347574  high: 1347574  USD: $18.52
    ├─ constructor            -  avg: 1063242  avg (confirmed): 1063242  low: 1063242  high: 1063242  USD: $14.61
    ├─ createCoins            -  avg:   65546  avg (confirmed):   67987  low:   22422  high:   68009  USD:  $0.93
    ├─ airdropCoins           -  avg:   45935  avg (confirmed):   68490  low:   22923  high:   68490  USD:  $0.94
    ├─ approve                -  avg:   42875  avg (confirmed):   44108  low:   21925  high:   44120  USD:  $0.61
    ├─ transfer               -  avg:   41514  avg (confirmed):   51009  low:   21946  high:   51009  USD:  $0.70
    ├─ transferFrom           -  avg:   39996  avg (confirmed):   45152  low:   23621  high:   59675  USD:  $0.82
    ├─ burn                   -  avg:   32805  avg (confirmed):   35354  low:   22613  high:   35354  USD:  $0.49
    ├─ increaseAllowance      -  avg:   30173  avg (confirmed):   30173  low:   30173  high:   30173  USD:  $0.41
    ├─ decreaseAllowance      -  avg:   30106  avg (confirmed):   30106  low:   30106  high:   30106  USD:  $0.41
    ├─ burnFrom               -  avg:   27770  avg (confirmed):   28942  low:   23089  high:   28942  USD:  $0.40
    ├─ transferOwnership      -  avg:   26444  avg (confirmed):   30117  low:   22772  high:   30117  USD:  $0.41
    ├─ symbol                 -  avg:   24452  avg (confirmed):   24452  low:   24452  high:   24452  USD:  $0.34
    ├─ name                   -  avg:   24387  avg (confirmed):   24387  low:   24387  high:   24387  USD:  $0.32
    ├─ allowance              -  avg:   23258  avg (confirmed):   23258  low:   23258  high:   23258  USD:  $0.31
    ├─ balanceOf              -  avg:   22715  avg (confirmed):   22715  low:   22706  high:   22718  USD:  $0.30
    ├─ owner                  -  avg:   22132  avg (confirmed):   22132  low:   22132  high:   22132  USD:  $0.30
    ├─ totalSupply            -  avg:   22113  avg (confirmed):   22113  low:   22113  high:   22113  USD:  $0.29
    ├─ decimals               -  avg:   21309  avg (confirmed):   21309  low:   21309  high:   21309  USD:  $0.29
    ├─ cap                    -  avg:   21301  avg (confirmed):   21301  low:   21301  high:   21301  USD:  $0.29
    └─ renounceOwnership      -  avg:   18496  avg (confirmed):   14767  low:   14767  high:   22226  USD:  $0.31
    Note: USD Calculations based on Gas Price:13 Wei and Ethereum price: $1057 from 07-01-2022.
    Formula: TransactionCost =  (Gas (High) * Gas Price * Ethereum USD Price) / 1,000,000,000

# Resources

@notice Pragma statements tell the compiler to use the version of solidity this
contract was designed for.

@notice Import statements allow the contract to access features of other
contracts. Specifically OpenZeppelin's ERC20, ERC20Burnable, ERC20Capped, and
Ownable libraries.

# Contract

@notice The contract statement defines the contract's name, and the libraries
that it uses.

@notice The ReneeCoin Contract inherits OpenZeppelin's ERC20, ERC20Burnable,
ERC20Capped and Ownable extensions to ensure compliance to the current
standards and provide a strong security basis with code that has been vetted
elsewhere.

# Constructor

@notice The constructor helps set up the initial state of the smart contract.
It is called when the contract is deployed. In the constructor the total number
of Renee Coins which can be in circulation at any given time is capped at
2,000,000. This cap is only set during the deployment of this contract and
cannot be changed later.

@notice The name of the ERC-20 Token and Symbol are also permanently set in the
constructor.

# External Functions

@notice External functions can ONLY be called from other contracts, or users.

## OnlyOwner Functions

@notice OnlyOwner functions are only callable by the owner of the contract.
They are subclass of External Functions.

### createCoins()

@notice When this contract is initially deployed, there are 0 Renee Coins in
existence. New Renee Coins must be 'minted' in order to create them.
createCoins() serves as the minting function for this contract. It can be
called only by the owner and allows them to mint as many Renee Coins as they
like, up to the cap.

This function will ONLY create coins in the Owner's wallet. The airdropCoins()
function can be used to mint coins directly to someone else's wallet.

@param amountOfCoinsToCreate The number of coins that are to be minted.

### airdropCoins()

@notice The airdropCoins() function allows the Owner to mint new Renee Coins
directly into a specified wallet address. This is significantly cheaper than
minting and transferring the coins separately.

This function can ONLY be called by the Owner.

@param recipientAddress The wallet address of the recipient of the airdrop.

@param amountOfCoinsToAirdrop The number of coins that are to be created.

# Public Functions

### decimals()

@notice The decimals() function replaces the inherited functions from the ERC20
and ERC20Capped OpenZeppelin Contracts. For Renee Coins there are 0 decimal
places, these tokens cannot be broken down in smaller increments. This function
is required by the ERC-20 standard.

@return decimalPlaces The amount of decimal places that are supported by these
tokens.

# Internal Functions

@notice Internal functions are only callable by the contract itself. They are
not available to users, the owner, or other contracts.

### \_mint()

@notice The \_mint() function replaces the inherited functions from the ERC20
and ERC20Capped OpenZeppelin Contracts. This is an internal function which can
only be called by the contract itself and is used inside other functions such
as createCoins() and airdropCoins().

@param recipientAddress The wallet address to which coins will be minted.

@param amountOfCoinsToCreate The number of coins that are to be created.
