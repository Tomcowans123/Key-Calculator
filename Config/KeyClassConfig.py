from PySignal import Signal

# Dataclass for the Mode, used to hold the information for the key to use later.
class Mode:
    all_modes = []

    def __init__(self, name: str, steps: list[int], chords: list[str], progression_1:list[int], progression_2:list[int], progression_3:list[int]):
        self.name = name
        # Steps Between each note 1 = half-tone 2 = whole tone
        self.steps = steps
        # The Chords-voicings within the key in order
        self.chords = chords
        #common chord progressions just using the number of each chord
        self.progression_1 = [c-1 for c in progression_1]
        self.progression_2 = [c-1 for c in progression_2]
        self.progression_3 = [c-1 for c in progression_3]
        Mode.all_modes.append(self)


major = Mode('Major',
             steps=[2, 2, 1, 2, 2, 2, 1],
             chords=[
                 'Major', 'minor', 'minor',
                 'Major', 'Major', 'minor',
                 'diminished'],
             progression_1=[1,4,5],
             progression_2=[1,5,6,4],
             progression_3=[2,5,1])
minor = Mode('Minor',
             steps=[2, 1, 2, 2, 1, 2, 2],
             chords=[
                 'minor', 'diminished', 'Major',
                 'minor', 'minor', 'Major', 'Major'
             ],
             progression_1=[1,4,5],
             progression_2=[1,6,3,7],
             progression_3=[2,5,1])
dorian = Mode('Dorian',
              steps=[2, 1, 2, 2, 2, 1, 2],
              chords=['minor', 'minor', 'major', 'major',
                      'minor', 'diminished', 'major'],
              progression_1=[1,4],
              progression_2=[1,2,4],
              progression_3=[1,3,4])
lydian = Mode('Lydian',
              steps=[2, 2, 2, 1, 2, 2, 1],
              chords=['Major', 'Major', 'Minor',
                      'Diminished', 'Major', 'Minor', 'Minor'],
              progression_1=[1,2,3,2],
              progression_2=[1,3,5],
              progression_3=[1,5,3,2])
mixolydian = Mode('Mixolydian',
                  steps=[2, 2, 1, 2, 2, 1, 2],
                  chords=['major', 'minor', 'minor b5',
                          'major', 'minor', 'minor', 'major'],
                  progression_1=[1,7,4],
                  progression_2=[1,5,7],
                  progression_3=[1,7,2])
locrian = Mode('locrian',
               steps=[1, 2, 2, 1, 2, 2, 2],
               chords=['diminished', 'major', 'minor',
                       'minor', 'major', 'major', 'minor'],
               progression_1=[1,2,3,2],
               progression_2=[1,2,3,4],
               progression_3=[1,3,5])


# used wit methods to determine information about musical keys
class Key:
    modes = list(Mode.all_modes)
    all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, root: str, mode: str):
        # root note
        self._root = root.upper()
        # Major or minor for now
        self._mode: Mode = self.find_mode(mode)
        self._notes = self.calculate_notes()
        self._chords = self.calculate_chords()
        self._steps = ['Whole' if x == 2 else 'Half' for x in self._mode.steps]
        self._identifier = f'{self._root} {self._mode.name}'
        self.progressions = {"progression 1": self.calculate_progression(self.mode.progression_1),
                             "progression 2": self.calculate_progression(self.mode.progression_2),
                             "progression 3": self.calculate_progression(self.mode.progression_3)}

    # Private: For use in another function.
    @staticmethod
    def find_mode(mode: str):
        for item in Key.modes:
            if item.name.lower() == mode.lower():
                return item
        return ValueError('Unknown mode')

    def _find_notes_from_root(self, notes=None):
        if not notes:
            notes = self.all_notes
        first_half = []
        second_part = []
        val_reached = False
        for i in notes:
            if val_reached:
                second_part.append(i)
            elif i == self._root:
                second_part.append(i)
                val_reached = True
            else:
                first_half.append(i)
        return second_part + first_half

    def calculate_chords(self):
        modal_lst = self._mode.chords
        chords = []
        for i, x in enumerate(self._notes):
            chords.append(f'{x} {modal_lst[i]}')
        return chords

    def calculate_notes(self):
        # Cycles through all notes, rejoining them as if the root note is at the start of the list
        first_half = []
        second_part = []
        val_reached = False
        for i in self.all_notes:
            if val_reached:
                second_part.append(i)
            elif i == self._root:
                second_part.append(i)
                val_reached = True
            else:
                first_half.append(i)
        chromatic_notes = second_part + first_half
        notes = []
        current_step = 0
        for x in self._mode.steps:
            notes.append(chromatic_notes[current_step])
            current_step += x
        return notes

    def calculate_progression(self, positions:list[int]):
        progression_lst = []
        for x in positions:
            progression_lst.append(self.chords[x])
        return progression_lst

    @property
    def id(self):
        return self._identifier

    @property
    def chords(self):
        return self._chords

    @property
    def root(self):
        return self._root

    @property
    def mode(self):
        return self._mode

    @property
    def notes(self):
        return self._notes

    @property
    def steps(self):
        return ' - '.join(self._steps)

    def __str__(self):
        return f""" 
    {self.id}:

    notes: {', '.join(self.notes)}

    Steps: {self.steps}

    chords: {', '.join(self.chords)}

    """


if __name__ == '__main__':
    while True:
        root = input('Root Note:')
        mode = input('Mode:')
        key = Key(root, mode)
        print(key)