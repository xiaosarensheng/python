
def get_apr_name():
    with open('apr应用名单.txt', 'r', encoding='utf-8') as file_one:
        list_one = file_one.readlines()
        for line in list_one:
            yield line

def main():
    file_two = open('android排名.txt', 'r', encoding='utf-8')
    list_two= file_two.readlines()
    for line in list_two:
        for i in get_apr_name():
            i=i.strip()
            if line.find(i) != -1:
                with open('比较.txt', 'a', encoding='utf-8') as file_three:
                    file_three.write(line)


if __name__ == '__main__':
    main()