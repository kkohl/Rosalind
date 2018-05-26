# Rosalid
# Bioinformatics Stronghold
# ID: GC


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

file = "file_path_placeholder"


def gc_content(fasta_file):
	
	# initiate dictionary
    d = {}
	
	# open fasta file
    with open(fasta_file, "r") as file:
		# read file 
        fasta = file.read()
		
		# loop through file by strand, delimiter of file is ">"
        for block in fasta.split(">")[1:]:
			
			# create list from new lines
            strand = block.split("\n")
			
			# set name variable with strand characteristics
            name = strand[0]
			
			# Sequence is all other list items
			# needed as strand with is limited to ~60 characters
            seq = "".join(strand[1:])
			
			# Calculate gc content
            gc_content = 100*((seq.count("G") + seq.count("C")) / len(seq))
			
			# Add content as dict keys and name as values
            d[gc_content] = name

    return str(d[max(d)]) + "\n" + str(max(d))


print(gc_content(file))
