operon_genes_file = "" # file with the operons
go_terms_genes_file = "" # file with GO Terms
output_file = "" # output file

operon_genes = []
genes_with_go_terms = []

with open(operon_genes_file, 'r') as operon_file:

    operon_file.readline()

    for operon_line in operon_file:
        operon_line = operon_line.strip().split('\t')

        if operon_line[1] not in operon_genes:
            operon_genes.append(operon_line[1])

with open(go_terms_genes_file, 'r') as go_terms_file, open(output_file, 'w') as out:

    go_terms_file.readline()

    for go_line in go_terms_file:
        go_line_out = go_line.strip()
        go_line = go_line_out.split(",")

        if go_line[1] in operon_genes:
            continue

        if go_line[2] == "":
            continue

        out.write(go_line_out + '\n')
