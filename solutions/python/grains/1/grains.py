def square(number):
    """Calculates the number of grains on a specific square (1-64)."""
    # Check if the square number is within the valid chessboard range
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
        
    return 1 << (number - 1)


def total():
    """Calculates the total number of grains on the entire 64-square chessboard."""
    # A fully filled board equals (2^64) - 1 grains
    return (1 << 64) - 1
