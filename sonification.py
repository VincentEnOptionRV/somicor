import music21 as mus

def generate_pitch_list():
    """Generate the list of frequencies corresponding to notes C1 to B8 in ascending order of frequency and the list of the corresponding pitch names."""
    letters = ['c','d','e','f','g','a','b']
    pitchFreqList = [mus.pitch.Pitch(l + str(n)).frequency for l in letters for n in range(1,9)]
    pitchNameList = [l + str(n) for l in letters for n in range(1,9)]
    return (pitchFreqList,pitchNameList)


def _asign_note(freq, pitchFreqList, pitchNameList):
    """Find the closest musical note to the given frequency."""
    closestFreqIndex = pitchFreqList.index(min(pitchFreqList, key = lambda x: abs(x - freq)))
    return pitchNameList[closestFreqIndex]

def asign_note(freq):
    """Kind of curryfies *_asign_note*."""
    return _asign_note(freq, *generate_pitch_list())

def freqList_to_note_list(freqList):
    """Assigns a list of notes to a list of frequencies. The notes are the ones closest to each frequency."""
    return list(map(asign_note, freqList))

def freq_list_to_tinyNotation(freqList):
    """
    Convert a list of frequencies into a string representing the melody based on these frequencies in tinyNotation format.
    The frequencies are first sorted by ascending order, so the resulting melody is also in ascending pitch.
    """
    freqList.sort()
    noteList = freqList_to_note_list(freqList)
    lowestNote = noteList[0]
    tinyNotation = "tinyNotation: 4/4"
    for note in noteList:
        nbOfOctavesUp = int(note[1]) - int(lowestNote[1])
        tinyNotation += " " + note[0] + "'" * nbOfOctavesUp + "4"
    return tinyNotation

def sonification(freqList):
    """Performs the sonification : convert a list of frequencies into a music21 Stream."""
    return mus.converter.parse(freq_list_to_tinyNotation(freqList))
