input_file = "" # input file
mapping_file = "" # mapping file
output_file = "" # output file

mapping = {}

with open(mapping_file, 'r') as m, open(output_file, 'w') as out:

    for m_line in m:
        m_line = m_line.strip().split('\t')

        if m_line[0] not in mapping:
            mapping[m_line[0]] = m_line[1]

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    i.readline()
    out.write("Operon_ID" + '\t' + "Human uniprot" + '\t' + "Human entrez" + '\t' + "GO id" + '\t' + "GO term name" + '\t' + "GO domain" + '\t' + "GO term definition" '\n')

    for line in i:
        line = line.strip().split('\t')

        if line[1] in mapping:

            if len(line) == 6:
                out.write(line[0] + '\t' + line[1] + '\t' + mapping[line[1]] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + line[5] + '\n')
            else:
                out.write(line[0] + '\t' + line[1] + '\t' + mapping[line[1]] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\n')
