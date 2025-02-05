# DAY-1
# Given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list for even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)

# second question
# Given list
numbers = [1, 2, 3, 4, 5]

# Calculate sums
even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = sum(num for num in numbers if num % 2 != 0)

print(f"Even Sum: {even_sum}, Odd Sum: {odd_sum}")

# third questions
# Given list of words
words = ["abcd", "efghi", "ghifh", "dskf", "sdddfsdf"]

# Extract first letter of each word and join them
result = "".join(word[0] for word in words)

print("Output:", result)

# fourth question
str = 'python'
rev=''
for i in range(0, len(str)):
    rev = str[i] + rev
print("Reverse String : ", rev)

# DAY-2
# first question

# Initialize counter
i = 1

# Loop from 1 to 100
while i <= 100:
    print(i, end=" ")
    i += 1

    # second question

# Using for loop
for num in range(100, 0, -1):
    print(num, end=" ")

# Initialize counter
num = 100

# Loop from 100 to 1
while num >= 1:
    print(num, end=" ")
    num -= 1

   #third question

# Function to reverse a number
def reverse(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10  # Extract last digit
        reversed = reversed * 10 + digit  # Append digit to reversed number
        n = n // 10  # Remove last digit
    return reversed
print("Reversed Number:", reverse (num))
