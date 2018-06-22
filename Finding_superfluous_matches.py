'''
Using the SAM output file:
cut -f1 file.sam > out1.txt
cut -f4 file.sam > out2.txt
awk -F"_" '{ print $10(number of _ +1)}' out1.txt > out1_1.txt
cut -f10 (last field) out1_1.txt > out1_2.txt
paste out1_2.txt out2.txt > out3.txt
then remove all unnessisary rows at top:
awk 'NR > 3' out3.txt > outfile.txt
save to folder
'''



import numpy as np

input_filename = '/home/18969577/Documents/Genolve/Data_analysis/Bowtie2_Output/test_file.txt'

input_file = np.loadtxt(input_filename, delimiter="\t")
number_of_superfluous_matches = 0
for row in input_file:
    if row[1] == 0:
        pass
    elif 4800 <= row[1] <= 6200:
        pass
    elif 20800 <= row[1] <= 21000:
        pass
    else:
        if (row[1] - row[0]) > 100:
            number_of_superfluous_matches += 1
        elif (row[0] - row[1]) > 100:
            number_of_superfluous_matches +=1
        else:
            pass
print(number_of_superfluous_matches)


