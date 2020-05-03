# music notes

from enum import IntEnum

SHARP = '♯' # U+266F
FLAT = '♭' # U+266D
NATURAL = '♮' # U+266E
DOUBLE_SHARP = '𝄪' # U+1D12A
DOUBLE_FLAT =  '𝄫' # U+1D12B 

#            0    1    2    3    4    5    6
NOTE_SEQ = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
NOTE_SEQ_COUNT = len(NOTE_SEQ)

#                0     1     2    3     4     5     6     7    8     9   10     11
ENH_SHARPES =  ('B♯', 'C♯', 'D', 'D♯', 'E',  'E♯', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B')
SHARP_NOTES =  ('C',  'C♯', 'D', 'D♯', 'E',  'F',  'F♯', 'G', 'G♯', 'A', 'A♯', 'B')
FLAT_NOTES  =  ('C',  'D♭', 'D', 'E♭', 'E',  'F',  'G♭', 'G', 'A♭', 'A', 'B♭', 'B')
ENH_FLATS   =  ('C',  'D♭', 'D', 'E♭', 'F♭', 'F',  'G♭', 'G', 'A♭', 'A', 'B♭', 'C♭')

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


def add_semitones_to_note(semitone_count, i_note):
    return (i_note + semitone_count) % CHROMATIC_NOTE_COUNT


# maybe raise instead of add
# then we could also have lower?
def add_interval_to_note(interval, i_note):
    return add_semitones_to_note(interval.value, i_note)


def is_natural_note(i_note):
    return SHARP_NOTES[i_note] == FLAT_NOTES[i_note]


def get_next_note_name(s_note):
    note_base = s_note[0]
    i_note = NOTE_SEQ.index(note_base)
    next_i = (i_note + 1) % NOTE_SEQ_COUNT
    return NOTE_SEQ[next_i]


def make_cycle(interval, i_start):
    cycle = [i_start]
    i_next_note = add_interval_to_note( interval, cycle[-1] )
    while i_next_note != i_start:
        cycle.append(i_next_note)
        i_next_note = add_interval_to_note( interval, cycle[-1] )
    return cycle


CYCLE_OF_FITHS = make_cycle(Interval.PERFECT_FIFTH, 0)
CYCLE_FIFTH_NOTES = [FLAT_NOTES[i] for i in CYCLE_OF_FITHS]

def generate_major_key_info():
    key_info = {}
    MAX_ACCIDENTALS = 6
    sharp_cnt = 0
    flat_cnt = MAX_ACCIDENTALS
    for k in CYCLE_FIFTH_NOTES:
        key_info[k] = {"sharps": sharp_cnt if sharp_cnt < MAX_ACCIDENTALS else 0, "flats": flat_cnt if sharp_cnt == MAX_ACCIDENTALS else 0 }  
        if sharp_cnt < MAX_ACCIDENTALS:
            sharp_cnt += 1
        else:
            if flat_cnt == MAX_ACCIDENTALS:
                i_note = FLAT_NOTES.index(k)
                key_info[SHARP_NOTES[i_note]] = {"sharps": sharp_cnt, "flats": 0}
            flat_cnt -= 1
    
    return key_info

      
MAJOR_KEYS = generate_major_key_info()
for k, info in MAJOR_KEYS.items():
    print(f'key of {k} {info["sharps"]} sharps {info["flats"]} flats')


MAJOR_SCALE_INTERVALS = [2,2,1,2,2,2,1]

def find_next_note(i_note, note_name, key):
    pass


def get_major_scale_starting_at( note_name ):
    if note_name in SHARP_NOTES:
        i_note = SHARP_NOTES.index(note_name)
    elif note_name in FLAT_NOTES:
        i_note = FLAT_NOTES.index(note_name)
    else:
        raise Exception(f'Unexpected note name:"{note_name}"')

    if note_name not in MAJOR_KEYS:
        note_name = FLAT_NOTES[i_note]
        if note_name not in MAJOR_KEYS:
            raise Exception(f'No major key for note name:"{note_name}"')

    key = MAJOR_KEYS[note_name]
    notes = [note_name]

    for i_interval in MAJOR_SCALE_INTERVALS:
        i_note = add_semitones_to_note(i_interval, i_note)
        next_note_name = get_next_note_name(notes[-1])
        if key["sharps"] > 0:
            if SHARP_NOTES[i_note].startswith(next_note_name):
                notes.append(SHARP_NOTES[i_note])
            elif ENH_SHARPES[i_note].startswith(next_note_name):
                notes.append(ENH_SHARPES[i_note])
            else:
                raise Exception(f'Cannot find sharp {next_note_name} for position {i_note}')
        elif key["flats"] > 0:
            if FLAT_NOTES[i_note].startswith(next_note_name):
                notes.append(FLAT_NOTES[i_note])
            elif ENH_FLATS[i_note].startswith(next_note_name):
                notes.append(ENH_FLATS[i_note])
            else:
                raise Exception(f'Cannot find flat {next_note_name} for position {i_note}')
        elif is_natural_note(i_note):
            notes.append(SHARP_NOTES[i_note])
        else:
            raise Exception(f'Cannot find natural {next_note_name} for position {i_note}')
        
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

cycle_of_fourths = make_cycle(Interval.PERFECT_FOURTH, i_c_note)
cycle_notes = [FLAT_NOTES[i] for i in cycle_of_fourths]
print(f"cycle of fourths: {', '.join(cycle_notes)}")   

print(f"cycle of fifths: {', '.join(CYCLE_FIFTH_NOTES)}")   

for i_current_note in range(CHROMATIC_NOTE_COUNT ):
    print(f"Major scale starting at {SHARP_NOTES[i_current_note]}: {','.join( get_major_scale_starting_at(SHARP_NOTES[i_current_note]))}")
    if SHARP_NOTES[i_current_note] != FLAT_NOTES[i_current_note]: 
        print(f"Major scale starting at {FLAT_NOTES[i_current_note]}: {','.join( get_major_scale_starting_at(FLAT_NOTES[i_current_note]))}")




