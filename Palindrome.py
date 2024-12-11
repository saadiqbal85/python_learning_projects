original_number = int(input("Enter a positive integer: "))
temp_number = original_number
reversed_number = 0

while temp_number > 0:
    last_digit = temp_number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + last_digit  # Append last digit to reversed number
    temp_number = temp_number // 10  # Remove the last digit

if reversed_number == original_number:
    print(f"The number {original_number} is a palindrome integer.")
else:
    print(f"The number {original_number} is not a palindrome integer.")
