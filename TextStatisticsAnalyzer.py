import re
from collections import Counter


class TextAnalyzer:
    def __init__(self):
        self.text = ""

    def load_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.text = file.read()
            print("\nFile loaded successfully!")
        except FileNotFoundError:
            print("\nError: File not found.")
        except Exception as e:
            print(f"\nUnexpected Error: {e}")

    def character_count(self):
        return len(self.text)

    def word_count(self):
        words = self.get_words()
        return len(words)

    def sentence_count(self):
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])

    def paragraph_count(self):
        paragraphs = self.text.split("\n\n")
        return len([p for p in paragraphs if p.strip()])

    def unique_word_count(self):
        words = self.get_words()
        return len(set(words))

    def get_words(self):
        return re.findall(r'\b\w+\b', self.text.lower())

    def top_words(self, n=10):
        words = self.get_words()
        counter = Counter(words)
        return counter.most_common(n)

    def search_word(self, word):
        words = self.get_words()
        return words.count(word.lower())

    def save_report(self):
        try:
            with open("report.txt", "w", encoding="utf-8") as file:
                file.write("TEXT ANALYSIS REPORT\n")
                file.write("=" * 30 + "\n")
                file.write(f"Characters: {self.character_count()}\n")
                file.write(f"Words: {self.word_count()}\n")
                file.write(f"Sentences: {self.sentence_count()}\n")
                file.write(f"Paragraphs: {self.paragraph_count()}\n")
                file.write(f"Unique Words: {self.unique_word_count()}\n\n")

                file.write("Top 10 Words:\n")
                for word, count in self.top_words():
                    file.write(f"{word}: {count}\n")

            print("\nReport saved as report.txt")

        except Exception as e:
            print("Error saving report:", e)


def display_menu():
    print("\n")
    print("=" * 40)
    print("TEXT STATISTICS ANALYZER v1.0")
    print("Learn Depth Internship Project")
    print("=" * 40)
    print("1. Load Text File")
    print("2. Show Statistics")
    print("3. Search Word")
    print("4. Save Report")
    print("5. Exit")


def main():
    analyzer = TextAnalyzer()

    while True:
        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter filename: ")
            analyzer.load_file(filename)

        elif choice == "2":
            if not analyzer.text:
                print("Load a file first.")
                continue

            print("\nStatistics")
            print("-" * 25)
            print("Characters:", analyzer.character_count())
            print("Words:", analyzer.word_count())
            print("Sentences:", analyzer.sentence_count())
            print("Paragraphs:", analyzer.paragraph_count())
            print("Unique Words:", analyzer.unique_word_count())

            print("\nTop 10 Words")
            for word, count in analyzer.top_words():
                print(word, ":", count)

        elif choice == "3":
            if not analyzer.text:
                print("Load a file first.")
                continue

            word = input("Enter word to search: ")
            count = analyzer.search_word(word)

            print(f"'{word}' appears {count} times.")

        elif choice == "4":
            if not analyzer.text:
                print("Load a file first.")
                continue

            analyzer.save_report()

        elif choice == "5":
            print("Thank you.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()