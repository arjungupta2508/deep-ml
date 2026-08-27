import math
import math

def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function (PDF)
    of the normal distribution.
    """

    final_result = (
        1 / ((2 * math.pi * std_dev**2) ** 0.5)
    ) * math.e ** (
        -((x - mean)**2) / (2 * std_dev**2)
    )

    return round(final_result, 5)