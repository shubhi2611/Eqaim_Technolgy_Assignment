def count_valid_numbers():
    count = 0
    for i in range(10, 100):
        digits = [int(d) for d in str(i)]
        if sorted(digits) == digits:
            count += 1
    for i in range(100, 1000):
        digits = [int(d) for d in str(i)]
        if sorted(digits) == digits:
            count += 1
    return count

valid_count = count_valid_numbers()
print(valid_count)