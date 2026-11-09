import random

faces = ['L', 'U', 'D', 'R', 'F', 'B']
opposites = {
        'U':'D',
        'L':'R',
        'F':'B'
        }
modifiers = ["'", "2", ""]

def scramble(faces, modifiers):
    final_scramble = []
    current_face = random.choice(faces)
    current_modifier = random.choice(modifiers)
    current_turn = current_face+current_modifier
    final_scramble.append(current_turn)
    for _ in range(19):
        previous_face = final_scramble[-1][0]
        current_face = random.choice(faces)
        opp = opposites.get(previous_face)
        while current_face == previous_face or current_face == opp:
            current_face = random.choice(faces)
        current_modifier = random.choice(modifiers)
        current_turn = current_face+current_modifier
        final_scramble.append(current_turn)
    return ' '.join(final_scramble)
