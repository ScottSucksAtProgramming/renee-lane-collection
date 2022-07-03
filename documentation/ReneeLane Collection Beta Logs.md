# Renee Lane Collection Beta Deployment

-   ReneeLaneCollection.sol Version: 0.0.0 beta
-   Date Deployed: July 3rd, 2022
-   Blockchain: Rinkeby (Ethereum Testnet)
-   Contract Address: 0xB6bEF169AE0c686cA030236F75769074d6A0C7d5

## Gas Costs

-   Deployment:

    -   USD Price: $126.59
    -   Gas Usage: 5,004,354 Gas
    -   Gas Price: 24 Wei
    -   Ether USD Price: $1,054

-   addToWhiteList:

    -   USD Price: $0.68
    -   Gas Usage: 46,099 Gas
    -   Gas Price: 14 Wei
    -   Ether Price $1,053

-   mintArtwork:

    -   USD Price: $3.54
    -   Gas Usage: 222,961 Gas
    -   Gas Price: 15 Wei
    -   Ether Price $1,059

# Renee Lane Collection Logs

## Deployment

Running 'scripts/deploy_renee_lane_collection.py::main'... Transaction sent:
0xf08a223b2c9da2f74eef604704202f03ac94ad0fe675232744c650704216a26e Gas price:
1.500000008 gwei Gas limit: 5504789 Nonce: 249 ReneeLaneCollection.constructor
confirmed Block: 10960823 Gas used: 5004354 (90.91%) ReneeLaneCollection
deployed at: 0xB6bEF169AE0c686cA030236F75769074d6A0C7d5

Waiting for https://api-rinkeby.etherscan.io/api to process contract...
Verification submitted successfully. Waiting for result... Verification
pending... Verification pending... Verification complete. Result: Pass -
Verified The Renee Lane Collection contract has been deployed on the
['rinkeby'] network. The contract address is
0xB6bEF169AE0c686cA030236F75769074d6A0C7d5

## Set Open Minting (addToWhiteList(ZERO_ADDRESS))

Running 'scripts/renee_lane_collection_set_open_minting.py::main'...
Transaction sent:
0x9659290167f3ac0fd262ce459b3f104faca5bfed33587080f2c92413890501a3 Gas price:
1.500000008 gwei Gas limit: 50708 Nonce: 250 ReneeLaneCollection.addToWhitelist
confirmed Block: 10960855  
 Gas used: 46099 (90.91%)

Attempting to whitelist 0x0000000000000000000000000000000000000000.
ReneeLaneCollection.addToWhitelist confirmed Block: 10960855 Gas used: 46099
(90.91%)

Success! Minting Should be open for all.

## Minting Artwork 1

Running 'scripts/renee_lane_collection/mintArtwork_RLC.py::main'...

Which Image (1-50) would you like to mint? 1 The Price of your Art Piece is:
0.12 Ether. Would you like to mint your Art Piece? (y/n) y Transaction sent:
0x75a597c02e03e2dc8872c7f0210349ea34589498abcd001f31b22e2bed12ac52 Gas price:
1.50000001 gwei Gas limit: 245257 Nonce: 251 ReneeLaneCollection.mintArtwork
confirmed Block: 10961226  
 Gas used: 222961 (90.91%)

Attempting to Mint Art Piece. ReneeLaneCollection.mintArtwork confirmed Block:
10961226  
 Gas used: 222961 (90.91%)

Art Piece Minted!
