import sys

def enough_argument_test():  # Checks if there are 3 arguments
    if len(sys.argv) != 3:
        print("ERROR: This program needs two command line arguments to run, where the first one is the input file and the second one is the output file!")
        print("Sample run command: python3 calculator.py input.txt output.txt")
        print("Program is going to terminate!")
        sys.exit(1)

def calculate(line):
    try:
        # Splits the line into operators
        operators = line.strip().split()

        # Checks if the line is empty
        if not operators:
            return None

        # Checks if the line has 3 operators
        if len(operators) != 3:
            return "{}\nERROR: Line format is erroneous!".format(line.strip())

        string_first_op, operator, string_second_op = operators

        # Checks if operands are numbers
        try:
            first_op = float(string_first_op)
        except ValueError:
            return "{}\nERROR: First operand is not a number!".format(line.strip())
        try:
            second_op = float(string_second_op)
        except ValueError:
            return "{}\nERROR: Second operand is not a number!".format(line.strip())

        # Makes calculations based on the operator
        if operator == '+':
            result = first_op + second_op
        elif operator == '-':
            result = first_op - second_op
        elif operator == '*':
            result = first_op * second_op
        elif operator == '/':
            result = first_op / second_op
        else:
            return "{}\nERROR: There is no such an operator!".format(line.strip())

        return "{}\n={:.2f}".format(line.strip(), result)

    except Exception as x:
        return str(x)

def output_writer(input_file, output_file):  # Writes the output to the output.txt
    results = []
    try:
        with open(input_file, 'r') as input1:
            for line in input1:
                result = calculate(line)
                if result is not None:
                    results.append(result)

        # Write the results to the output file
        with open(output_file, 'w') as output1:
            output1.write('\n'.join(results))

    except FileNotFoundError:  # Checks is there a file named input.txt
        print(f"ERROR: There is either no such a file namely {input_file} or this program does not have permission to read it!")
        print("Program is going to terminate!")
        sys.exit(1)

def main():  # Calls the necessary functions
    enough_argument_test()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    output_writer(input_file, output_file)

if __name__ == "__main__":
    main()
