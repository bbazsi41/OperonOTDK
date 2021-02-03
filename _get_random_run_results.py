import random


input_file = "" # input file
output_file = "" # output file

number_of_different_groups = {
    2: 984,
    3: 301,
    4: 100,
    5: 42,
    6: 11,
    7: 4,
    8: 3,
}

genes = []

with open(input_file, 'r') as i, open(output_file, 'w') as out:

    i.readline()

    for line in i:
        line = line.strip().split(",")

        if line[1] not in genes:
            genes.append(line[1])

with open(output_file, 'w') as out:

    for n in number_of_different_groups:

        index = 1

        while index <= number_of_different_groups[n]:
            x = 1

            while x <= n:
                choosen_gene = random.choice(genes)
                genes.remove(choosen_gene)
                group_id = f"{n}_{index}"
                out.write(group_id + '\t' + choosen_gene + '\n')
                x += 1

            index += 1
