import sys
from stats import get_num_words, get_chars_dict, sorted_chars_list


def main():
    # Verify the user provided a file path argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Grab path from CLI arguments
    path_to_file = sys.argv[1]

    try:
        with open(path_to_file) as f:
            file_contents = f.read()

            # Word Count
            total_words = get_num_words(file_contents)

            # Character Analytics
            chars_dict = get_chars_dict(file_contents)
            sorted_list = sorted_chars_list(chars_dict)

            # Print the Report
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {path_to_file}...")
            print("----------- Word Count ----------")
            print(f"Found {total_words} total words")
            print("--------- Character Count -------")
            print("---------Fedora------------------")

            for item in sorted_list:
                print(f"{item['char']}: {item['num']}")

            print("============= END ===============")

    except FileNotFoundError:
        print(f"Error: The file at {path_to_file} was not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
