def is_array_in_sorted_order(arr):
    if len(arr) <= 1:
        return True
    return arr[0] <= arr[1] and is_array_in_sorted_order(arr[1:])

A = [124, 123, 125]  # Corrected array
A2 = [127, 220, 225, 230, 235, 240, 245]

print(is_array_in_sorted_order(A))  # Output: False
print(is_array_in_sorted_order(A2))  # Output: True
print("EOF")
