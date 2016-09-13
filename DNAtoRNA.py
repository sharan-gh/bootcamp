def rna(seq):
    """Convert DNA sequence to RNA. The returned sequences have the same capitalization as the input sequence."""
    #convert to uppercase
    seq = seq.upper()
    return seq.replace('T','U')
