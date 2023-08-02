from lib.dairy import Diary
from lib.dairy_entry import DiaryEntry

def test_adds_to_list_of_diarys():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'my content 1')
    entry2 = DiaryEntry('my title 2', 'my content 2')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


def test_count_words_return_number_of_word_in_diary():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two')
    entry2 = DiaryEntry('my title 2', 'three four five')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5


def test_reading_time_return_time():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two')
    entry2 = DiaryEntry('my title 2', 'three four five')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 3


def test_find_the_best_entry_for_reading_time_returns_entry_that_fits_time():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two three')
    entry2 = DiaryEntry('my title 2', 'one two three four five six seven')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1


def test_find_the_best_entry_for_reading_time_returns_single_entry():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two three')
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1



def test_find_the_best_entry_for_reading_time_returns_nothing():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two three four five six seven')
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None


def test_find_the_best_reading_time_return_the_longest_readale():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two three')
    entry2 = DiaryEntry('my title 2', 'one two three four five six seven')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry2
