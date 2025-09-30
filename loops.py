# loops_examples.py

# Example 1: For loop - print numbers from 1 to 5
print("For loop example:")
for i in range(1, 6):
    print(i)

# Example 2: While loop - print numbers from 1 to 5
print("\nWhile loop example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Example 3: For loop with list
print("\nIterating through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 4: Nested loop - multiplication table (1 to 3)
print("\nNested loop example (Multiplication Table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-----")

# Example 5: Loop with break statement
print("\nBreak statement example:")
for num in range(1, 10):
    if num == 5:
        print("Loop stopped at:", num)
        break
    print(num)

# Example 6: Loop with continue statement
print("\nContinue statement example:")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
