# Rosalid
# Bioinformatics Stronghold
# ID: GC


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

file = "file_path_placeholder"


def gc_content(fasta_file):

    d = {}
    with open(fasta_file, "r") as file:
        fasta = file.read()

        for block in fasta.split(">")[1:]:

            strand = block.split("\n")

            name = strand[0]
            seq = "".join(strand[1:])

            gc_content = 100*((seq.count("G") + seq.count("C")) / len(seq))

            d[gc_content] = name

    return str(d[max(d)]) + "\n" + str(max(d))


print(gc_content(file))
