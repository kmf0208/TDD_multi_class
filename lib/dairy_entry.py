from math import ceil


class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.stop_of_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
          count_word = self.count_words()
          return ceil(count_word / wpm)

    def reading_chunk(self, wpm, minutes):
         words = self.contents.split()
         if self.stop_of_point >= len(words):
              self.stop_of_point = 0


         readable_chunk_length = wpm * minutes
         start_point = self.stop_of_point
         end_point = self.stop_of_point + readable_chunk_length
         readable_chunk =  ' '.join(words[start_point:end_point])
         self.stop_of_point += readable_chunk_length
         return readable_chunk