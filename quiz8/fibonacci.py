import sys

eager_fibonacci_list = [1, 1]

def eager_fibonacci(number):
    if number <= 0:
        return "nan"
    elif number <= len(eager_fibonacci_list):
        return eager_fibonacci_list[number - 1]
    else:
        for i in range(len(eager_fibonacci_list) + 1, number + 1):
            result = eager_fibonacci(i - 1) + eager_fibonacci(i - 2)
            eager_fibonacci_list.append(result)
        return eager_fibonacci_list[number - 1]

def naive_fibonacci(number):
    if number <= 0:
        return "nan"
    elif number == 1 or number == 2:
        return 1
    else:
        result = naive_fibonacci(number - 1) + naive_fibonacci(number - 2)
        return result

def calculate_eager_fibonacci_sequence(number, calculated=None):
    if number <= 0:
        return [f"ERROR: Fibonacci cannot be calculated for the non-positive numbers!"]

    if calculated is None:
        calculated = {}

    output_lines = []

    if number in calculated:
        output_lines.append(f"fib({number}) = {calculated[number]}")
        return output_lines

    if number <= len(eager_fibonacci_list):
        output_lines.append(f"fib({number}) = {eager_fibonacci(number)}")
        calculated[number] = eager_fibonacci(number)
    else:
        output_lines.append(f"fib({number}) = fib({number - 1}) + fib({number - 2})")

        output_lines.extend(calculate_eager_fibonacci_sequence(number - 1, calculated))
        output_lines.extend(calculate_eager_fibonacci_sequence(number - 2, calculated))

        calculated[number] = calculated[number - 1] + calculated[number - 2]

    return output_lines

def calculate_naive_fibonacci_sequence(number):
    if number <= 0:
        return ["ERROR: Fibonacci cannot be calculated for the non-positive numbers!"]

    output_lines = []

    if number == 1 or number == 2:
        output_lines.append(f"fib({number}) = 1")
    else:
        output_lines.append(f"fib({number}) = fib({number - 1}) + fib({number - 2})")

        output_lines.extend(calculate_naive_fibonacci_sequence(number - 1))
        output_lines.extend(calculate_naive_fibonacci_sequence(number - 2))

    return output_lines

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_naive_file output_eager_file")
        sys.exit(1)

    with open(sys.argv[1], "r") as file:
        input_numbers = [int(line.strip()) for line in file.readlines()]

    with open(sys.argv[2], "w") as output_naive_file, open(sys.argv[3], "w") as output_eager_file:
        for n in input_numbers:
            output_naive_file.write(f"--------------------------------\nCalculating {n}. Fibonacci number:\n")
            output_naive_lines = calculate_naive_fibonacci_sequence(n)
            for line in output_naive_lines:
                output_naive_file.write(line + "\n")

            result_naive = naive_fibonacci(n)
            output_naive_file.write(f"{n}. Fibonacci number is: {result_naive}\n")

            output_eager_file.write(f"{'-' * 32}\nCalculating {n}. Fibonacci number:\n")
            output_eager_lines = calculate_eager_fibonacci_sequence(n)
            for line in output_eager_lines:
                output_eager_file.write(line + "\n")

            result_eager = eager_fibonacci(n)
            output_eager_file.write(f"{n}. Fibonacci number is: {result_eager}\n")

        output_eager_file.write(f"{'-' * 32}\nStructure for the eager solution:\n{eager_fibonacci_list}")
        output_naive_file.write("--------------------------------")
        output_eager_file.write("\n--------------------------------")

if __name__ == "__main__":
    main()
