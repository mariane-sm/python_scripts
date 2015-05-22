def find_look_and_say(n):
    counter = 1
    sequence = ['1', '11']
    while counter <= n:
        if counter == n:
            return sequence
        sequence.append(next_look_and_say_number(sequence[counter]))
        counter += 1

def next_look_and_say_number(look_and_say_number):
    result = ''
    same_digit_count = 1
    previous_digit = look_and_say_number[0]
    for index, digit in enumerate(look_and_say_number[1:]):
        if previous_digit == digit:
            same_digit_count += 1
            if index + 1 == len(look_and_say_number) - 1:
                result += str(same_digit_count) + previous_digit
        else:
            result += str(same_digit_count) + previous_digit
            same_digit_count = 1
            if index + 1 == len(look_and_say_number) - 1:
                result += '1' + digit
            previous_digit = digit
    return result

print find_look_and_say(7)
