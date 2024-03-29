import random
def generate_large_random_numbers(filename, num_count):
    with open(filename, 'w') as file:
        # Write the number count in the first line
        file.write(str(num_count) + '\n')
        # Write the random numbers in the second line, space-separated
        for _ in range(num_count):
            random_number = random.randint(1,9)
            file.write(str(random_number) + ' ')
        print("\n")
# Example usage: generate 10^8 random numbers and write to "large_random_numbers.txt"
generate_large_random_numbers("testcase13.txt", (10**5)*5+(10**4)*3)