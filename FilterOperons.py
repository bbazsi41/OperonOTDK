import sys


operon_file = "" # file with the operons/genes
output_file = "" # output file

lines_in_input = sum(1 for line in open(operon_file))
go_terms_for_genes = {}
genes_of_the_operon = {}
duplicated_operons = {}

with open(operon_file, 'r') as f:

    f.readline()

    for line in f:
        line = line.strip().split('\t')

        operon_id = line[0]
        gene_id_in_operon = line[1]
        go_term = line[3]

        if gene_id_in_operon not in go_terms_for_genes:
            go_terms_for_genes[gene_id_in_operon] = set()
        go_terms_for_genes[gene_id_in_operon].add(go_term)

        if operon_id not in genes_of_the_operon:
            genes_of_the_operon[operon_id] = set()
        genes_of_the_operon[operon_id].add(gene_id_in_operon)

for operons, genes in genes_of_the_operon.items():

    results = []
    not_common_go_terms = []
    common_go_terms = []

    for gene in genes:
        results.append(go_terms_for_genes[gene])

    for go_terms in results:
        for go in go_terms:
            if go not in not_common_go_terms:
                not_common_go_terms.append(go)
            else:
                if go not in common_go_terms:
                    common_go_terms.append(go)

    duplicated_operons[operons] = common_go_terms

with open(operon_file, 'r') as operon, open(output_file, 'w') as out:

    operon.readline()
    index = 0
    out.write("Operon_ID" + '\t' + "Human uniprot" + '\t' + "Human entrez" + '\t' + "Worm entrez" + '\t' +
              "Worm ensembl" + '\t' + "GO id" + '\t' + "GO term name" + '\t' + "GO domain" + '\t' +
              "GO term definition" '\n')
    checking_set = set()

    for operon_line in operon:
        operon_line = operon_line.strip()
        op_line = operon_line.split('\t')
        percent = int(index / lines_in_input * 100)
        sys.stdout.write(f"\r{index}/{lines_in_input} | {percent}%")

        if op_line[0] in duplicated_operons:
            if op_line[3] in duplicated_operons[op_line[0]]:
                pairs = f'{op_line[1]}_{op_line[3]}'
                if pairs not in checking_set:
                    checking_set.add(pairs)
                    out.write(operon_line + '\n')

        index += 1

sys.stdout.write(f"\r{lines_in_input}/{lines_in_input} | 100%")
print("")
