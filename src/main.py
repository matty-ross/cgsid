import cgsid


def main() -> None:
    action = input("[c]ompress [u]ncompress ? ")
    match action:
        case 'c' | 'C':
            string = input("String: ")
            id = cgsid.compress(string)
            print(f'{id :016X}')
        case 'u' | 'U':
            id = int(input("ID: "), 16)
            string = cgsid.uncompress(id)
            print(string)
        case _:
            print("Unknown option!")


if __name__ == '__main__':
    main()
