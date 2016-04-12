import csv
import re
import os

#List of all mutations and keywords to be found in the file
mutation = [
r"Sample:",
r"Analyzed:",
r"Raw_Signal",
r"Wt_Allele",
r"del_e2e3",
r"intron_1",
r"E60X",
r"R75X",
r"G85E",
r"394delTT",
r"405+3A>C",
r"406-1G>A",
r"444delA",
r"R117C",
r"R117H",
r"Y122X",
r"621+1G>T",
r"G178R",
r"711+1G>T",
r"L206W",
r"935delA",
r"deltaF311",
r"1078delT",
r"G330X",
r"R334W",
r"R347P",
r"R347H",
r"R352Q",
r"S364P",
r"A455E",
r"G480C",
r"Q493X",
r"dI507",
r"dF508",
r"1677delTA",
r"V520F",
r"1717-1G>A",
r"G542X",
r"S549N",
r"S549R(T>G)",
r"G551D",
r"R553X",
r"A559T",
r"R560T",
r"1812-1G>A",
r"1898+1G>A",
r"1898+5G>T",
r"G622D",
r"2055del9>A",
r"2143delT",
r"2183AA>G",
r"2184delA",
r"K710X",
r"2307insA",
r"2789+5G>A",
r"Q890X",
r"2869insG",
r"3120G>A",
r"3120+1G>A",
r"3199del6",
r"R1066C",
r"W1089X",
r"Y1092X-C>G",
r"Y1092X-C>A",
r"M1101K",
r"D1152H",
r"R1158X",
r"R1162X",
r"3659delC",
r"S1196X",
r"S1255X(ex.19)",
r"S1255X(ex.20)",
r"3791delC",
r"3849+10kbC>T",
r"3876delA",
r"3905insT",
r"W1282X",
r"N1303K",
r"5T",
r"7T",
r"9T",
r"I506V",
r"I507V",
r"F508C"
]

#File locations, all should be in same directory
replace_file = r"replace_words.csv"
space_delimited_csv = r"CF70_150826.csv"
csv_file = r"csv_outfile.csv"

#Remove output file if it exists, to prevent errors
if os.path.exists(csv_file):
    os.remove(csv_file)

#Makes file comma delimited, rather than space delimited
old_new = [i.strip().split(',') for i in open(replace_file)]


new_line = []
analyzed_count = 0
with open(space_delimited_csv) as fin, open(csv_file, 'wb') as fout:
    o=csv.writer(fout)
    for line in fin:
        for oldword, newword in old_new:
            #Replaces certain sets of words with underscores between them
            line = line.replace(oldword, newword)

        #Only lines starting with a mutation or keyword are written. Must have correct range of fields.
        if any(word in line[:10] for word in mutation) and len(line.split()) > 2 and len(line.split()) < 17:

            #Exceptions for lines typically involve inserting blank spaces to the csv.

            #"Analyzed" info line only needs to be written once.
            if r"Analyzed:" == line[:9]:
                if analyzed_count < 1:
                    o.writerow(line.split())
                    analyzed_count += 1
                else:
                    pass

            elif r"Wt_Allele" == line[:9]:
                line_list = line.split()
                line_list.insert(0, "")
                line_list.insert(1, "")
                o.writerow(line_list)

            elif r"Sample:" == line[:7]:
                line_list = line.split()
                line_list.remove(line_list[1])
                line_list.remove(line_list[1])
                line_list.remove(line_list[1])
                o.writerow(new_line)
                o.writerow(line_list)

            elif r"Variation" == line[:9]:
                line_list = line.split()
                line_list.insert(3, "")
                line_list.insert(5, "")
                line_list.insert(7, "")
                line_list.insert(9, "")
                line_list.insert(11, "")
                line_list.insert(12, "")
                o.writerow(line_list)

            elif r"del_e2e3" == line[:8]:
                line_list = line.split()
                line_list.insert(8, "")
                line_list.insert(9, "")
                o.writerow(line_list)

            elif r"intron_1" in line[:8]:
                line_list = line.split()
                line_list.insert(1, "")
                line_list.insert(3, "")
                line_list.insert(5, "")
                o.writerow(line_list)

            elif r"R347H" in line[:5]:
                line_list = line.split()
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"dF508" == line[:5]:
                line_list = line.split()
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"2184delA" in line[:8]:
                line_list = line.split()
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"Y1092X-C>A" in line[:10]:
                line_list = line.split()
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"G551D" in line[:5]:
                line_list = line.split()
                line_list.insert(11, "")
                #line_list.insert(12, "")
                o.writerow(line_list)

            elif r"5T" in line[:2]:
                line_list = line.split()
                line_list.remove(line_list[2])
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"7T" in line[:2]:
                line_list = line.split()
                line_list.insert(1, "")
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"9T" in line[:2]:
                line_list = line.split()
                line_list.insert(1, "")
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                o.writerow(line_list)

            elif r"I506V" in line[:5]:
                line_list = line.split()
                line_list.remove(line_list[2])
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(9, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                line_list.insert(12, "")
                o.writerow(line_list)

            elif r"I507V" in line[:5]:
                line_list = line.split()
                line_list.insert(1, "")
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(9, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                line_list.insert(12, "")
                o.writerow(line_list)

            elif r"F508C" in line[:5]:
                line_list = line.split()
                line_list.insert(1, "")
                line_list.insert(2, "")
                line_list.insert(4, "")
                line_list.insert(6, "")
                line_list.insert(8, "")
                line_list.insert(9, "")
                line_list.insert(10, "")
                line_list.insert(11, "")
                line_list.insert(12, "")
                o.writerow(line_list)
                
            else:
                #Write lines that are not exceptions, and pass criteria 
                o.writerow(line.split())
        else:
            pass