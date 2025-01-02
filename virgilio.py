import os
import json


class Virgilio:
    CANTI_RANGE: range = range(1, 34)

    class CantoNotFoundError(
        Exception
    ):
        """
        Exception raised when the number of the Canto is not between 1 and 34.
        """

        def __init__(self):
            super().__init__("canto_number must be between 1 and 34")

    def __init__(self, directory: str):
        """
        Initialize the directory attribute with the provided path.

        -param directory: Absolute path to the directory
        containing the "Canti".
        """
        self.directory = directory

    def read_canto_lines(self,
                         canto_number: int,
                         strip_lines: bool = False,
                         num_lines: int | None = None) -> list[str] | str:
        """
        Reads the lines of a Canto specified by number.

        -param canto_number: Number of the Canto to read (1-34).
        -param strip_lines: If True, removes spaces and newlines from lines.
        -param num_lines: Number of lines to read (None to read all).
        -return: List of lines of the Canto.
        -raises TypeError: If canto_number is not an integer.
        -raises CantoNotFoundError:
        If the number of the Canto is not between 1 and 34.
        """
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")

        if not (1 <= canto_number <= 34):
            raise self.CantoNotFoundError()

        file_path: str = os.path.join(
            self.directory, f"Canto_{canto_number}.txt")

        try:
            # method to open the file
            with open(file_path, "r", encoding="utf-8") as file:
                # method to read all lines of the file
                lines: list[str] = file.readlines()
                if strip_lines:
                    # method to remove spaces and newlines (strip)
                    stripped_lines = []
                    for line in lines:
                        stripped_lines.append(line.strip())
                    lines = stripped_lines
                if num_lines is not None:
                    lines = lines[:num_lines]
                return lines
        except Exception:
            return f"error while opening {file_path}"

    def count_verses(self, canto_number: int) -> int:
        """
        Counts the number of verses (lines) of a specified Canto.

        -param canto_number: Number of the Canto to analyze (1-34).
        -return: Number of verses of the Canto.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        return len(lines)

    def count_tercets(self, canto_number: int) -> int:
        """
        Counts the number of tercets in a specified Canto.

        -param canto_number: Number of the Canto to analyze (1-34).
        -return: Number of tercets in the Canto.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        return len(lines) // 3  # integer division

    def count_word(self, canto_number: int, word: str) -> int:
        """
        Counts the number of occurrences of a specific word in a Canto.

        -param canto_number: Canto number to analyze (1-34).
        -param word: Word to search for.
        -return: Number of occurrences of the word in the Canto.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        content: str = ''.join(lines)
        # method to count the number of occurrences
        return content.count(word)

    def get_verse_with_word(self, canto_number: int, word: str) -> str | None:
        """
        Returns the first line of the specified Canto
        that contains the given word.

        -param canto_number: Number of the Canto to analyze (1-34).
        -param word: Word to search for.
        -return: First line containing the word or None if not found.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        for line in lines:
            # method to check if the word is in the line
            if word in line:
                return line
        return None

    def get_verses_with_word(self, canto_number: int, word: str) -> list[str]:
        """
        Returns all verses of the specified Canto that contain the given word.

        -param canto_number: Number of the Canto to analyze (1-34).
        -param word: Word to search for.
        -return: List of verses containing the word or empty list if not found.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        filtered_lines = []
        for line in lines:
            if word in line:
                filtered_lines.append(line)
        return filtered_lines

    def get_longest_verse(self, canto_number: int) -> str | None:
        """
        Returns the longest line of the specified Canto.

        -param canto_number: Number of the Canto to analyze (1-34).
        -return: Longest line of the Canto.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        # method to find the longest item
        return max(lines, key=len, default=None)

    def get_longest_canto(self) -> dict[str, int]:
        """
        Returns the Canto with the most lines.

        -return: Dictionary with Canto number and maximum length.
        """
        max_length: int = 0
        longest_canto: int | None = None
        for canto_number in self.CANTI_RANGE:
            length = self.count_verses(canto_number)
            if length > max_length:
                max_length = length
                longest_canto = canto_number
        return {"canto_number": longest_canto, "canto_len": max_length}

    def count_words(self,
                    canto_number: int,
                    words: list[str]) -> dict[str, int]:
        """
        Counts occurrences of a list of words in a specified Canto.

        -param canto_number: Number of the Canto to analyze (1-34).
        -param words: List of words to search for.
        -return: Dictionary with words as keys and occurrences as values.
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        word_counts: dict[str, int] = {}
        content: str = ''.join(lines)
        for word in words:
            word_counts[word] = content.count(word)
        with open(
            os.path.join(self.directory, "word_counts.json"),
            "w",
            encoding="utf-8"
        ) as file:
            # method to write a dictionary in a file
            json.dump(word_counts, file)
        return word_counts

    def get_hell_verses(self) -> list[str]:
        """
        Returns all the verses of Inferno in order.

        -return: List of all the verses of Inferno.
        """
        all_verses: list[str] = []
        for canto_number in self.CANTI_RANGE:
            lines = self.read_canto_lines(canto_number)
            # method to append a list to another list
            all_verses.extend(lines)
        return all_verses

    def count_hell_verses(self) -> int:
        """
        Count the total number of lines in Hell.

        -return: Total number of lines.
        """
        all_verses: list[str] = self.get_hell_verses()
        return len(all_verses)

    def get_hell_verse_mean_len(self) -> float:
        """
        Calculate the average length of the lines of Inferno.

        -return: Average length of lines.
        """
        all_verses: list[str] = self.get_hell_verses()
        total_length: int = 0
        for verse in all_verses:
            total_length += len(verse.strip())
        average_length: float = total_length / \
            len(all_verses) if all_verses else 0
        # method to round to 2 decimal places
        return round(average_length, 2)
