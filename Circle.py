print()
radius =float(input("Enter circle Radius: "))
distance =float(input("Enter the distance from the cilecle center to the chord: "))

perimeter= radius*2*3.14
area= radius*radius*3.14

#Chord_Length
chord_length = 2*(radius**2 - distance**2) ** 0.5
print("Circle Perimeter is :",perimeter,"   ","Circle Area is :",area,"   ","Circle Chord-Length is :",chord_length)
