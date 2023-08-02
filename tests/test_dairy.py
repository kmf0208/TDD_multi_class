from lib.dairy import Diary
import pytest


def test_for_empty_list():
    diary = Diary()
    assert diary.all() == []


def test_word_count_0():
    diary = Diary()
    assert diary.count_words() == 0



def test_reading_time_raises_error():
    dairy = Diary()
    with pytest.raises(Exception) as e:
        dairy.reading_time(2)
    assert str(e.value) == "no entries added yet"

def test_finding_the_best_reading_time_raises_error():
    dairy = Diary()
    with pytest.raises(Exception) as e:
        dairy.find_best_entry_for_reading_time(2, 2)
    assert str(e.value) == "no entries added yet"