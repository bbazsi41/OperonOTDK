mapping_file = "" # mapping file
input_file = "" # iput tsv file
output_file = "" # output file

mapping_dictionary = {}

with open(mapping_file, 'r') as mapping:

    for line in mapping:
        line = line.strip().split('\t')

        wormbase_id = line[0]
        uniprot_id = line[1]

        if wormbase_id not in mapping_dictionary:
            mapping_dictionary[wormbase_id] = uniprot_id

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    i.readline()

    for input_line in i:
        input_line = input_line.strip().split('\t')

        wb_id = input_line[1]
        if wb_id not in mapping_dictionary:
            continue

        input_line[1] = mapping_dictionary[wb_id]
        out.write('\t'.join(input_line) + '\n')
