input_file = "" # input file
output_file = "" # output file

ids = []

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    i.readline()

    for line in i:
        line = line.strip().split('\t')

        if line[3] not in ids:
            out.write(line[3] + '\n')
            ids.append(line[3])
