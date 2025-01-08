import os
import json


class Virgilio:
    CANTI_RANGE: range = range(1, 34)

    class CantoNotFoundError(
        Exception
    ):
        """
        Exception raised if the number of the Canto is not between 1 and 34.
        """

        def __init__(self):
            super().__init__("canto_number must be between 1 and 34")

    def __init__(self, directory: str):
        """
        Initialize the directory attribute with the provided path.

        The attributes are:
        ***
        directory: Absolute path to the directory containing the "Canti".
        ***
        """
        self.directory = directory

    def read_canto_lines(self,
                         canto_number: int,
                         strip_lines: bool = False,
                         num_lines: int | None = None) -> list[str] | str:
        """
        This method returns a list of lines of a Canto specified by number,
        optionally removing spaces and newlines
        and limiting the number of lines.

        The parameters are:
        ***
        canto_number: Number of the Canto to read (1-34).
        strip_lines: If True, removes spaces and newlines from lines.
        num_lines: Number of lines to read (None to read all).
        ***

        The exceptions are:
        ***
        TypeError: If canto_number is not an integer.
        CantoNotFoundError:
        If the number of the Canto is not between 1 and 34.
        ***
        """
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")

        if not (1 <= canto_number <= 34):
            raise self.CantoNotFoundError()

        # method to build the file path
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
                        # methods to append a list to another list
                        # and to remove spaces and newlines
                        stripped_lines.append(line.strip())
                    lines = stripped_lines
                if num_lines is not None:
                    # method to limit the number of lines
                    lines = lines[:num_lines]
                return lines

        # method to handle exceptions
        except Exception:
            return f"error while opening {file_path}"

    def count_verses(self, canto_number: int) -> int:
        """
        This method returns the number of verses (lines) of a specified Canto.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        ***
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        # method to count the number of lines
        return len(lines)

    def count_tercets(self, canto_number: int) -> int:
        """
        This method returns the number of tercets in a specified Canto.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        ***
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        return len(lines) // 3  # integer division

    def count_word(self, canto_number: int, word: str) -> int:
        """
        This method returns the number of occurrences
        of a specific word in a Canto.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        word: Word to search for.
        ***
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        # join the lines into a single string
        content: str = ''.join(lines)
        # method to count the number of occurrences
        return content.count(word)

    def get_verse_with_word(self, canto_number: int, word: str) -> str | None:
        """
        This method returns the first line of the specified Canto
        that contains the given word or None if not found.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        word: Word to search for.
        ***
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        for line in lines:
            # method to check if the word is in the line
            if word in line:
                return line
        return None

    def get_verses_with_word(self, canto_number: int, word: str) -> list[str]:
        """
        This method returns all verses of the specified Canto
        that contain the given word or empty list if not found.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        word: Word to search for.
        ***
        """
        lines: list[str] = self.read_canto_lines(canto_number)
        filtered_lines = []
        for line in lines:
            if word in line:
                # method to append a list to another list
                filtered_lines.append(line)
        return filtered_lines

    def get_longest_verse(self, canto_number: int) -> str | None:
        """
        This method returns the longest line of the specified Canto.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        ***
        """
        # Recalling the read_canto_lines method
        lines: list[str] = self.read_canto_lines(canto_number)
        # method to find the longest item
        return max(lines, key=len, default=None)

    def get_longest_canto(self) -> dict[str, int]:
        """
        This method returns the Canto with the most lines.
        """
        max_length: int = 0
        longest_canto: int | None = None
        for canto_number in self.CANTI_RANGE:
            # Recalling the count_verses method
            length = self.count_verses(canto_number)
            if length > max_length:
                max_length = length
                longest_canto = canto_number
            else:
                continue
        return {"canto_number": longest_canto, "canto_len": max_length}

    def count_words(self,
                    canto_number: int,
                    words: list[str]) -> dict[str, int]:
        """
        This method Counts occurrences of a list of words in a specified Canto
        and saves them in a JSON file in the directory of assets.

        The parameters are:
        ***
        canto_number: Number of the Canto to analyze (1-34).
        words: List of words to search for.
        ***
        """
        # Recalling the read_canto_lines method
        lines: list[str] = self.read_canto_lines(canto_number)
        # Initialize an empty dictionary
        word_counts: dict[str, int] = {}
        content: str = ''.join(lines)
        for word in words:
            # method to count the number of occurrences
            word_counts[word] = content.count(word)
        # method to open a file
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
        This method returns a list of all the verses of "Inferno" in order.
        """
        all_verses: list[str] = []
        for canto_number in self.CANTI_RANGE:
            # Recalling the read_canto_lines method
            lines = self.read_canto_lines(canto_number)
            # method to append a list to another list
            all_verses.extend(lines)
        return all_verses

    def count_hell_verses(self) -> int:
        """
        This method returns the total number of lines in "Inferno".
        """
        # Recalling the get_hell_verses method
        all_verses: list[str] = self.get_hell_verses()
        # method to count the number of lines
        return len(all_verses)

    def get_hell_verse_mean_len(self) -> float:
        """
        This method returns the average length of the lines of "Inferno".
        """
        # Recalling the get_hell_verses method
        all_verses: list[str] = self.get_hell_verses()
        total_length: int = 0
        for verse in all_verses:
            # method to concatenate strings
            total_length += len(verse.strip())
            # the backslash is used to escape the newline character
        average_length: float = total_length / \
            len(all_verses) if all_verses else 0
        # method to round to 2 decimal places
        return round(average_length, 2)
