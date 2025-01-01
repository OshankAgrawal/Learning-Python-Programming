def count_characters(string):
    return len(string)

def display_within_limit(string, limit):
    if len(string) <= limit:
        print("String within character limit:")
        print(string)
    else:
        print("String exceeds character limit. Truncated to {} characters:".format(limit))
        print(string[:limit])

def main():
    user_string = input("Enter the string: ")
    character_limit = int(input("Enter the character limit: "))

    total_characters = count_characters(user_string)
    print("Total characters in the string:", total_characters)

    display_within_limit(user_string, character_limit)

if __name__ == "__main__":
    main()
