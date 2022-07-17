#
#* ----------------------------- Documentation ------------------------------ #
# Module:  whitelist_integration_test.py
# DESCRIPTION
#
#
# Modification History
# 07-17-2022 | SRK | Module Created

#* -------------------------------- Tasks ---------------------------------- #

#* ------------------------------- Imports --------------------------------- #
from control_center import contract_functions
from scripts.helpful_scripts import get_account
#* ------------------------------ Variables -------------------------------- #

#* ---------------------------- Main Function ------------------------------ #

#* ----------------------------- Expected Use Cases --------------------------------- #
# Todo: User Checks if they are whitelisted.


def test_user_checks_their_whitelist_status():

    user_account = get_account(9)

    assert contract_functions.isWhitelisted(user_account) == False


# Todo: Owner adds address to whitelist.

# Todo: Owner removes address from whitelist.

# Todo: Owner sets open minting.
