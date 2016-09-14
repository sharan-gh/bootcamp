import bioinfo_dicts
def one_to_three(seq):
    seq = seq.upper()

    #build conversion
    aa_list = []
    for amino_acid in seq:
        if amino_acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[amino_acid], '-']
        else:
            raise RuntimeError(amino_acid + 'is not a valid amino acid.')
    return ''.join(aa_list[:-1])

    # Good code includes checks that generate informative error messages


try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False

seq = 'ATTACTACGACTACG'

if have_gc:
    print(gc_content.gc(seq))
else:
    print(seq.count('G') + seq.count('C')/len(seq))

 #This says, don't worry if I have forgotten to import a module, and keep running the program
 #I have installed a backup further down, even if that function isn' as efficient.

 #This is how the try function works. The except function 'creates an exception' for a particular type of error. 
