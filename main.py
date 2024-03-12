import re


def less_nums():
    nums = [int(input()) for _ in range(int(input()))]
    nums.sort()
    print(nums[0], nums[1])


def print_line_by_num():
    line_num = int(input("Введите номер строки: "))
    with open("lines.txt") as f:
        lines = f.readlines()
    if len(lines) < line_num or line_num <= 0:
        print("Строки с таким номером нет")
    else:
        print(lines[line_num - 1])


def count_prices():
    with open("prices.txt") as f:
        items = []
        for line in f.readlines():
            line_data = line.split(";")
            items.append(
                (line_data[0], int(line_data[1]), int(line_data[2]))
            )
        print(sum([item[1] * item[2] for item in items]))


def king_move():
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        print("YES")
    else:
        print("NO")


def count_of_words():
    with open("input.txt") as f:
        text = f.read()
    words_count = {}
    for word in re.findall(r"\w+", text):
        if words_count.get(word):
            words_count[word] += 1
        else:
            words_count[word] = 1
    for word, count in words_count.items():
        print(f"{word} — {count}")


def caesars_cipher():
    shift = int(input())
    text = input()
    result = ""
    for char in text:
        if char.isalpha():
            start_code = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start_code + shift) % 26 + start_code)
        else:
            result += char
    print(result)


if __name__ == '__main__':
    print_line_by_num()
    count_prices()
    king_move()
    count_of_words()
    caesars_cipher()
    less_nums()
