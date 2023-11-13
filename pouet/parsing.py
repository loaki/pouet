import xml.etree.ElementTree as ET


def pitch_to_note(pitch):
    pitch_note_dict = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 
        6: "F#",7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}
    if (pitch == -1):
        return "R"
    return pitch_note_dict[int(pitch) % 12]


def trombone_position(pitch):
    positions = {
        7: [40, 47],
        6: [41, 48],
        5: [42, 49, 54],
        4: [43, 50, 55, 59],
        3: [44, 51, 56, 60, 63, 66, 69],
        2: [45, 52, 57, 61, 64, 67, 70, 72, 74, 76, 78],
        1: [46, 53, 58, 62, 65, 68, 71, 73, 75, 77, 79]}
    for pos in positions:
        if int(pitch) in positions[pos]:
            return pos
    return 0


def parsing(path, filename):
    tree = ET.parse(path)
    root = tree.getroot()
    for measure in root.findall(".//Measure"):
        voices = measure.findall(".//voice") or [None]
        for voice in voices:
            if not voice:
                voice = measure
            for chord in voice.findall(".//Chord"):
                position = ""
                for note in chord.findall(".//Note"):
                    aspn = pitch_to_note(note.find('.//pitch').text)
                    position += str(trombone_position(note.find('.//pitch').text))
                staff_text = ET.Element("StaffText")
                ET.SubElement(staff_text, "style").text = "Measure Number"
                text = ET.SubElement(staff_text, "text")
                font = ET.SubElement(text, "font")
                font2 = ET.SubElement(text, "font")
                font.set("size","7")
                font2.set("face","FreeSans")
                font2.text = f"{position}\n{aspn}"
                if chord in list(voice):
                    index = list(voice).index(chord)
                    voice.insert(index, staff_text)
    tree.write(f"cache/{filename}_note.mscx")
