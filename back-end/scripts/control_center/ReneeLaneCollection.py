from brownie import Contract


class ReneeLaneCollection:
    def __init__(self, address):
        self.address = address
        self.name = self.name()
        contract = Contract(address)

    def build_contract_container(self, address):
        return Contract.from_explorer(address)

    def get_address(self):
        return self.address


def test_get_address():
    rlc = ReneeLaneCollection("0xd732dEC77Bd7725C55A8325D762904876CE8aDB0")
    print(rlc.address)
    print(rlc.contract.name())
    assert rlc.address == "0xd732dEC77Bd7725C55A8325D762904876CE8aDB0"
