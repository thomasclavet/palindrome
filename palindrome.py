import argparse
import string
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(name)s:%(levelname)s: %(message)s", level=logging.INFO)


def is_palindrome(phrase: str) -> bool:
	if isinstance(phrase, int):
		raise TypeError("Word must be a string")

	phrase = phrase.translate(str.maketrans("", "", string.punctuation)).lower().replace(" ", "")
	if phrase == phrase[::-1]:
		return True
	else:
		return False


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Argument Parser for palindrome function")
	parser.add_argument("phrase", help="Phrase to check if it is a palindrome", type=str)
	args = parser.parse_args()

	logger.info(f"{args.phrase} is a palindrome: {is_palindrome(args.phrase)}")
