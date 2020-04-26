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

def make_cycle(interval):
    cycle = [i_c_note]
    i_next_note = add_interval_to_note( interval, cycle[-1] )
    while i_next_note != i_c_note:
        cycle.append(i_next_note)
        i_next_note = add_interval_to_note( interval, cycle[-1] )
    return cycle

MAJOR_SCALE_INTERVALS = [2,2,1,2,2,2,1]


def get_major_scale_starting_at( i_note ):
    notes = [SHARP_NOTES[i_note]]
    for i_interval in MAJOR_SCALE_INTERVALS:
        i_note = add_semitones_to_note(i_interval, i_note)
        if  SHARP_NOTES[i_note] != FLAT_NOTES[i_note]:            
            # this note is a sharp check the degree
            if len(notes) > 0 and notes[-1] == SHARP_NOTES[i_note -1]:
                notes.append(FLAT_NOTES[i_note])
            else:    
                notes.append(SHARP_NOTES[i_note])
        else:    
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
    print( f"{from_note} plus {interval.name} is {to_note} ({interval.value} semitones)")

for num_semitones in range(CHROMATIC_NOTE_COUNT * 2 +1):    
    i_second_note = add_semitones_to_note(num_semitones, i_c_note) 
    from_note = SHARP_NOTES[i_c_note]
    to_note = SHARP_NOTES[i_second_note]
    to_note_flat = FLAT_NOTES[i_second_note]
    print( f'{from_note} plus {num_semitones} semitones is {to_note}/{to_note_flat}')

for i_current_note in range(CHROMATIC_NOTE_COUNT ):
    print(f"Major scale starting at {SHARP_NOTES[i_current_note]}: {','.join( get_major_scale_starting_at(i_current_note))}")

cycle_of_fourths = make_cycle(Interval.PERFECT_FOURTH)
cycle_notes = [FLAT_NOTES[i] for i in cycle_of_fourths]
print(f"cycle of fourths: {', '.join(cycle_notes)}")   

cycle_of_fifths = make_cycle(Interval.PERFECT_FIFTH)
cycle_notes = [FLAT_NOTES[i] for i in cycle_of_fifths]
print(f"cycle of fifths: {', '.join(cycle_notes)}")   

for i_key in cycle_of_fifths:
    major_scale = get_major_scale_starting_at(i_key)

