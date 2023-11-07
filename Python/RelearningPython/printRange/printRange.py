#Prints the even numbers between 2 User defined numbers

# main Fucntion
def main():
    print("### This program will print the even numbers between 2 numbers you give. ###")
    #get lower number
    get_low_prompt = 'Please enter the lower Bound first.'
    get_upper_prompt = "Please enter the upper Bound."
    range_of_numbers = []
    even_numbers = []
    valid_entry = False

    while valid_entry is False:
        lower_number = int(input(get_low_prompt))
        upper_number = int(input(get_upper_prompt))
        valid_entry = greater_then_and_not_equal(lower_number, upper_number)
        if valid_entry is False:
            print("Please Try Again. The lower bound not less then Upper bound.")
        else:
            valid_entry = True

    # Generate range of numbers and find even numbers within the range
    range_of_numbers = range(lower_number, upper_number)
    even_numbers = get_even_numbers(range_of_numbers)
    str_of_even_numbers = write_list_of_numbers(even_numbers)

    # Print the even numbers and the range
    print("The even Numbers bettween" + str(lower_number) + " and " + str(upper_number) + " are:")
    print(str_of_even_numbers)

# Function to check if upper bound is greater than lower bound
def greater_then_and_not_equal (lower_val, upper_val):
    return upper_val > lower_val



# Function to check if a number is even
def is_even(number_to_check):
    return number_to_check % 2 == 0


# Function to get even numbers from a sequence
def get_even_numbers(number_sequence):
    even_numbers = []
    for i in number_sequence:
        if is_even(i):
            even_numbers.append(i)
    return even_numbers

# Function to format a list of numbers as a string
def write_list_of_numbers(list_to_print):
    numbers_to_print = ""
    for i, number in enumerate(list_to_print):
        if i == 0:
            numbers_to_print += str(number)
        else:
            numbers_to_print += ", " + str(number)
    return numbers_to_print

# Call the main function
if __name__ == "__main__":
    main()
