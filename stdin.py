with (open(input(), 'r', encoding='utf-8') as file_in,
      open(input(), 'w', encoding='utf-8') as file_even,
      open(input(), 'w', encoding='utf-8') as file_odd,
      open(input(), 'w', encoding='utf-8') as file_eq):
    numbers = file_in.readline().split()
    for number in numbers:
        count = 0
        for ch in number:
            count += 1 if int(ch) > 0 else -1
        if count > 0:
            file_even.write(number)
            