def dynamic_analysis(data):

    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    max_number = max(numbers) if numbers else None

    strings = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(strings, key=len) if strings else None

    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    largest_tuple = max(tuples, key=len) if tuples else None

    string_lengths = list(map(len, strings))
    tuple_lengths = list(map(len, tuples))
    return max_number, longest_string, largest_tuple, string_lengths, tuple_lengths


data = [42, "hello", (1, 2, 3), "world", 3.14, [1, 2], ("a", "b", "c")]
max_number, longest_string, largest_tuple, string_lengths, tuple_lengths = dynamic_analysis(data)

print(f"Największa liczba: {max_number}")
print(f"Najdłuższy napis: {longest_string}")
print(f"Największa krotka: {largest_tuple}")
print(f"Długości napisów: {string_lengths}")
print(f"Długości krotek: {tuple_lengths}")
