## There are several aspects to consider when arrange members into a song
## 1. A person must be a leader of the song
## 2. Song of low preference must be prioritized to be arranged first
## 3. Members of lower preference and lower score should be prioritized

## Before we determine the arrangement, we must make sure that there are
## enough members to participate in all the songs
## This function return the difference between required and participate
## numbers and True if satisfied, and the difference and False if not
## satisfied
def check_quantity(Songs,Members):
    total_want = 0
    total_req = 0
    for member in Members:
        total_want+=member.number_of_songs
    for song in Songs:
        total_req +=song.numbers_of_members[0]
    if diff>=0:
        return diff,True
    return diff,False

## This function return the list of songs according to their popularity from
## the most to the least popular
def song_popularity(Songs, Members):
    max = len(Songs)
    for index,song in enumerate(Songs):
        for member in Members:
            song.popularity += max-Members.list_of_preference[index]

## This function based on the difference between the participate and required
## number and the song popularity to decide which song should be increased in
## number of members
def double_member_in_song(diff, Songs):
    # arrange songs according to their popularity
    song_rank = {}
    for song in Songs:
        song_rank[song] = song.popularity
    new_song_rank = sorted(mydict.items(), key=lambda item: item[1]):
    for song, value in new_song_rank.items():
        if diff>=song.numbers_of_possible_members:
            song.num_member(song.numbers_of_possible_members*2)
            diff = diff - song.numbers_of_possible_members
