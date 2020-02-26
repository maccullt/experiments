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

# maybe raise instead of add
# then we could also have lower?
def add_interval_to_note(interval, i_note):
    return (i_note + interval.value) % CHROMATIC_NOTE_COUNT


def add_semitones_to_note(semitone_count, i_note):
    return (i_note + semitone_count) % CHROMATIC_NOTE_COUNT


MAJOR_SCALE_INTERVALS = [2,2,1,2,2,2,1]


def get_major_scale_starting_at( i_note ):
    notes = [SHARP_NOTES[i_note]]
    for i_interval in MAJOR_SCALE_INTERVALS:
        i_note = add_semitones_to_note(i_interval, i_note) 
        notes.append(SHARP_NOTES[i_note])
    return notes


print('intervals')
for interval in Interval:
    print( interval )
    print( interval.value )


i_c_note = 0
for interval in Interval:
    i_second_note = add_interval_to_note( interval, i_c_note)
    from_note = SHARP_NOTES[i_c_note]
    to_note = SHARP_NOTES[i_second_note]
    print( "{0:s} plus {1:s} is {2:s} ({3:d} semitones)".format(from_note, interval.name, to_note, interval.value) )



for num_semitones in range(CHROMATIC_NOTE_COUNT * 2 +1):    
    i_second_note = add_semitones_to_note(num_semitones, i_c_note) 
    from_note = SHARP_NOTES[i_c_note]
    to_note = SHARP_NOTES[i_second_note]
    to_note_flat = FLAT_NOTES[i_second_note]
    print( "{0:s} plus {1:d} semitones is {2:s}/{3:s}".format(from_note,  num_semitones, to_note, to_note_flat) )



for i_current_note in range(CHROMATIC_NOTE_COUNT ):
    print('Major scale starting at {0:s}: {1:s}'.format(
        SHARP_NOTES[i_current_note], 
        ','.join( get_major_scale_starting_at(i_current_note) )))


cycle_of_fourths = [i_c_note]
i_next_note = add_interval_to_note( Interval.PERFECT_FOURTH, cycle_of_fourths[-1] )

while i_next_note != i_c_note:
    cycle_of_fourths.append(i_next_note)
    i_next_note = add_interval_to_note( Interval.PERFECT_FOURTH, cycle_of_fourths[-1] )

cycle_notes = [FLAT_NOTES[i] for i in cycle_of_fourths]
print('cycle of fourths: {0:s}'.format(', '.join(cycle_notes)))   