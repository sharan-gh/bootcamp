def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material =='RNA':
            return 'U'
    elif base in 'TtUut':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        print('improper input')
        return 'error'
        
def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a nucleic acid sequence."""
    # Initialize empty string
    rev_comp = ''
    # Loop through and add new function
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)
    return rev_comp
