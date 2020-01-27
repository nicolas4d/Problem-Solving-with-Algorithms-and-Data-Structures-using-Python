def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

moveTower(1, "A", "B", "C")
'''
moveing disk from A to B
'''

moveTower(2, "A", "B", "C")
'''
moveing disk from A to B
moveing disk from A to C
moveing disk from A to B
moveing disk from C to B
'''

moveTower(3, "A", "B", "C")
'''
moveing disk from A to B
moveing disk from A to C
moveing disk from A to B
moveing disk from C to B
moveing disk from A to B
moveing disk from A to C
moveing disk from B to C
moveing disk from A to B
moveing disk from C to A
moveing disk from C to B
moveing disk from A to B
'''
moveTower(6, "A", "B", "C")
