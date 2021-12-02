def input_to_list(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines
