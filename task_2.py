import random

def get_numbers_ticket(min, max, quantity):
    if not all(isinstance(p, int) and not isinstance(p, bool) for p in (min, max, quantity)):
        return []
    elif min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    elif max - min < quantity:
        return []

    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))
    return sorted(result)