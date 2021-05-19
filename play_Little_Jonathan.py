import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


notes = "sol,125-mi,125-mi,350-fa,125-re,125-re,350-do,125-re,125-mi,125-fa,125-sol,125-sol,125-sol,350"
notes = notes.split("-")
for note in notes:
    note = note.split(",")
    winsound.Beep(freqs[note[0]], int(note[1]))