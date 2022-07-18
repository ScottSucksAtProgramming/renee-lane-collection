# The Renee Lane Collection Testing Suite

## Overview

The testing suite for contracts of this project are stored in the tests folder
(located in back-end) and are split into unit tests and integration tests. Both
testing levels are then split into the contracts. At the time of this document
only unit testing has been started.

## Unit Testing

Unit tests were written in Python. The tests have been modularized into
separate python files based on category including:

-   Contract Level Behaviors
-   Constructor Level Behaviors
-   Function Level Behaviors

### Renee Coins Testing Suite

#### Contract Behaviors Tested

-   Contract Deploys and returns address.
-   Contract has all ERC20 functions.
-   Contract has ERC20Burnable Functions.
-   Contract has ERC20Capped Functions.
-   Contract has Ownable Functions.

#### Constructor Behaviors Tested

-   Contract returns correct name.
-   Contract returns correct symbol.
-   Contract returns correct token cap.
-   Contract returns correct owner.

#### createCoins() Behaviors Tested

-   CreateCoins() mints the correct amount of Renee Coins.
-   CreateCoins() mints to the correct wallet.
-   Transaction reverts if CreateCoins() would exceed cap.
-   Transaction reverts if CreateCoins() called by someone other than owner.

#### airdropsCoins() Behaviors Tested

-   airdropCoins() mints the correct amount of Renee Coins.
-   airdropCoins() mints to the correct wallet.
-   Transaction reverts if airdropCoins() would exceed cap.
-   Transaction reverts if airdropCoins() called by someone other than owner.

#### decimals() Behaviors Tested

-   decimals() returns correct number.

#### transfer() Behaviors Tested

-   Renee Coins can be transferred.
-   Transaction reverts when attempting to send more coins than owned.
-   Transaction reverts when attempting to send to the zero address.
-   Transaction logs are correct.

#### approval() and allowance() Behaviors Tested

-   Approvals can be set.
-   Allowance can be increased.
-   Allowance can be decreased.
-   Approvals revert if the spender is the zero address.
-   Approvals revert if the value is negative.
-   Approval logs are correct.

#### transferFrom() Behaviors Tested

-   Renee Coins can be transferred by approved spender.
-   Transfer of 0 coins does not revert.
-   Transaction reverts if amount is greater than sender's allowance.
-   Transaction reverts if recipient address is the zero address.
-   TransferFrom logs are correct.

#### burn() Behaviors Tested

-   Token owner can burn tokens.
-   Burn reverts if balance below amount to be burnt.
-   Burn logs are correct.
-   BurnFrom can burn tokens from approved address.
-   BurnFrom reverts if spender not approved.
-   BurnFrom logs are correct.

#### Ownable Extension Behaviors Tested

-   Owner returns expected value.
-   Owner can transfer ownership.
-   Owner can renounce ownership.
-   Renounce ownership can only be called by owner.
-   Transfer ownership can only be called by owner.

### Renee Lane Collection Testing Suite

#### Contract Behaviors Tested

#### Constructor Behaviors Tested

#### createCoins() Behaviors Tested

#### airdropsCoins() Behaviors Tested

#### decimals() Behaviors Tested

#### transfer() Behaviors Tested

#### approval() and allowance() Behaviors Tested

#### transferFrom() Behaviors Tested

#### burn() Behaviors Tested

#### Ownable Extension Behaviors Tested
