import sys


def is_sorted(list):#Checks the given numbers are sorted
    if all(list[x] <= list[x + 1] for x in range(len(list) - 1)):

        return True
def bubble_sort(list_1, output_bubble):
    n = len(list_1)
    for num_pass in range(1, n):
        for i in range(0, n - num_pass):

            if list_1[i] > list_1[i + 1]:  # Swap elements which are in the wrong order
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]

        output_bubble.write("Pass {}: {}".format(num_pass, ' '.join(map(str, list_1))))# Write the current step of the list to the output_bubble.txt

        if all(list_1[i + 1] >= list_1[i] for i in range(n - 1)): #Checks the list and exit the loop if it is completely sorted
            break
        else:
            output_bubble.write("\n")
    return list_1


def insertion_sort(list, output_insertion):
    n = len(list)

    for i in range(1, n):
        current_value = list[i]
        j = i - 1

        # Shifts elements greater than the current value to the right
        while j >= 0 and current_value < list[j]:
            list[j + 1] = list[j]
            j = j-1


        list[j + 1] = current_value

        # Write the current step of the list to the output_insertion
        output_insertion.write("Pass {}: {}".format(i, ' '.join(map(str, list))))

        # Check if the list is completely sorted, and exit the loop if so
        if all(list[j] <= list[j + 1] for j in range(n - 1)):
            break
        else:
            output_insertion.write("\n")

    return list


def main():
    input_filename = sys.argv[1]
    input_list = []

    with open(input_filename, 'r') as input_file:#Reads string from input.txt and convert them into integers than extend the list
        for line in input_file:
            input_list.extend(map(int, line.strip().split()))
    # Gets output filenames from command line
    output_bubble = sys.argv[2]
    output_insertion = sys.argv[3]
    if len(input_list) <= 1 or is_sorted(input_list): #Checks if the list is already sorted or has only one/none element
        with open(output_bubble, 'w') as output_file_1, open(output_insertion, 'w') as output_file_2:
            output_file_1.write("Already sorted!")
            output_file_2.write("Already sorted!")
    else:# Applies bubble sort and insertion sort to the copied lists and write to output files
        with open(output_bubble, 'w') as output_file_1:
            bubble_sort(input_list.copy(), output_file_1)

        with open(output_insertion, 'w') as output_file_2:
            insertion_sort(input_list.copy(), output_file_2)


if __name__ == "__main__":
    main()
