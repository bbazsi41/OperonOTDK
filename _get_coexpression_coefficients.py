import numpy as np
from scipy import stats


input_file = "" # input file
output_file = "" # output file
number_of_expression_columns = 4

operons_info = {}

with open(input_file, 'r') as input_expressions:

    input_expressions.readline()

    for input_line in input_expressions:
        input_line = input_line.strip().split('\t')

        if number_of_expression_columns == 4:
            expression_one = float(input_line[2])
            expression_two = float(input_line[3])
            expression_three = float(input_line[4])
            expression_four = float(input_line[5])
            all_data = [input_line[1], expression_one, expression_two, expression_three, expression_four]

            if number_of_expression_columns == 7:
                expression_five = float(input_line[6])
                expression_six = float(input_line[7])
                expression_seven = float(input_line[8])
                all_data = [input_line[1], expression_one, expression_two, expression_three, expression_four,
                            expression_five, expression_six, expression_seven]

                if number_of_expression_columns == 10:
                    expression_eight = float(input_line[9])
                    expression_nine = float(input_line[10])
                    expression_ten = float(input_line[11])
                    all_data = [input_line[1], expression_one, expression_two, expression_three, expression_four,
                                expression_five, expression_six, expression_seven, expression_eight, expression_nine,
                                expression_ten]

        if input_line[0] not in operons_info:
            operons_info[input_line[0]] = []
        if all_data not in operons_info[input_line[0]]:
            operons_info[input_line[0]].append(all_data)

with open(output_file, 'w') as out:

    out.write("Operon_ID" + '\t' + "Gene_1_ID" + '\t' + "Gene_2_ID" + '\t' + "Spearmann_coefficient" + '\t' + "P_value" + '\n')

    for operon in operons_info:

        for x in range(0, len(operons_info[operon]) - 1):

            for y in range(x + 1, len(operons_info[operon])):

                gene_one = operons_info[operon][x][0]
                if number_of_expression_columns == 4:
                    array_one = [operons_info[operon][x][1], operons_info[operon][x][2], operons_info[operon][x][3],
                                 operons_info[operon][x][4]]

                elif number_of_expression_columns == 7:
                    array_one = [operons_info[operon][x][1], operons_info[operon][x][2], operons_info[operon][x][3],
                                 operons_info[operon][x][4], operons_info[operon][x][5], operons_info[operon][x][6],
                                 operons_info[operon][x][7]]

                elif number_of_expression_columns == 10:
                    array_one = [operons_info[operon][x][1], operons_info[operon][x][2], operons_info[operon][x][3],
                                 operons_info[operon][x][4], operons_info[operon][x][5], operons_info[operon][x][6],
                                 operons_info[operon][x][7], operons_info[operon][x][8], operons_info[operon][x][9],
                                 operons_info[operon][x][10]]

                gene_two = operons_info[operon][y][0]
                if number_of_expression_columns == 4:
                    array_two = [operons_info[operon][y][1], operons_info[operon][y][2], operons_info[operon][y][3],
                                 operons_info[operon][y][4]]

                elif number_of_expression_columns == 7:
                    array_two = [operons_info[operon][y][1], operons_info[operon][y][2], operons_info[operon][y][3],
                                 operons_info[operon][y][4], operons_info[operon][y][5], operons_info[operon][y][6],
                                 operons_info[operon][y][7]]

                elif number_of_expression_columns == 10:
                    array_two = [operons_info[operon][y][1], operons_info[operon][y][2], operons_info[operon][y][3],
                                 operons_info[operon][y][4], operons_info[operon][y][5], operons_info[operon][y][6],
                                 operons_info[operon][y][7], operons_info[operon][y][8], operons_info[operon][y][9],
                                 operons_info[operon][y][10]]

                # coexpression_value = np.corrcoef(array_one, array_two)[0, 1]
                coef = stats.spearmanr(array_one, array_two)

                out.write(operon + '\t' + gene_one + '\t' + gene_two + '\t' + format(coef) + '\n')
