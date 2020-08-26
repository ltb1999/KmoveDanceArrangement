## This code is constructed to arrange members into dance songs in a specific
## event with specific songs selected. Members are asked to fill out a Google
## survey

## Class Member stores the name and important information about the members
## such as how many song they want to perform and rank the songs in order
## of preference. This class also contains the information about the members
## such as they are new members or they can lead the song
## attributes: name (string), number_of_songs (int), list_of_preference
## (list of int), lead_ability (list of numbers), new_member, song_in
## (list of string), leader_of_song (list of string)
class Member:
    def __init__(self,name,number_of_songs,list_of_preference,lead_ability,new_member):
        self.__name__ = name
        self.__number_of_songs__ = number_of_songs
        self.__list_of_preference__ = list_of_preference
        self.__lead_ability__ = lead_ability
        self.__new_member__ = new_member
        self.song_in = []
        self.leader_of_song = []
    def add_song(self,theSong):
        self.song_in.append(theSong.name)
    def add_leader(self,theSong):
        self.leader_of_song.append(theSong.name)

## Class Song stores information about the songs selected in the event, such as
## name (string), numbers_of_possible_members (list of int), leader (string),
## number_of_official_member =
class Song:
    def __init__(self,name,numbers_of_members):
        self.__name__ = name
        self.numbers_of_possible_members = numbers_of_possible_members
        self.number_of_official_member = 0
    def add_leader(member):
        self.__leader__ = member.name
    def add_member():
        self.number_of_official_member += 1
