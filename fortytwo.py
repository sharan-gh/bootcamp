def answer_to_the_ultimate_q_of_life_univ_everything():
    """Simple program."""
    return 42

def complement_base(base):
    """Return the Watson-Crick complement of a base."""

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
