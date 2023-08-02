from lib.dairy_entry import DiaryEntry
import pytest

def test_contrcuts_gets_title_contents():
    dairy = DiaryEntry("mytitle", 'contents')
    assert dairy.title == 'mytitle'


def test_counts_words_contents():
    dairy = DiaryEntry("mytitle", 'one two three four five')
    assert dairy.count_words() == 5

def test_reading_time():
    dairy = DiaryEntry("mytitle", 'one two three four five')
    assert dairy.reading_time(2) == 3


def test_readable_chunk_first_chunk():
     dairy = DiaryEntry("mytitle", 'one two three four five')
     assert dairy.reading_chunk(2, 1) == "one two"


def test_readable_chunk_second_chunk():
     dairy = DiaryEntry("mytitle", 'one two three four five')
     dairy.reading_chunk(2, 1)
     assert dairy.reading_chunk(2, 1) == "three four"


def test_readable_chunk_third_chunk():
     dairy = DiaryEntry("mytitle", 'one two three four five')
     dairy.reading_chunk(2, 1)
     dairy.reading_chunk(2, 1)
     assert dairy.reading_chunk(2, 1) == 'five'

def test_readable_chunk_fourth_chunk():
     dairy = DiaryEntry("mytitle", 'one two three four five')
     dairy.reading_chunk(2, 1)
     dairy.reading_chunk(2, 1)
     dairy.reading_chunk(2, 1)
     assert dairy.reading_chunk(2, 1) == 'one two'

def test_readable_chunk_fourth_chunk_with_exact_chunk():
     dairy = DiaryEntry("mytitle", 'one two three four five')
     dairy.reading_chunk(2, 1)
     dairy.reading_chunk(2, 1)
     dairy.reading_chunk(2, 1)
     assert dairy.reading_chunk(2, 1) == 'one two'