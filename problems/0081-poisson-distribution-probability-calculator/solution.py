import math

def poisson_probability(k: int, lam: float) -> float:
    """
    Calculates the probability P(X = k) for a Poisson distribution.
    
    Parameters:
        k (int): Number of occurrences (k >= 0).
        lam (float): Average rate of occurrence (lambda > 0).
        
    Returns:
        float: The exact probability P(X = k).
    """
    if k < 0 or not isinstance(k, int):
        return 0.0
    if lam <= 0:
        raise ValueError("Lambda must be strictly positive.")
    
    # Formula: (lam^k * e^-lam) / k!
    return (lam ** k * math.exp(-lam)) / math.factorial(k)