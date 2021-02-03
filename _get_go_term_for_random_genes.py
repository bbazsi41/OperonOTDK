input_file = "" # input file
output_file = "" # output file
go_file = "" # file which contains the GO annotations

genes_data = {}

with open(go_file, 'r') as go_file:

    go_file.readline()

    for go_line in go_file:
        def_line = go_line.strip()
        go_line = go_line.strip().split(",")

        if go_line[3] == "":
            continue

        gene_id = go_line[1]
        go_term_id = go_line[2]
        go_term_name = go_line[3]
        go_domain = go_line[-1]

        go_definition = def_line.split('"')[1]

        out_array = [go_term_id, go_term_name, go_domain, go_definition]

        if gene_id not in genes_data:
            genes_data[gene_id] = []

        if out_array not in genes_data[gene_id]:
            genes_data[gene_id].append(out_array)

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    for line in i:
        line = line.strip().split('\t')

        if line[1] in genes_data:

            for gene_data in genes_data[line[1]]:
                out.write('\t'.join(line) + '\t' + '\t'.join(gene_data) + '\n')
