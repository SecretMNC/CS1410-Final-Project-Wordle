from unittest import TestCase
from unittest.mock import patch, mock_open
from random_word import WordPicker


class TestRandomWords(TestCase):

    def test_get_word_and_difficulty(self):
        # Tests if the getter function returns what's expected
        pick_word = WordPicker()
        pick_word._random_word = 'APPLE'
        pick_word._word_diff = '1'
        word, diff = pick_word.get_word_and_difficulty()
        self.assertEqual(word, 'APPLE')
        self.assertEqual(diff, '1')
    
    def test_output_type(self):
        # Tests if the word is a string and difficulty is a digit
        pick_word = WordPicker()
        word, diff = pick_word.get_word_and_difficulty()
        self.assertIs(type(word), str)
        self.assertTrue(diff.isdigit())

    def test_word_length(self):
        # Tests that the length of the word is 5 characters (random)
        pick_word = WordPicker()
        word, _ = pick_word.get_word_and_difficulty()
        self.assertEqual(len(word), 5, "Word should be 5 letters long")

    def test_word_uppercase(self):
        # Tests if the returned word is uppercase (random)
        pick_word = WordPicker()
        word, _ = pick_word.get_word_and_difficulty()
        self.assertTrue(word.isupper(), "Word should be in uppercase")

    @patch('builtins.open', new_callable=mock_open, read_data="APPLE1\nBANANA2\nCRY3\n")
    def test_read_word_list(self, mock_file):
        # Tests if reading a text file with words with wrong lengths is ignored
        pick_word = WordPicker()
        pick_word.read_word_list()
        self.assertEqual(len(pick_word._word_dict), 2)
        self.assertIn('APPLE', pick_word._word_dict)
        self.assertEqual(pick_word._word_dict['APPLE'], '1')

    @patch('builtins.open', new_callable=mock_open, read_data="AP PLE1\nBANANA2\nCHERRY3\n")
    def test_invalid_word_format(self, mock_file):
        # Tests if incorrect formatting is correctly ignored
        pick_word = WordPicker()
        pick_word.read_word_list()
        self.assertEqual(len(pick_word._word_dict), 2)
        self.assertNotIn('AP PLE', pick_word._word_dict)

    @patch('builtins.input', return_value='1')
    def test_prompt_fix_file(self, mock_input):
        # Tests if user prompt works as intended
        pick_word = WordPicker()
        result = pick_word.prompt_fix_file()
        self.assertTrue(result)

    @patch('builtins.input', return_value='2')
    def test_prompt_fix_file_no(self, mock_input):
        # Tests if user prompt cancels properly
        pick_word = WordPicker()
        result = pick_word.prompt_fix_file()
        self.assertFalse(result)
