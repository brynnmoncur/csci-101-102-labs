  #   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 4 - Lab B - Amino Acids
        #   References: 
        #   Time: 25 minutes

print("Input the chemical elements of the amino acid:")
C = int(input("CARBON>"))
H = int(input("HYDROGEN>"))
N = int(input("NITROGEN>"))
O = int(input("OXYGEN>"))
S = int(input("SULFUR>"))

amino_acid_eqn = str(f"{C}C--{H}H--{N}N--{O}O--{S}S")
amino_acid_name = str()

if C == 3 and H == 7 and N ==1 and O == 2 and S == 0:
    amino_acid_name = "Alanine"

elif C == 6 and H == 14:
    amino_acid_name = "Arginine"

elif C == 4:
    amino_acid_name = "Asparagine"

elif C == 3 and H == 7 and N == 1 and O == 2 and S == 1:
    amino_acid_name = "Cysteine"

elif C == 6 and H == 9:
    amino_acid_name = "Histidine"

elif C == 5:
    amino_acid_name = "Glutamine"

print(f"The amino acid for {amino_acid_eqn} is {amino_acid_name}")
print(f"OUTPUT {amino_acid_eqn}")
print(f"OUTPUT {amino_acid_name}")








