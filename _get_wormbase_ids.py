input_file = "" # input file
output_file = "" # output file

ids = []

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    i.readline()

    for line in i:
        line = line.strip().split('\t')
        wb_id = line[1]

        if wb_id not in ids:
            ids.append(wb_id)
            out.write(wb_id + '\n')
