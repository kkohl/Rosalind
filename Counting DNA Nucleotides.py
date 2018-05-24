# Rosalid
# Bioinformatics Stronghold
# ID: DNA

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


# Sample string
s = "TTAAAACGCTGAACAATACTTTATATACTGTTCAGCGTTTGCGCGAGATAGGTCCCGATCTTTCGAATGGAGTACCGACTGACGAGGAGTAAGGGCTATGGGGTATCGGATGGCAGTGCACAGGGGATGGGACTGCCGTCCGGGCTGCGAAATCCGGTCGAAACCTGGTCCTGGCTTCCGAGAACTTATTTATCTCTTGCGCGAAGGCAGAAGAAAAGGTTAAGCGCCTGGGCTGAAAGAGAGCAACCTCCTTGGTTACACCCGCACTGTCCATTCGGATCCAACTCATTCAACTCAGTATATGTATGTTTAATCCCACGTCGTTGCCCGTGTCGCATCTCATTGGTAGTCCCCTCAAATAATACGCCGTGAGGAAGATTCTTCGAGGTCACTTAGCGAATACGGGTCTCGGCTAAACGGGAGACGCAGCATTAGGTGGGCCATCACGCATGGACTCAAGCGGACTGATCGTTTATTTCTCCTCCCGCTCTCTCTCGTGCGCTTGCCGTCCGCTAGGCAGGTAAGATAGCTTAATTCCTTCAAATCGCCTACTTTGATTCGACAAAGGTTGTGGGAGAGCGCTTTACACAGCTAATATTATGAAGAGGTCCCTAAATTGTGGACTGTGCAATGCAACTAATTAAGTCCAGCGGCATGGCTGGACCTCGGGATGCAGATCCTCTCGAGCTGTTCGTTCGGATTGACTAAGCTTAGTGCTCCACTGGCCTAGAGTAACTGTGCCGAGAGATGGGCTCCCAACCCGATTCTCAAACTACGTCACGTCGCCCCAGGATCAGCCGGCAATCGTTCTTAAAGAGGCAGTTCCGCCCCCCTTGACAATAGGCCCTTCCCTGTTCCATGCAAATTACGAGGTAGGACTGAAAGTACCGTCATACATCACAGC"

# Set variable for number of each base
A_count = s.upper().count("A")
C_count = s.upper().count("C")
G_count = s.upper().count("G")
T_count = s.upper().count("T")

# Print Results
print(str(A_count) + " " + str(C_count) + " "+ str(G_count) + " " + str(T_count))

