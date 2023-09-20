"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]


def another_function(a: int, b: int, c: str) -> dict[str: tuple[int, int]]:
    """
    Return a dictionary.

    Parameters
    ----------

    a: int
        the number a
    b: int
        the number b
    c: str
        the key c

    Returns
    -------
    dict
        Description
    """
    return {c: (a, b)}
