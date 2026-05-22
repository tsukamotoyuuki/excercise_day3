
def read_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(type(lines))
        print("read success")
        return lines
    except Exception as ex:
        print(f"fa:{ex}")
        return None


def write_txt(lines, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("wirte success")
    except Exception as ex:
        print(f"fa:{ex}")



def process_lines(lines):
    new_lines = []

    for line in lines:
        line = line.strip()
        print(type(line))
        new_line = int(line) * 2
        new_lines.append(str(new_line) + "\n")

    return new_lines

def process_lines2(lines):
    total = 0

    for line in lines:
        line = line.strip()
        try:
            num = int(line)
            if num % 2 == 0:
                total += num
        except ValueError:
            continue
    return total


def main():
    input_file = "sample11_6_1.txt"
    output_file = "sample11_6_1_doubled.txt"

    lines = read_txt(input_file)
    new_lines2 = process_lines(lines)
    print(new_lines2)
    new_lines = process_lines(lines)

    write_txt(new_lines, output_file)


main()
