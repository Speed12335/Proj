import time

def slowType(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
        
slowType(''' The Atlas Hotel was established in the late 19th century, a time of global expansion and modernization. Named after the mythical Greek Titan who held up the heavens, the hotel was envisioned as a grand destination where travelers from all over the world could find luxurious comfort. Built in a prominent urban center—often a coastal or commercial hub—the Atlas quickly became a beacon of high society. Its architecture, a blend of classical and emerging modernist elements, set it apart from other hotels of the era.''')
