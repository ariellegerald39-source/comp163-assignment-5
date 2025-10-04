print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

print("    " + "----" * 10)

for row in range(1, 11):
    print(f"{row:2} |", end="")
    for col in range(1, 11):
        product = col * row
        print(f"{product:4}", end="")
    print()








