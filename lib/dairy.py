from math import ceil

class Diary:
    def __init__(self):
        self._entry = []

    def add(self, entry):
        return self._entry.append(entry)

    def all(self):
        return [x for x in self._entry]

    def count_words(self):
        return sum([x.count_words() for x in self._entry])


    def reading_time(self, wpm):
        if self._entry == []:
            raise Exception("no entries added yet")
        count_word = self.count_words()
        return ceil(count_word / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entry == []:
            raise Exception("no entries added yet")
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_user_can_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for i in self._entry:
            if i.count_words() <= words_user_can_read:
                if i.count_words() >longest_found_so_far:
                    most_readable = i
                    longest_found_so_far = i.count_words()
        return most_readable
        
