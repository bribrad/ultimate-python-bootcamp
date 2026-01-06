def chai_flavor(flavor="masala"):
    """Return the flavor of chai"""

    return flavor

print(chai_flavor.__doc__)


def generate_bill(chai=0, samosa=0):
    """

    Calculate the total bill for chai and samosas

    :param chai: Number of chai
    :param samosa: Number of samosas
    :return: (Total amount, thank you message as a string)
    """
    pass

print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill.__kwdefaults__)
    