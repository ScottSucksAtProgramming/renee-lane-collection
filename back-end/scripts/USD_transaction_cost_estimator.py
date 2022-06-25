# ------------------------------ Documentation ------------------------------ #
# Module:  USD_transaction_cost_estimator.py
# This is a utility module which converts a Gas Cost into USD using the
# formula: USDCost =  (Gas * gasPrice * EthPrice) / 1,000,000,000. This module
#  was build using Test Driven Development as practice.
#
#
# Modification History
# DATE INITIAL UPDATE.
# 06-21-2022 | SRK | Module Created

# -------------------------------- Tasks ----------------------------------- #
# getUSDTransactionCost() can be called. - Done
# getUSDTransactionCost() takes and returns Gas. - Done
# getUSDTransactionCost() returns current ethPrice. - Done
# getUSDTransactionCost() returns gasPrice. - Done
# getUSDTransactionCost() returns calculated USDCost. - Done

# ------------------------------- Resources -------------------------------- #
import os, random, requests
from dotenv import load_dotenv

# ------------------------------- Variables -------------------------------- #
ETHERSCAN_API = os.environ.get("ETHERSCAN_API")

# ------------------------------ Functions --------------------------------- #
def getRandomGas():
    return random.randint(0, 1_000_000_000)


def getUsedGasAmounts():
    gasList = []
    transactions = int(input("How many transactions are you calculating: "))
    for i in range(transactions):
        gasList.append(int(input(f"Enter gas used in transaction {i}: ")))
    return transactions, gasList


def getUSDTransactionCost(gas):
    load_dotenv()
    ethPrice = int(
        requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
        ).json()["USD"]
    )
    gasPrice = int(
        requests.get(
            f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API}"
        ).json()["result"]["SafeGasPrice"]
    )
    transactionCost = "$" + str(round((gas * ethPrice * gasPrice) / 1_000_000_000, 2))
    print(f"\nGas Used:       {gas}")
    print(f"Gas Price:        {gasPrice}")
    print(f"Ether Price:      {ethPrice}")
    print(f"Transaction Cost: {transactionCost}\n")
    return (gas, ethPrice, gasPrice, transactionCost)


# ----------------------------- Main Function ------------------------------ #
def main():
    gasAmounts = getUsedGasAmounts()
    for i in range(gasAmounts[0]):
        getUSDTransactionCost(gasAmounts[1][i])


# ---------------------------- Test Functions ------------------------------ #
def test_getUSDTransactionCost_returns_gas_when_gas_passed():
    # Arrange
    random_gas = getRandomGas()
    # Act and Assert
    assert getUSDTransactionCost(random_gas)[0] == random_gas


def test_getUSDTransactionCost_obtains_and_returns_ethPrice():
    # Arrange
    # Act and Assert
    assert getUSDTransactionCost(getRandomGas())[1] != None


def test_getUSDTransactionCost_obtains_and_returns_gasPrice():
    # Act
    # Assert
    assert getUSDTransactionCost(getRandomGas())[2] != None


def test_getUSDTransactionCost_calculates_price_in_USD():
    # Arrange
    random_gas = getRandomGas()
    # Act
    function_info = getUSDTransactionCost(random_gas)
    gasUsed = function_info[0]
    ethPrice = function_info[1]
    gasPrice = function_info[2]
    expected_transaction_cost = "$" + str(
        round((gasUsed * ethPrice * gasPrice) / 1_000_000_000, 2)
    )
    actual_transaction_cost = function_info[3]
    # Assert
    assert actual_transaction_cost == expected_transaction_cost
