//\* ----------------------------- Documentation --------------------------- //

@title Renee Coins

@author Scott Kostolni

@notice Version 0.0.0 beta

@notice This is a bespoke ERC-20 Contract that provides the social currency,
Renee Coins, which grants benefits to investors and artists of The Renee Lane
NFT Collection.

@notice This contract acts as the ledger for the Renee Coins and allows for
Renee Coins to be created, tracked, and transferred or traded between wallets.
It uses the OpenZeppelin contracts as a back bone with extension allowing a
maximum cap to be specified, and for the owner to destroy or burn their tokens.
The OpenZepplin Ownable extension is used to set an Owner for the contract and
ensure certain functions are ONLY callable by the Owner.
