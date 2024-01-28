def print_formatted(number):

    formatted_lines = []
    for i in range(1, number + 1):
        adj_size = len(bin(number)[2:])
        line = (str(i).rjust(adj_size), str(oct(i)[2:]).rjust(adj_size),
                str(hex(i).upper())[2:].rjust(adj_size), str(bin(i)[2:]).rjust(adj_size))
        formatted_lines.append(line)

    return formatted_lines
