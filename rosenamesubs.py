import sys
import string
import codecs

mapping = {
    'a': unichr(0x2641), # Earth,
    'b': unichr(0x263e), # Moon,
    'c': unichr(0x263f), # Mercury
    'd': unichr(0x2640), # Venus
    'e': unichr(0x2609), # Sun
    'f': unichr(0x2642), # Mars
    'g': unichr(0x2643), # Jupiter
    'h': unichr(0x2644), # Saturn
    'i': unichr(0x2648), # Ram
    'l': unichr(0x2649), # Bull
    'm': unichr(0x264a), # Twins
    'n': unichr(0x264b), # Crab
    'o': unichr(0x264c), # Lion
    'p': unichr(0x264d), # Virgin
    'q': unichr(0x264e), # Scales
    'r': unichr(0x264f), # Scorpion
    's': unichr(0x2650), # Archer
    't': unichr(0x2651), # Sea-goat
    'u': unichr(0x2652), # Waterbearer
    'v': unichr(0x2652), # Waterbearer
    'z': unichr(0x2653), # Fish
    
    'j': unichr(0x2646), # Neptune
    'k': unichr(0x2645), # Uranus
    'x': unichr(0x2647), # Pluto
    'y': unichr(0x26b3), # Ceres

    'A': unichr(0x2641), # Earth,
    'B': unichr(0x263e), # Moon,
    'C': unichr(0x263f), # Mercury
    'D': unichr(0x2640), # Venus
    'E': unichr(0x2609), # Sun
    'F': unichr(0x2642), # Mars
    'G': unichr(0x2643), # Jupiter
    'H': unichr(0x2644), # Saturn
    'I': unichr(0x2648), # Ram
    'L': unichr(0x2649), # Bull
    'M': unichr(0x264a), # Twins
    'N': unichr(0x264b), # Crab
    'O': unichr(0x264c), # Lion
    'P': unichr(0x264d), # Virgin
    'Q': unichr(0x264e), # Scales
    'R': unichr(0x264f), # Scorpion
    'S': unichr(0x2650), # Archer
    'T': unichr(0x2651), # Sea-goat
    'U': unichr(0x2652), # Waterbearer
    'V': unichr(0x2652), # Waterbearer
    'Z': unichr(0x2653), # Fish
    
    'J': unichr(0x2646), # Neptune
    'K': unichr(0x2645), # Uranus
    'X': unichr(0x2647), # Pluto
    'Y': unichr(0x26b3), # Ceres
}

txt = None
out = None

if len(sys.argv) == 3:
    file = open(source)
    txt = file.read()
    out = codecs.open(dest, mode='w', encoding='utf-8')
    for ch in txt:
        try:
            out.write(mapping[ch])
        except:
            out.write(ch)
    
else:
    txt = raw_input('Write a message to encode: ')
    out = str()
    for ch in txt:
        try:
            out += mapping[ch]
        except:
            out += ch
    print out

