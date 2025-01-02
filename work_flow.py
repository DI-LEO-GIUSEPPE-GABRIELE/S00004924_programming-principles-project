from virgilio import Virgilio

# Variables
DIRECTORY_PATH: str = "./assets/canti"
canto_to_read: int = 1
word_to_count: str = "selva"
words_to_count: list[str] = ["selva", 'inferno', 'vita']

# Class instance
virgilio = Virgilio(DIRECTORY_PATH)

# Tests Work Flow
try:
    # Exercise 1 - Read lines from a selected Canto.
    canto_lines = virgilio.read_canto_lines(canto_to_read)
    print(f"Lines of Canto {canto_to_read}:")
    for line in canto_lines:
        print(f"{line}")

    # Exercise 2 - Count verses in a selected Canto.
    verse_count = virgilio.count_verses(canto_to_read)
    print(f"Number of verses in Canto {canto_to_read}: {verse_count}")

    # Exercise 3 - Count tercets in a selected Canto.
    tercets_count = virgilio.count_tercets(canto_to_read)
    print(f"Number of tercets in Canto {canto_to_read}: {tercets_count}")

    # Exercise 4 - Count selected word in a selected Canto.
    word_count = virgilio.count_word(canto_to_read, word_to_count)
    print(
        f"Occurrences of the word '{word_to_count}' "
        f"in Canto {canto_to_read}: {word_count}"
    )

    # Exercise 5 - Find the first verse of the selected Canto
    # that contains the selected word.
    found_verse = virgilio.get_verse_with_word(canto_to_read, word_to_count)
    print(
        f"First verse containing '{word_to_count}' "
        f"of Canto {canto_to_read}: \n{found_verse}")

    # Exercise 6 - Find all verses of the selected Canto
    # that contain the selected word.
    found_verses = virgilio.get_verses_with_word(canto_to_read, word_to_count)
    print(
        f"All verses containing '{word_to_count}' of Canto {canto_to_read}:"
    )
    for line in found_verses:
        print(f"{line}")

    # Exercise 7 - Find the longest verse of the selected Canto.
    longest_verse = virgilio.get_longest_verse(canto_to_read)
    print(f"Longest verse of Canto 1:\n{longest_verse}")

    # Exercise 8 - Find the longest Canto of the Hell.
    print(f"Longest Canto of the Hell:\n{virgilio.get_longest_canto()}")

    # Exercise 9 - Find all verses of the selected Canto
    # that contain the selected words.
    found_verses = virgilio.count_words(canto_to_read, words_to_count)
    print(
        f"Verses containing {', '.join(words_to_count)} of Canto {
            canto_to_read}:\n"
        f"{found_verses}"
    )

    # Exercise 10 - Return a list with all the verses of all the Hell.
    found_verses = virgilio.get_hell_verses()
    print("All verses of the Inferno:")
    for verse in found_verses:
        print(f"{verse.strip()}")

    # Exercise 11 - Return number of verses of the Hell.
    print(
        f"Number of verses of the Inferno: {virgilio.count_hell_verses()}")

    # Exercise 12 - Return the mean verse length of the Hell.
    print(
        f"Mean verse length of the Inferno: "
        f"{virgilio.get_hell_verse_mean_len()}"
    )

    # Exercise 13 - new strip_lines param in read_canto_lines.
    canto_lines = virgilio.read_canto_lines(canto_to_read, strip_lines=True)
    print(
        f"Lines of Canto {
            canto_to_read} with spaces and line breaks removed:\n"
    )
    for line in canto_lines:
        print(f"{line}")

    # Exercise 14 - new num_lines param in read_canto_lines.
    canto_lines = virgilio.read_canto_lines(
        canto_to_read, strip_lines=True, num_lines=10)
    print(
        f"Lines of Canto {
            canto_to_read} with spaces and line breaks removed and limit:\n"
    )
    for line in canto_lines:
        print(f"{line}")

except Exception as e:
    print(f"Error during execution: {e}")
