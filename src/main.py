import cgsid


def main() -> None:
    action = input("[c]ompress [u]ncompress ? ")
    
    if action == 'c':
        string = input("String: ")
        id = cgsid.compress(string)
        print(f'{id :016X}')
    elif action == 'u':
        id = int(input("ID: "), 16)
        string = cgsid.uncompress(id)
        print(string)


if __name__ == '__main__':
    main()
