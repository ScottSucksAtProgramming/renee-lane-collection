# ------------------------------ Documentation ------------------------------ #
# Module:  metadata_template.py
# This module contains the metadata template used to create finalized metadata
# for the Non-Fungible Tokens. It is used in conjunction with the
# create_metadata.py script to create the JSON files.
#
#
# Modification History
# 05-03-2022 | SRK | Module Imported to Project.

# -------------------------------- Tasks ----------------------------------- #
# Todo: Create Field for Print Name,
# Todo: Create Field for Description,
# Todo: Create Field for Image URI,
# Todo: Create Property for Royalty Fee and Royalty Address
# Todo: Create Property for
# Todo: Create Property for Artist,
# Todo: Create Property for Medium
# Todo: Create Property for Photo Source
# Todo: Create Property for Title
# Todo: Create Property for Edition
# ------------------------------- Resources -------------------------------- #
metadata_template = {

    # Name of the item.
    "name": "",                                         # Task 1

    # A human readable description of the item. Markdown is supported.
    "description": "",

    # This is the URL that will appear below the asset's image on OpenSea and
    # will allow users to leave OpenSea and view the item on your site.
    "external_url": "",

    # This is the URL to the image of the item. Can be just about any type of
    # image (including SVGs, which will be cached into PNGs by OpenSea), and
    # can be IPFS URLs or paths. We recommend using a 350 x 350 image.
    "image": "",

    # These are the attributes for the item, which will show up on the OpenSea
    # page for the item. (see below)
    "attributes": [
        {
            "trait_type": "Artist",
            "value": "",
        },
        {
            "trait_name": "Medium",
            "value": "",
        },
        {
            "trait_name": "Photo Source",
            "value": "",
        },
        {
            "trait_name": "Title",
            "value": "",
        },
        {
            "display_type": "",
            "trait_type": "Edition",
            "value": "",
            "max_value": "",
        },
    ],
    "Royalty Percentage": "10%",
    "Royalty Address": "",
}
# ------------------------------ Functions --------------------------------- #
