def main():
    with open('day1.txt', 'r') as f:
        data = sorted((sum(map(int, entry.split('\n'))) for entry in f.read().split('\n\n')))
    print(f'Part 1: {data[-1]}')
    print(f'Part 2: {sum(data[-3::])}')


if __name__ == "__main__":
    main()
