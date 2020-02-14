# music notes

from enum import IntEnum

SHARP = '♯' # U+266F
FLAT = '♭' # U+266D

SHARP_NOTES = ('C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B')
FLAT_NOTES  = ('C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B')
CHROMATIC_NOTE_COUNT = len(SHARP_NOTES)

class Interval(IntEnum):
    PERFECT_UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    DIMINISHED_FIFTH = 6
    AUGMENTED_FOURTH = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    PERFECT_OCTAVE = 12


MAJOR_SCALE_INTERVALS = [2,2,1,2,2,2,1]


def get_major_scale_starting_at( i_note ):
    notes = [SHARP_NOTES[i_note]]
    for i_interval in MAJOR_SCALE_INTERVALS:
        i_note = (i_note + i_interval) % CHROMATIC_NOTE_COUNT
        notes.append(SHARP_NOTES[i_note])
    return notes

print('intervals')
for interval in Interval:
    print( interval )
    print( interval.value )

i_c_note = 0
for interval in Interval:
    i_second_note = (i_c_note + interval.value) % CHROMATIC_NOTE_COUNT
    from_note = SHARP_NOTES[i_c_note]
    to_note = SHARP_NOTES[i_second_note]
    print( "{0:s} plus {1:s} is {2:s} ({3:d} semitones)".format(from_note, interval.name, to_note, interval.value) )



for num_semitones in range(CHROMATIC_NOTE_COUNT * 2 +1):    
    i_second_note = (i_c_note + num_semitones) % CHROMATIC_NOTE_COUNT
    from_note = SHARP_NOTES[i_c_note]
    to_note = SHARP_NOTES[i_second_note]
    to_note_flat = FLAT_NOTES[i_second_note]
    print( "{0:s} plus {1:d} semitones is {2:s}/{3:s}".format(from_note,  num_semitones, to_note, to_note_flat) )



for i_current_note in range(CHROMATIC_NOTE_COUNT ):
    print('Major scale starting at {0:s}: {1:s}'.format(
        SHARP_NOTES[i_current_note], 
        ','.join( get_major_scale_starting_at(i_current_note) )))

