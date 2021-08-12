# https://www.codewars.com/kata/551dc350bf4e526099000ae5

def song_decoder(song):

    nowub = song.replace('WUB', ' ').strip()
    nodubspace = " ".join(nowub.split())
    print(nodubspace)
    return nodubspace









song_decoder("AWUBBWUBC")#, "A B C","WUB should be replaced by 1 space")
song_decoder("AWUBWUBWUBBWUBWUBWUBC")#, "A B C","multiples WUB should be replaced by only 1 space")
song_decoder("WUBAWUBBWUBCWUB")#, "A B C","heading or trailing spaces should be removed")