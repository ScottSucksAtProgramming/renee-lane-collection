from scripts.control_center.rlc_contract import RLC

rlc_1 = RLC


def main():

    print(get_name())


def get_name():
    return rlc_1.name


def test_get_name():
    assert get_name() == "RLC"
