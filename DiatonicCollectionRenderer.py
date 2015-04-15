KeytoneA=1
KeytoneASharp=2
KeytoneB=3
KeytoneC=4
KeytoneCSharp=5
KeytoneD=6
KeytoneDSharp=7
KeytoneE=8
KeytoneF=9
KeytoneFSharp=10
KeytoneG=11
KeytoneGSharp=12
KeytoneAO2=13
KeytoneASharpO2=14
KeytoneBO2=15
KeytoneCO2=16
KeytoneCSharpO2=17
KeytoneDO2=18
KeytoneDSharpO2=19
KeytoneEO2=20
KeytoneFO2=21
KeytoneFSharpO2=22
KeytoneGO2=23
KeytoneGSharpO2=24

ACounter = 0
BbCounter = 0
BCounter = 0
CCounter = 0
DbCounter = 0
DCounter = 0
EbCounter = 0
ECounter = 0
FCounter = 0
GbCounter = 0
GCounter = 0
AbCounter = 0

import random

print ("Please enter your selections using the following formats:")
print ("'A' for A natural")
print ("'C#' for C sharp")
print ("'Bb' for B flat")
print ("\n")
print ("Enter 'R' for a randomized pitch class.")
print ("\n")

TonicKey = input("What pitch class is your tonic note? ")

if TonicKey == str('A'):
    TonicKey = int(KeytoneA)
    ACounter += 1
if TonicKey == str('A#') or TonicKey == str('Bb'):
    TonicKey = int(KeytoneASharp)
    BbCounter += 1
if TonicKey == str('B'):
    TonicKey = int(KeytoneB)
    BCounter += 1
if TonicKey == str('C'):
    TonicKey = int(KeytoneC)
    CCounter += 1
if TonicKey == str('C#') or TonicKey == str('Db'):
    TonicKey = int(KeytoneCSharp)
    DbCounter += 1
if TonicKey == str('D'):
    TonicKey = int(KeytoneD)
    DCounter += 1    
if TonicKey == str('D#') or TonicKey == str('Eb'):
    TonicKey = int(KeytoneDSharp)
    EbCounter += 1
if TonicKey == str('E'):
    TonicKey = int(KeytoneE)
    ECounter += 1
if TonicKey == str('F'):
    TonicKey = int(KeytoneF)
    FCounter += 1
if TonicKey == str('F#') or TonicKey == str('Gb'):
    TonicKey = int(KeytoneFSharp)
    GbCounter += 1    
if TonicKey == str('G'):
    TonicKey = int(KeytoneG)
    GCounter += 1
if TonicKey == str('G#') or TonicKey == str('Ab'):
    TonicKey = int(KeytoneGSharp)
    AbCounter += 1

if TonicKey == str('R'):
    TonicKey = int(random.randint (1,12))
       

if TonicKey == 1 or TonicKey == 13:
    TonicDisp = str('A')
if TonicKey == 2 or TonicKey == 14:
    TonicDisp = str('A#/Bb')
if TonicKey == 3 or TonicKey == 15:
    TonicDisp = str('B')
if TonicKey == 4 or TonicKey == 16:
    TonicDisp = str('C')
if TonicKey == 5 or TonicKey == 17:
    TonicDisp = str('C#/Db')
if TonicKey == 6 or TonicKey == 18:
    TonicDisp = str('D')
if TonicKey == 7 or TonicKey == 19:
    TonicDisp = str('D#/Eb')
if TonicKey == 8 or TonicKey == 20:
    TonicDisp = str('E')
if TonicKey == 9 or TonicKey == 21:
    TonicDisp = str('F')
if TonicKey == 10 or TonicKey == 22:
    TonicDisp = str('F#/Gb')
if TonicKey == 11 or TonicKey == 23:
    TonicDisp = str('G')
if TonicKey == 12 or TonicKey == 24:
    TonicDisp = str('G#/Ab')

#MAJOR/IONIAN BEGINS

Major1st = int(TonicKey+0)
Major2nd = int(TonicKey+2)
Major3rd = int(TonicKey+4)
Major4th = int(TonicKey+5)
Major5th = int(TonicKey+7)
Major6th = int(TonicKey+9)
Major7th = int(TonicKey+11)

if Major1st == 1 or Major1st == 13:
    Major1st = str('A')
    ACounter += 2 #influences pentatonic
if Major1st == 2 or Major1st == 14:
    Major1st = str('A#/Bb')
    BbCounter += 2
if Major1st == 3 or Major1st == 15:
    Major1st = str('B')
    BCounter += 2
if Major1st == 4 or Major1st == 16:
    Major1st = str('C')
    CCounter += 2
if Major1st == 5 or Major1st == 17:
    Major1st = str('C#/Db')
    DbCounter += 2
if Major1st == 6 or Major1st == 18:
    Major1st = str('D')
    DCounter += 2
if Major1st == 7 or Major1st == 19:
    Major1st = str('D#/Eb')
    EbCounter += 2
if Major1st == 8 or Major1st == 20:
    Major1st = str('E')
    ECounter += 2
if Major1st == 9 or Major1st == 21:
    Major1st = str('F')
    FCounter += 2
if Major1st == 10 or Major1st == 22:
    Major1st = str('F#/Gb')
    GbCounter += 2
if Major1st == 11 or Major1st == 23:
    Major1st = str('G')
    GCounter += 2
if Major1st == 12 or Major1st == 24:
    Major1st = str('G#/Ab')
    AbCounter += 2








##^^Counters 100% done past this point^^

if Major2nd == 1 or Major2nd == 13:
    Major2nd = str('A')
    ACounter += 2 #influences pentatonic
if Major2nd == 2 or Major2nd == 14:
    Major2nd = str('A#/Bb')
    BbCounter += 2
if Major2nd == 3 or Major2nd == 15:
    Major2nd = str('B')
    BCounter += 2
if Major2nd == 4 or Major2nd == 16:
    Major2nd = str('C')
    CCounter += 2
if Major2nd == 5 or Major2nd == 17:
    Major2nd = str('C#/Db')
if Major2nd == 6 or Major2nd == 18:
    Major2nd = str('D')
if Major2nd == 7 or Major2nd == 19:
    Major2nd = str('D#/Eb')
if Major2nd == 8 or Major2nd == 20:
    Major2nd = str('E')
if Major2nd == 9 or Major2nd == 21:
    Major2nd = str('F')
if Major2nd == 10 or Major2nd == 22:
    Major2nd = str('F#/Gb')
if Major2nd == 11 or Major2nd == 23:
    Major2nd = str('G')
if Major2nd == 12 or Major2nd == 24:
    Major2nd = str('G#/Ab')

if Major3rd == 1 or Major3rd == 13:
    Major3rd = str('A')
    ACounter += 2 #influences pentatonic
if Major3rd == 2 or Major3rd == 14:
    Major3rd = str('A#/Bb')
    BbCounter += 2
if Major3rd == 3 or Major3rd == 15:
    Major3rd = str('B')
    BCounter += 2
if Major3rd == 4 or Major3rd == 16:
    Major3rd = str('C')
    CCounter += 2
if Major3rd == 5 or Major3rd == 17:
    Major3rd = str('C#/Db')
if Major3rd == 6 or Major3rd == 18:
    Major3rd = str('D')
if Major3rd == 7 or Major3rd == 19:
    Major3rd = str('D#/Eb')
if Major3rd == 8 or Major3rd == 20:
    Major3rd = str('E')
if Major3rd == 9 or Major3rd == 21:
    Major3rd = str('F')
if Major3rd == 10 or Major3rd == 22:
    Major3rd = str('F#/Gb')
if Major3rd == 11 or Major3rd == 23:
    Major3rd = str('G')
if Major3rd == 12 or Major3rd == 24:
    Major3rd = str('G#/Ab')

if Major4th == 1 or Major4th == 13:
    Major4th = str('A')
    ACounter += 1
if Major4th == 2 or Major4th == 14:
    Major4th = str('A#/Bb')
    BbCounter += 1
if Major4th == 3 or Major4th == 15:
    Major4th = str('B')
    BCounter += 1
if Major4th == 4 or Major4th == 16:
    Major4th = str('C')
    CCounter += 1
if Major4th == 5 or Major4th == 17:
    Major4th = str('C#/Db')
if Major4th == 6 or Major4th == 18:
    Major4th = str('D')
if Major4th == 7 or Major4th == 19:
    Major4th = str('D#/Eb')
if Major4th == 8 or Major4th == 20:
    Major4th = str('E')
if Major4th == 9 or Major4th == 21:
    Major4th = str('F')
if Major4th == 10 or Major4th == 22:
    Major4th = str('F#/Gb')
if Major4th == 11 or Major4th == 23:
    Major4th = str('G')
if Major4th == 12 or Major4th == 24:
    Major4th = str('G#/Ab')

if Major5th == 1 or Major5th == 13:
    Major5th = str('A')
    ACounter += 2 #influences pentatonic
if Major5th == 2 or Major5th == 14:
    Major5th = str('A#/Bb')
    BbCounter += 2
if Major5th == 3 or Major5th == 15:
    Major5th = str('B')
    BCounter += 1
if Major5th == 4 or Major5th == 16:
    Major5th = str('C')
    CCounter += 1
if Major5th == 5 or Major5th == 17:
    Major5th = str('C#/Db')
if Major5th == 6 or Major5th == 18:
    Major5th = str('D')
if Major5th == 7 or Major5th == 19:
    Major5th = str('D#/Eb')
if Major5th == 8 or Major5th == 20:
    Major5th = str('E')
if Major5th == 9 or Major5th == 21:
    Major5th = str('F')
if Major5th == 10 or Major5th == 22:
    Major5th = str('F#/Gb')
if Major5th == 11 or Major5th == 23:
    Major5th = str('G')
if Major5th == 12 or Major5th == 24:
    Major5th = str('G#/Ab')

if Major6th == 1 or Major6th == 13:
    Major6th = str('A')
    ACounter += 2 #influences pentatonic
if Major6th == 2 or Major6th == 14:
    Major6th = str('A#/Bb')
    BbCounter += 2
if Major6th == 3 or Major6th == 15:
    Major6th = str('B')
    BCounter += 1
if Major6th == 4 or Major6th == 16:
    Major6th = str('C')
    CCounter += 2
if Major6th == 5 or Major6th == 17:
    Major6th = str('C#/Db')
if Major6th == 6 or Major6th == 18:
    Major6th = str('D')
if Major6th == 7 or Major6th == 19:
    Major6th = str('D#/Eb')
if Major6th == 8 or Major6th == 20:
    Major6th = str('E')
if Major6th == 9 or Major6th == 21:
    Major6th = str('F')
if Major6th == 10 or Major6th == 22:
    Major6th = str('F#/Gb')
if Major6th == 11 or Major6th == 23:
    Major6th = str('G')
if Major6th == 12 or Major6th == 24:
    Major6th = str('G#/Ab')

if Major7th == 1 or Major7th == 13:
    Major7th = str('A')
    ACounter += 1
if Major7th == 2 or Major7th == 14:
    Major7th = str('A#/Bb')
    BbCounter += 1
if Major7th == 3 or Major7th == 15:
    Major7th = str('B')
    BCounter += 1
if Major7th == 4 or Major7th == 16:
    Major7th = str('C')
    CCounter += 1
if Major7th == 5 or Major7th == 17:
    Major7th = str('C#/Db')
if Major7th == 6 or Major7th == 18:
    Major7th = str('D')
if Major7th == 7 or Major7th == 19:
    Major7th = str('D#/Eb')
if Major7th == 8 or Major7th == 20:
    Major7th = str('E')
if Major7th == 9 or Major7th == 21:
    Major7th = str('F')
if Major7th == 10 or Major7th == 22:
    Major7th = str('F#/Gb')
if Major7th == 11 or Major7th == 23:
    Major7th = str('G')
if Major7th == 12 or Major7th == 24:
    Major7th = str('G#/Ab')

print ("\n")
print ("\n")
MajorScaleIntro = ("The Ionian (Major Scale) collection for ") +str(TonicDisp) + (" is: ")
print (MajorScaleIntro)
MajorScale = (str (Major1st) + ("    ") + str (Major2nd) + ("    ") +str (Major3rd) + ("    ") +str (Major4th) + ("    ") +str (Major5th) + ("    ") +str (Major6th) + ("    ") +str (Major7th))
print (MajorScale)

print ("\n")
PentMajIntro = ("The Pentatonic Major collection for ") +str(TonicDisp) + (" is: ")
print (PentMajIntro)
PentMaj = (str (Major1st) + ("    ") + str (Major2nd) + ("    ") +str (Major3rd) + ("    ") +str (Major5th) + ("    ") +str (Major6th))
print (PentMaj)

#MAJOR/IONIAN ENDS
print ("\n")
#MINOR/AEOLIAN BEGINS

Minor1st = int(TonicKey+0)
Minor2nd = int(TonicKey+2)
Minor3rd = int(TonicKey+3)
Minor4th = int(TonicKey+5)
Minor5th = int(TonicKey+7)
Minor6th = int(TonicKey+8)
Minor7th = int(TonicKey+10)


if Minor1st == 1 or Minor1st == 13:
    Minor1st = str('A')
    ACounter += 2 #influences pentatonic
if Minor1st == 2 or Minor1st == 14:
    Minor1st = str('A#/Bb')
    BbCounter += 2
if Minor1st == 3 or Minor1st == 15:
    Minor1st = str('B')
    BCounter += 2
if Minor1st == 4 or Minor1st == 16:
    Minor1st = str('C')
    CCounter += 2
if Minor1st == 5 or Minor1st == 17:
    Minor1st = str('C#/Db')
if Minor1st == 6 or Minor1st == 18:
    Minor1st = str('D')
if Minor1st == 7 or Minor1st == 19:
    Minor1st = str('D#/Eb')
if Minor1st == 8 or Minor1st == 20:
    Minor1st = str('E')
if Minor1st == 9 or Minor1st == 21:
    Minor1st = str('F')
if Minor1st == 10 or Minor1st == 22:
    Minor1st = str('F#/Gb')
if Minor1st == 11 or Minor1st == 23:
    Minor1st = str('G')
if Minor1st == 12 or Minor1st == 24:
    Minor1st = str('G#/Ab')

if Minor2nd == 1 or Minor2nd == 13:
    Minor2nd = str('A')
    ACounter += 1
if Minor2nd == 2 or Minor2nd == 14:
    Minor2nd = str('A#/Bb')
    BbCounter += 1
if Minor2nd == 3 or Minor2nd == 15:
    Minor2nd = str('B')
    BCounter += 1
if Minor2nd == 4 or Minor2nd == 16:
    Minor2nd = str('C')
    CCounter += 1
if Minor2nd == 5 or Minor2nd == 17:
    Minor2nd = str('C#/Db')
if Minor2nd == 6 or Minor2nd == 18:
    Minor2nd = str('D')
if Minor2nd == 7 or Minor2nd == 19:
    Minor2nd = str('D#/Eb')
if Minor2nd == 8 or Minor2nd == 20:
    Minor2nd = str('E')
if Minor2nd == 9 or Minor2nd == 21:
    Minor2nd = str('F')
if Minor2nd == 10 or Minor2nd == 22:
    Minor2nd = str('F#/Gb')
if Minor2nd == 11 or Minor2nd == 23:
    Minor2nd = str('G')
if Minor2nd == 12 or Minor2nd == 24:
    Minor2nd = str('G#/Ab')

if Minor3rd == 1 or Minor3rd == 13:
    Minor3rd = str('A')
    ACounter += 2 #influences pentatonic
if Minor3rd == 2 or Minor3rd == 14:
    Minor3rd = str('A#/Bb')
    BbCounter += 2
if Minor3rd == 3 or Minor3rd == 15:
    Minor3rd = str('B')
    BCounter += 2
if Minor3rd == 4 or Minor3rd == 16:
    Minor3rd = str('C')
    CCounter += 2
if Minor3rd == 5 or Minor3rd == 17:
    Minor3rd = str('C#/Db')
if Minor3rd == 6 or Minor3rd == 18:
    Minor3rd = str('D')
if Minor3rd == 7 or Minor3rd == 19:
    Minor3rd = str('D#/Eb')
if Minor3rd == 8 or Minor3rd == 20:
    Minor3rd = str('E')
if Minor3rd == 9 or Minor3rd == 21:
    Minor3rd = str('F')
if Minor3rd == 10 or Minor3rd == 22:
    Minor3rd = str('F#/Gb')
if Minor3rd == 11 or Minor3rd == 23:
    Minor3rd = str('G')
if Minor3rd == 12 or Minor3rd == 24:
    Minor3rd = str('G#/Ab')

if Minor4th == 1 or Minor4th == 13:
    Minor4th = str('A')
    ACounter += 2 #influences pentatonic
if Minor4th == 2 or Minor4th == 14:
    Minor4th = str('A#/Bb')
    BbCounter += 2
if Minor4th == 3 or Minor4th == 15:
    Minor4th = str('B')
    BCounter += 2
if Minor4th == 4 or Minor4th == 16:
    Minor4th = str('C')
    CCounter += 2
if Minor4th == 5 or Minor4th == 17:
    Minor4th = str('C#/Db')
if Minor4th == 6 or Minor4th == 18:
    Minor4th = str('D')
if Minor4th == 7 or Minor4th == 19:
    Minor4th = str('D#/Eb')
if Minor4th == 8 or Minor4th == 20:
    Minor4th = str('E')
if Minor4th == 9 or Minor4th == 21:
    Minor4th = str('F')
if Minor4th == 10 or Minor4th == 22:
    Minor4th = str('F#/Gb')
if Minor4th == 11 or Minor4th == 23:
    Minor4th = str('G')
if Minor4th == 12 or Minor4th == 24:
    Minor4th = str('G#/Ab')

if Minor5th == 1 or Minor5th == 13:
    Minor5th = str('A')
    ACounter += 2 #influences pentatonic
if Minor5th == 2 or Minor5th == 14:
    Minor5th = str('A#/Bb')
    BbCounter += 2
if Minor5th == 3 or Minor5th == 15:
    Minor5th = str('B')
    BCounter += 2
if Minor5th == 4 or Minor5th == 16:
    Minor5th = str('C')
    CCounter += 2
if Minor5th == 5 or Minor5th == 17:
    Minor5th = str('C#/Db')
if Minor5th == 6 or Minor5th == 18:
    Minor5th = str('D')
if Minor5th == 7 or Minor5th == 19:
    Minor5th = str('D#/Eb')
if Minor5th == 8 or Minor5th == 20:
    Minor5th = str('E')
if Minor5th == 9 or Minor5th == 21:
    Minor5th = str('F')
if Minor5th == 10 or Minor5th == 22:
    Minor5th = str('F#/Gb')
if Minor5th == 11 or Minor5th == 23:
    Minor5th = str('G')
if Minor5th == 12 or Minor5th == 24:
    Minor5th = str('G#/Ab')

if Minor6th == 1 or Minor6th == 13:
    Minor6th = str('A')
    ACounter += 1
if Minor6th == 2 or Minor6th == 14:
    Minor6th = str('A#/Bb')
    BbCounter += 1
if Minor6th == 3 or Minor6th == 15:
    Minor6th = str('B')
    BCounter += 1
if Minor6th == 4 or Minor6th == 16:
    Minor6th = str('C')
    CCounter += 1
if Minor6th == 5 or Minor6th == 17:
    Minor6th = str('C#/Db')
if Minor6th == 6 or Minor6th == 18:
    Minor6th = str('D')
if Minor6th == 7 or Minor6th == 19:
    Minor6th = str('D#/Eb')
if Minor6th == 8 or Minor6th == 20:
    Minor6th = str('E')
if Minor6th == 9 or Minor6th == 21:
    Minor6th = str('F')
if Minor6th == 10 or Minor6th == 22:
    Minor6th = str('F#/Gb')
if Minor6th == 11 or Minor6th == 23:
    Minor6th = str('G')
if Minor6th == 12 or Minor6th == 24:
    Minor6th = str('G#/Ab')

if Minor7th == 1 or Minor7th == 13:
    Minor7th = str('A')
    ACounter += 2 #influences pentatonic
if Minor7th == 2 or Minor7th == 14:
    Minor7th = str('A#/Bb')
    BbCounter += 2
if Minor7th == 3 or Minor7th == 15:
    Minor7th = str('B')
    BCounter += 2
if Minor7th == 4 or Minor7th == 16:
    Minor7th = str('C')
    CCounter += 2
if Minor7th == 5 or Minor7th == 17:
    Minor7th = str('C#/Db')
if Minor7th == 6 or Minor7th == 18:
    Minor7th = str('D')
if Minor7th == 7 or Minor7th == 19:
    Minor7th = str('D#/Eb')
if Minor7th == 8 or Minor7th == 20:
    Minor7th = str('E')
if Minor7th == 9 or Minor7th == 21:
    Minor7th = str('F')
if Minor7th == 10 or Minor7th == 22:
    Minor7th = str('F#/Gb')
if Minor7th == 11 or Minor7th == 23:
    Minor7th = str('G')
if Minor7th == 12 or Minor7th == 24:
    Minor7th = str('G#/Ab')

MinorScaleIntro = ("The Aeolian (Natural Minor) collection for ") +str(TonicDisp) + (" is: ")
print (MinorScaleIntro)
MinorScale = (str (Minor1st) + ("    ") + str (Minor2nd) + ("    ") +str (Minor3rd) + ("    ") +str (Minor4th) + ("    ") +str (Minor5th) + ("    ") +str (Minor6th) + ("    ") +str (Minor7th)) 
print (MinorScale)

print ("\n")
PentMinIntro = ("The Pentatonic Minor collection for ") +str(TonicDisp) + (" is: ")
print (PentMinIntro)
PentMin = (str (Minor1st) + ("    ") + str (Minor3rd) + ("    ") +str (Minor4th) + ("    ") +str (Minor5th) + ("    ") +str (Minor7th))
print (PentMin)


#MINOR/AEOLIAN ENDS
print ("\n")
#DORIAN BEGINS

Dorian1st = int(TonicKey+0)
Dorian2nd = int(TonicKey+2)
Dorian3rd = int(TonicKey+3)
Dorian4th = int(TonicKey+5)
Dorian5th = int(TonicKey+7)
Dorian6th = int(TonicKey+9)
Dorian7th = int(TonicKey+10)


if Dorian1st == 1 or Dorian1st == 13:
    Dorian1st = str('A')
    ACounter += 1
if Dorian1st == 2 or Dorian1st == 14:
    Dorian1st = str('A#/Bb')
    BbCounter += 1
if Dorian1st == 3 or Dorian1st == 15:
    Dorian1st = str('B')
    BCounter += 1
if Dorian1st == 4 or Dorian1st == 16:
    Dorian1st = str('C')
    CCounter += 1
if Dorian1st == 5 or Dorian1st == 17:
    Dorian1st = str('C#/Db')
if Dorian1st == 6 or Dorian1st == 18:
    Dorian1st = str('D')
if Dorian1st == 7 or Dorian1st == 19:
    Dorian1st = str('D#/Eb')
if Dorian1st == 8 or Dorian1st == 20:
    Dorian1st = str('E')
if Dorian1st == 9 or Dorian1st == 21:
    Dorian1st = str('F')
if Dorian1st == 10 or Dorian1st == 22:
    Dorian1st = str('F#/Gb')
if Dorian1st == 11 or Dorian1st == 23:
    Dorian1st = str('G')
if Dorian1st == 12 or Dorian1st == 24:
    Dorian1st = str('G#/Ab')

if Dorian2nd == 1 or Dorian2nd == 13:
    Dorian2nd = str('A')
    ACounter += 1
if Dorian2nd == 2 or Dorian2nd == 14:
    Dorian2nd = str('A#/Bb')
    BbCounter += 1
if Dorian2nd == 3 or Dorian2nd == 15:
    Dorian2nd = str('B')
    BCounter += 1
if Dorian2nd == 4 or Dorian2nd == 16:
    Dorian2nd = str('C')
    CCounter += 1
if Dorian2nd == 5 or Dorian2nd == 17:
    Dorian2nd = str('C#/Db')
if Dorian2nd == 6 or Dorian2nd == 18:
    Dorian2nd = str('D')
if Dorian2nd == 7 or Dorian2nd == 19:
    Dorian2nd = str('D#/Eb')
if Dorian2nd == 8 or Dorian2nd == 20:
    Dorian2nd = str('E')
if Dorian2nd == 9 or Dorian2nd == 21:
    Dorian2nd = str('F')
if Dorian2nd == 10 or Dorian2nd == 22:
    Dorian2nd = str('F#/Gb')
if Dorian2nd == 11 or Dorian2nd == 23:
    Dorian2nd = str('G')
if Dorian2nd == 12 or Dorian2nd == 24:
    Dorian2nd = str('G#/Ab')

if Dorian3rd == 1 or Dorian3rd == 13:
    Dorian3rd = str('A')
    ACounter += 1
if Dorian3rd == 2 or Dorian3rd == 14:
    Dorian3rd = str('A#/Bb')
    BbCounter += 1
if Dorian3rd == 3 or Dorian3rd == 15:
    Dorian3rd = str('B')
    BCounter += 1
if Dorian3rd == 4 or Dorian3rd == 16:
    Dorian3rd = str('C')
    CCounter += 1
if Dorian3rd == 5 or Dorian3rd == 17:
    Dorian3rd = str('C#/Db')
if Dorian3rd == 6 or Dorian3rd == 18:
    Dorian3rd = str('D')
if Dorian3rd == 7 or Dorian3rd == 19:
    Dorian3rd = str('D#/Eb')
if Dorian3rd == 8 or Dorian3rd == 20:
    Dorian3rd = str('E')
if Dorian3rd == 9 or Dorian3rd == 21:
    Dorian3rd = str('F')
if Dorian3rd == 10 or Dorian3rd == 22:
    Dorian3rd = str('F#/Gb')
if Dorian3rd == 11 or Dorian3rd == 23:
    Dorian3rd = str('G')
if Dorian3rd == 12 or Dorian3rd == 24:
    Dorian3rd = str('G#/Ab')

if Dorian4th == 1 or Dorian4th == 13:
    Dorian4th = str('A')
    ACounter += 1
if Dorian4th == 2 or Dorian4th == 14:
    Dorian4th = str('A#/Bb')
    BbCounter += 1
if Dorian4th == 3 or Dorian4th == 15:
    Dorian4th = str('B')
    BCounter += 1
if Dorian4th == 4 or Dorian4th == 16:
    Dorian4th = str('C')
    CCounter += 1
if Dorian4th == 5 or Dorian4th == 17:
    Dorian4th = str('C#/Db')
if Dorian4th == 6 or Dorian4th == 18:
    Dorian4th = str('D')
if Dorian4th == 7 or Dorian4th == 19:
    Dorian4th = str('D#/Eb')
if Dorian4th == 8 or Dorian4th == 20:
    Dorian4th = str('E')
if Dorian4th == 9 or Dorian4th == 21:
    Dorian4th = str('F')
if Dorian4th == 10 or Dorian4th == 22:
    Dorian4th = str('F#/Gb')
if Dorian4th == 11 or Dorian4th == 23:
    Dorian4th = str('G')
if Dorian4th == 12 or Dorian4th == 24:
    Dorian4th = str('G#/Ab')

if Dorian5th == 1 or Dorian5th == 13:
    Dorian5th = str('A')
    ACounter += 1
if Dorian5th == 2 or Dorian5th == 14:
    Dorian5th = str('A#/Bb')
    BbCounter += 1
if Dorian5th == 3 or Dorian5th == 15:
    Dorian5th = str('B')
    BCounter += 1
if Dorian5th == 4 or Dorian5th == 16:
    Dorian5th = str('C')
    CCounter += 1
if Dorian5th == 5 or Dorian5th == 17:
    Dorian5th = str('C#/Db')
if Dorian5th == 6 or Dorian5th == 18:
    Dorian5th = str('D')
if Dorian5th == 7 or Dorian5th == 19:
    Dorian5th = str('D#/Eb')
if Dorian5th == 8 or Dorian5th == 20:
    Dorian5th = str('E')
if Dorian5th == 9 or Dorian5th == 21:
    Dorian5th = str('F')
if Dorian5th == 10 or Dorian5th == 22:
    Dorian5th = str('F#/Gb')
if Dorian5th == 11 or Dorian5th == 23:
    Dorian5th = str('G')
if Dorian5th == 12 or Dorian5th == 24:
    Dorian5th = str('G#/Ab')

if Dorian6th == 1 or Dorian6th == 13:
    Dorian6th = str('A')
    ACounter += 1
if Dorian6th == 2 or Dorian6th == 14:
    Dorian6th = str('A#/Bb')
    BbCounter += 1
if Dorian6th == 3 or Dorian6th == 15:
    Dorian6th = str('B')
    BCounter += 1
if Dorian6th == 4 or Dorian6th == 16:
    Dorian6th = str('C')
    CCounter += 1
if Dorian6th == 5 or Dorian6th == 17:
    Dorian6th = str('C#/Db')
if Dorian6th == 6 or Dorian6th == 18:
    Dorian6th = str('D')
if Dorian6th == 7 or Dorian6th == 19:
    Dorian6th = str('D#/Eb')
if Dorian6th == 8 or Dorian6th == 20:
    Dorian6th = str('E')
if Dorian6th == 9 or Dorian6th == 21:
    Dorian6th = str('F')
if Dorian6th == 10 or Dorian6th == 22:
    Dorian6th = str('F#/Gb')
if Dorian6th == 11 or Dorian6th == 23:
    Dorian6th = str('G')
if Dorian6th == 12 or Dorian6th == 24:
    Dorian6th = str('G#/Ab')

if Dorian7th == 1 or Dorian7th == 13:
    Dorian7th = str('A')
    ACounter += 1
if Dorian7th == 2 or Dorian7th == 14:
    Dorian7th = str('A#/Bb')
    BbCounter += 1
if Dorian7th == 3 or Dorian7th == 15:
    Dorian7th = str('B')
    BCounter += 1
if Dorian7th == 4 or Dorian7th == 16:
    Dorian7th = str('C')
    CCounter += 1
if Dorian7th == 5 or Dorian7th == 17:
    Dorian7th = str('C#/Db')
if Dorian7th == 6 or Dorian7th == 18:
    Dorian7th = str('D')
if Dorian7th == 7 or Dorian7th == 19:
    Dorian7th = str('D#/Eb')
if Dorian7th == 8 or Dorian7th == 20:
    Dorian7th = str('E')
if Dorian7th == 9 or Dorian7th == 21:
    Dorian7th = str('F')
if Dorian7th == 10 or Dorian7th == 22:
    Dorian7th = str('F#/Gb')
if Dorian7th == 11 or Dorian7th == 23:
    Dorian7th = str('G')
if Dorian7th == 12 or Dorian7th == 24:
    Dorian7th = str('G#/Ab')

DorianScaleIntro = ("The Dorian collection for ") +str(TonicDisp) + (" is: ")
print (DorianScaleIntro)
DorianScale = (str (Dorian1st) + ("    ") + str (Dorian2nd) + ("    ") +str (Dorian3rd) + ("    ") +str (Dorian4th) + ("    ") +str (Dorian5th) + ("    ") +str (Dorian6th) + ("    ") +str (Dorian7th)) 
print (DorianScale)

#DORIAN ENDS
print ("\n")
#MIXOLYDIAN BEGINS

Mixolydian1st = int(TonicKey+0)
Mixolydian2nd = int(TonicKey+2)
Mixolydian3rd = int(TonicKey+4)
Mixolydian4th = int(TonicKey+5)
Mixolydian5th = int(TonicKey+7)
Mixolydian6th = int(TonicKey+9)
Mixolydian7th = int(TonicKey+10)


if Mixolydian1st == 1 or Mixolydian1st == 13:
    Mixolydian1st = str('A')
    ACounter += 1
if Mixolydian1st == 2 or Mixolydian1st == 14:
    Mixolydian1st = str('A#/Bb')
    BbCounter += 1
if Mixolydian1st == 3 or Mixolydian1st == 15:
    Mixolydian1st = str('B')
    BCounter += 1
if Mixolydian1st == 4 or Mixolydian1st == 16:
    Mixolydian1st = str('C')
    CCounter += 1
if Mixolydian1st == 5 or Mixolydian1st == 17:
    Mixolydian1st = str('C#/Db')
if Mixolydian1st == 6 or Mixolydian1st == 18:
    Mixolydian1st = str('D')
if Mixolydian1st == 7 or Mixolydian1st == 19:
    Mixolydian1st = str('D#/Eb')
if Mixolydian1st == 8 or Mixolydian1st == 20:
    Mixolydian1st = str('E')
if Mixolydian1st == 9 or Mixolydian1st == 21:
    Mixolydian1st = str('F')
if Mixolydian1st == 10 or Mixolydian1st == 22:
    Mixolydian1st = str('F#/Gb')
if Mixolydian1st == 11 or Mixolydian1st == 23:
    Mixolydian1st = str('G')
if Mixolydian1st == 12 or Mixolydian1st == 24:
    Mixolydian1st = str('G#/Ab')

if Mixolydian2nd == 1 or Mixolydian2nd == 13:
    Mixolydian2nd = str('A')
    ACounter += 1
if Mixolydian2nd == 2 or Mixolydian2nd == 14:
    Mixolydian2nd = str('A#/Bb')
    BbCounter += 1
if Mixolydian2nd == 3 or Mixolydian2nd == 15:
    Mixolydian2nd = str('B')
    BCounter += 1
if Mixolydian2nd == 4 or Mixolydian2nd == 16:
    Mixolydian2nd = str('C')
    CCounter += 1
if Mixolydian2nd == 5 or Mixolydian2nd == 17:
    Mixolydian2nd = str('C#/Db')
if Mixolydian2nd == 6 or Mixolydian2nd == 18:
    Mixolydian2nd = str('D')
if Mixolydian2nd == 7 or Mixolydian2nd == 19:
    Mixolydian2nd = str('D#/Eb')
if Mixolydian2nd == 8 or Mixolydian2nd == 20:
    Mixolydian2nd = str('E')
if Mixolydian2nd == 9 or Mixolydian2nd == 21:
    Mixolydian2nd = str('F')
if Mixolydian2nd == 10 or Mixolydian2nd == 22:
    Mixolydian2nd = str('F#/Gb')
if Mixolydian2nd == 11 or Mixolydian2nd == 23:
    Mixolydian2nd = str('G')
if Mixolydian2nd == 12 or Mixolydian2nd == 24:
    Mixolydian2nd = str('G#/Ab')

if Mixolydian3rd == 1 or Mixolydian3rd == 13:
    Mixolydian3rd = str('A')
    ACounter += 1
if Mixolydian3rd == 2 or Mixolydian3rd == 14:
    Mixolydian3rd = str('A#/Bb')
    BbCounter += 1
if Mixolydian3rd == 3 or Mixolydian3rd == 15:
    Mixolydian3rd = str('B')
    BCounter += 1
if Mixolydian3rd == 4 or Mixolydian3rd == 16:
    Mixolydian3rd = str('C')
    CCounter += 1
if Mixolydian3rd == 5 or Mixolydian3rd == 17:
    Mixolydian3rd = str('C#/Db')
if Mixolydian3rd == 6 or Mixolydian3rd == 18:
    Mixolydian3rd = str('D')
if Mixolydian3rd == 7 or Mixolydian3rd == 19:
    Mixolydian3rd = str('D#/Eb')
if Mixolydian3rd == 8 or Mixolydian3rd == 20:
    Mixolydian3rd = str('E')
if Mixolydian3rd == 9 or Mixolydian3rd == 21:
    Mixolydian3rd = str('F')
if Mixolydian3rd == 10 or Mixolydian3rd == 22:
    Mixolydian3rd = str('F#/Gb')
if Mixolydian3rd == 11 or Mixolydian3rd == 23:
    Mixolydian3rd = str('G')
if Mixolydian3rd == 12 or Mixolydian3rd == 24:
    Mixolydian3rd = str('G#/Ab')

if Mixolydian4th == 1 or Mixolydian4th == 13:
    Mixolydian4th = str('A')
    ACounter += 1
if Mixolydian4th == 2 or Mixolydian4th == 14:
    Mixolydian4th = str('A#/Bb')
    BbCounter += 1
if Mixolydian4th == 3 or Mixolydian4th == 15:
    Mixolydian4th = str('B')
    BCounter += 1
if Mixolydian4th == 4 or Mixolydian4th == 16:
    Mixolydian4th = str('C')
    CCounter += 1
if Mixolydian4th == 5 or Mixolydian4th == 17:
    Mixolydian4th = str('C#/Db')
if Mixolydian4th == 6 or Mixolydian4th == 18:
    Mixolydian4th = str('D')
if Mixolydian4th == 7 or Mixolydian4th == 19:
    Mixolydian4th = str('D#/Eb')
if Mixolydian4th == 8 or Mixolydian4th == 20:
    Mixolydian4th = str('E')
if Mixolydian4th == 9 or Mixolydian4th == 21:
    Mixolydian4th = str('F')
if Mixolydian4th == 10 or Mixolydian4th == 22:
    Mixolydian4th = str('F#/Gb')
if Mixolydian4th == 11 or Mixolydian4th == 23:
    Mixolydian4th = str('G')
if Mixolydian4th == 12 or Mixolydian4th == 24:
    Mixolydian4th = str('G#/Ab')

if Mixolydian5th == 1 or Mixolydian5th == 13:
    Mixolydian5th = str('A')
    ACounter += 1
if Mixolydian5th == 2 or Mixolydian5th == 14:
    Mixolydian5th = str('A#/Bb')
    BbCounter += 1
if Mixolydian5th == 3 or Mixolydian5th == 15:
    Mixolydian5th = str('B')
    BCounter += 1
if Mixolydian5th == 4 or Mixolydian5th == 16:
    Mixolydian5th = str('C')
    CCounter += 1
if Mixolydian5th == 5 or Mixolydian5th == 17:
    Mixolydian5th = str('C#/Db')
if Mixolydian5th == 6 or Mixolydian5th == 18:
    Mixolydian5th = str('D')
if Mixolydian5th == 7 or Mixolydian5th == 19:
    Mixolydian5th = str('D#/Eb')
if Mixolydian5th == 8 or Mixolydian5th == 20:
    Mixolydian5th = str('E')
if Mixolydian5th == 9 or Mixolydian5th == 21:
    Mixolydian5th = str('F')
if Mixolydian5th == 10 or Mixolydian5th == 22:
    Mixolydian5th = str('F#/Gb')
if Mixolydian5th == 11 or Mixolydian5th == 23:
    Mixolydian5th = str('G')
if Mixolydian5th == 12 or Mixolydian5th == 24:
    Mixolydian5th = str('G#/Ab')

if Mixolydian6th == 1 or Mixolydian6th == 13:
    Mixolydian6th = str('A')
    ACounter += 1
if Mixolydian6th == 2 or Mixolydian6th == 14:
    Mixolydian6th = str('A#/Bb')
    BbCounter += 1
if Mixolydian6th == 3 or Mixolydian6th == 15:
    Mixolydian6th = str('B')
    BCounter += 1
if Mixolydian6th == 4 or Mixolydian6th == 16:
    Mixolydian6th = str('C')
    CCounter += 1
if Mixolydian6th == 5 or Mixolydian6th == 17:
    Mixolydian6th = str('C#/Db')
if Mixolydian6th == 6 or Mixolydian6th == 18:
    Mixolydian6th = str('D')
if Mixolydian6th == 7 or Mixolydian6th == 19:
    Mixolydian6th = str('D#/Eb')
if Mixolydian6th == 8 or Mixolydian6th == 20:
    Mixolydian6th = str('E')
if Mixolydian6th == 9 or Mixolydian6th == 21:
    Mixolydian6th = str('F')
if Mixolydian6th == 10 or Mixolydian6th == 22:
    Mixolydian6th = str('F#/Gb')
if Mixolydian6th == 11 or Mixolydian6th == 23:
    Mixolydian6th = str('G')
if Mixolydian6th == 12 or Mixolydian6th == 24:
    Mixolydian6th = str('G#/Ab')

if Mixolydian7th == 1 or Mixolydian7th == 13:
    Mixolydian7th = str('A')
    ACounter += 1
if Mixolydian7th == 2 or Mixolydian7th == 14:
    Mixolydian7th = str('A#/Bb')
    BbCounter += 1
if Mixolydian7th == 3 or Mixolydian7th == 15:
    Mixolydian7th = str('B')
    BCounter += 1
if Mixolydian7th == 4 or Mixolydian7th == 16:
    Mixolydian7th = str('C')
    CCounter += 1
if Mixolydian7th == 5 or Mixolydian7th == 17:
    Mixolydian7th = str('C#/Db')
if Mixolydian7th == 6 or Mixolydian7th == 18:
    Mixolydian7th = str('D')
if Mixolydian7th == 7 or Mixolydian7th == 19:
    Mixolydian7th = str('D#/Eb')
if Mixolydian7th == 8 or Mixolydian7th == 20:
    Mixolydian7th = str('E')
if Mixolydian7th == 9 or Mixolydian7th == 21:
    Mixolydian7th = str('F')
if Mixolydian7th == 10 or Mixolydian7th == 22:
    Mixolydian7th = str('F#/Gb')
if Mixolydian7th == 11 or Mixolydian7th == 23:
    Mixolydian7th = str('G')
if Mixolydian7th == 12 or Mixolydian7th == 24:
    Mixolydian7th = str('G#/Ab')

MixolydianScaleIntro = ("The Mixolydian collection for ") +str(TonicDisp) + (" is: ")
print (MixolydianScaleIntro)
MixolydianScale = (str (Mixolydian1st) + ("    ") + str (Mixolydian2nd) + ("    ") +str (Mixolydian3rd) + ("    ") +str (Mixolydian4th) + ("    ") +str (Mixolydian5th) + ("    ") +str (Mixolydian6th) + ("    ") +str (Mixolydian7th)) 
print (MixolydianScale)

print ("\n")
#MIXOLYDIAN ENDS

#PHRYGIAN BEGINS


Phrygian1st = int(TonicKey+0)
Phrygian2nd = int(TonicKey+1)
Phrygian3rd = int(TonicKey+3)
Phrygian4th = int(TonicKey+5)
Phrygian5th = int(TonicKey+7)
Phrygian6th = int(TonicKey+8)
Phrygian7th = int(TonicKey+10)


if Phrygian1st == 1 or Phrygian1st == 13:
    Phrygian1st = str('A')
    ACounter += 1
if Phrygian1st == 2 or Phrygian1st == 14:
    Phrygian1st = str('A#/Bb')
    BbCounter += 1
if Phrygian1st == 3 or Phrygian1st == 15:
    Phrygian1st = str('B')
    BCounter += 1
if Phrygian1st == 4 or Phrygian1st == 16:
    Phrygian1st = str('C')
    CCounter += 1
if Phrygian1st == 5 or Phrygian1st == 17:
    Phrygian1st = str('C#/Db')
if Phrygian1st == 6 or Phrygian1st == 18:
    Phrygian1st = str('D')
if Phrygian1st == 7 or Phrygian1st == 19:
    Phrygian1st = str('D#/Eb')
if Phrygian1st == 8 or Phrygian1st == 20:
    Phrygian1st = str('E')
if Phrygian1st == 9 or Phrygian1st == 21:
    Phrygian1st = str('F')
if Phrygian1st == 10 or Phrygian1st == 22:
    Phrygian1st = str('F#/Gb')
if Phrygian1st == 11 or Phrygian1st == 23:
    Phrygian1st = str('G')
if Phrygian1st == 12 or Phrygian1st == 24:
    Phrygian1st = str('G#/Ab')

if Phrygian2nd == 1 or Phrygian2nd == 13:
    Phrygian2nd = str('A')
    ACounter += 1
if Phrygian2nd == 2 or Phrygian2nd == 14:
    Phrygian2nd = str('A#/Bb')
    BbCounter += 1
if Phrygian2nd == 3 or Phrygian2nd == 15:
    Phrygian2nd = str('B')
    BCounter += 1
if Phrygian2nd == 4 or Phrygian2nd == 16:
    Phrygian2nd = str('C')
    CCounter += 1
if Phrygian2nd == 5 or Phrygian2nd == 17:
    Phrygian2nd = str('C#/Db')
if Phrygian2nd == 6 or Phrygian2nd == 18:
    Phrygian2nd = str('D')
if Phrygian2nd == 7 or Phrygian2nd == 19:
    Phrygian2nd = str('D#/Eb')
if Phrygian2nd == 8 or Phrygian2nd == 20:
    Phrygian2nd = str('E')
if Phrygian2nd == 9 or Phrygian2nd == 21:
    Phrygian2nd = str('F')
if Phrygian2nd == 10 or Phrygian2nd == 22:
    Phrygian2nd = str('F#/Gb')
if Phrygian2nd == 11 or Phrygian2nd == 23:
    Phrygian2nd = str('G')
if Phrygian2nd == 12 or Phrygian2nd == 24:
    Phrygian2nd = str('G#/Ab')


Freygish3rd = Phrygian3rd+1 #additional for modified Phrygian scale
if Phrygian3rd == 1 or Phrygian3rd == 13:
    Phrygian3rd = str('A')
    ACounter += 1
if Phrygian3rd == 2 or Phrygian3rd == 14:
    Phrygian3rd = str('A#/Bb')
    BbCounter += 1
if Phrygian3rd == 3 or Phrygian3rd == 15:
    Phrygian3rd = str('B')
    BCounter += 1
if Phrygian3rd == 4 or Phrygian3rd == 16:
    Phrygian3rd = str('C')
    CCounter += 1
if Phrygian3rd == 5 or Phrygian3rd == 17:
    Phrygian3rd = str('C#/Db')
if Phrygian3rd == 6 or Phrygian3rd == 18:
    Phrygian3rd = str('D')
if Phrygian3rd == 7 or Phrygian3rd == 19:
    Phrygian3rd = str('D#/Eb')
if Phrygian3rd == 8 or Phrygian3rd == 20:
    Phrygian3rd = str('E')
if Phrygian3rd == 9 or Phrygian3rd == 21:
    Phrygian3rd = str('F')
if Phrygian3rd == 10 or Phrygian3rd == 22:
    Phrygian3rd = str('F#/Gb')
if Phrygian3rd == 11 or Phrygian3rd == 23:
    Phrygian3rd = str('G')
if Phrygian3rd == 12 or Phrygian3rd == 24:
    Phrygian3rd = str('G#/Ab')

if Phrygian4th == 1 or Phrygian4th == 13:
    Phrygian4th = str('A')
    ACounter += 1
if Phrygian4th == 2 or Phrygian4th == 14:
    Phrygian4th = str('A#/Bb')
    BbCounter += 1
if Phrygian4th == 3 or Phrygian4th == 15:
    Phrygian4th = str('B')
    BCounter += 1
if Phrygian4th == 4 or Phrygian4th == 16:
    Phrygian4th = str('C')
    CCounter += 1
if Phrygian4th == 5 or Phrygian4th == 17:
    Phrygian4th = str('C#/Db')
if Phrygian4th == 6 or Phrygian4th == 18:
    Phrygian4th = str('D')
if Phrygian4th == 7 or Phrygian4th == 19:
    Phrygian4th = str('D#/Eb')
if Phrygian4th == 8 or Phrygian4th == 20:
    Phrygian4th = str('E')
if Phrygian4th == 9 or Phrygian4th == 21:
    Phrygian4th = str('F')
if Phrygian4th == 10 or Phrygian4th == 22:
    Phrygian4th = str('F#/Gb')
if Phrygian4th == 11 or Phrygian4th == 23:
    Phrygian4th = str('G')
if Phrygian4th == 12 or Phrygian4th == 24:
    Phrygian4th = str('G#/Ab')

if Phrygian5th == 1 or Phrygian5th == 13:
    Phrygian5th = str('A')
    ACounter += 1
if Phrygian5th == 2 or Phrygian5th == 14:
    Phrygian5th = str('A#/Bb')
    BbCounter += 1
if Phrygian5th == 3 or Phrygian5th == 15:
    Phrygian5th = str('B')
    BCounter += 1
if Phrygian5th == 4 or Phrygian5th == 16:
    Phrygian5th = str('C')
    CCounter += 1
if Phrygian5th == 5 or Phrygian5th == 17:
    Phrygian5th = str('C#/Db')
if Phrygian5th == 6 or Phrygian5th == 18:
    Phrygian5th = str('D')
if Phrygian5th == 7 or Phrygian5th == 19:
    Phrygian5th = str('D#/Eb')
if Phrygian5th == 8 or Phrygian5th == 20:
    Phrygian5th = str('E')
if Phrygian5th == 9 or Phrygian5th == 21:
    Phrygian5th = str('F')
if Phrygian5th == 10 or Phrygian5th == 22:
    Phrygian5th = str('F#/Gb')
if Phrygian5th == 11 or Phrygian5th == 23:
    Phrygian5th = str('G')
if Phrygian5th == 12 or Phrygian5th == 24:
    Phrygian5th = str('G#/Ab')

if Phrygian6th == 1 or Phrygian6th == 13:
    Phrygian6th = str('A')
    ACounter += 1
if Phrygian6th == 2 or Phrygian6th == 14:
    Phrygian6th = str('A#/Bb')
    BbCounter += 1
if Phrygian6th == 3 or Phrygian6th == 15:
    Phrygian6th = str('B')
    BCounter += 1
if Phrygian6th == 4 or Phrygian6th == 16:
    Phrygian6th = str('C')
    CCounter += 1
if Phrygian6th == 5 or Phrygian6th == 17:
    Phrygian6th = str('C#/Db')
if Phrygian6th == 6 or Phrygian6th == 18:
    Phrygian6th = str('D')
if Phrygian6th == 7 or Phrygian6th == 19:
    Phrygian6th = str('D#/Eb')
if Phrygian6th == 8 or Phrygian6th == 20:
    Phrygian6th = str('E')
if Phrygian6th == 9 or Phrygian6th == 21:
    Phrygian6th = str('F')
if Phrygian6th == 10 or Phrygian6th == 22:
    Phrygian6th = str('F#/Gb')
if Phrygian6th == 11 or Phrygian6th == 23:
    Phrygian6th = str('G')
if Phrygian6th == 12 or Phrygian6th == 24:
    Phrygian6th = str('G#/Ab')

if Phrygian7th == 1 or Phrygian7th == 13:
    Phrygian7th = str('A')
    ACounter += 1
if Phrygian7th == 2 or Phrygian7th == 14:
    Phrygian7th = str('A#/Bb')
    BbCounter += 1
if Phrygian7th == 3 or Phrygian7th == 15:
    Phrygian7th = str('B')
    BCounter += 1
if Phrygian7th == 4 or Phrygian7th == 16:
    Phrygian7th = str('C')
    CCounter += 1
if Phrygian7th == 5 or Phrygian7th == 17:
    Phrygian7th = str('C#/Db')
if Phrygian7th == 6 or Phrygian7th == 18:
    Phrygian7th = str('D')
if Phrygian7th == 7 or Phrygian7th == 19:
    Phrygian7th = str('D#/Eb')
if Phrygian7th == 8 or Phrygian7th == 20:
    Phrygian7th = str('E')
if Phrygian7th == 9 or Phrygian7th == 21:
    Phrygian7th = str('F')
if Phrygian7th == 10 or Phrygian7th == 22:
    Phrygian7th = str('F#/Gb')
if Phrygian7th == 11 or Phrygian7th == 23:
    Phrygian7th = str('G')
if Phrygian7th == 12 or Phrygian7th == 24:
    Phrygian7th = str('G#/Ab')

PhrygianScaleIntro = ("The Phrygian collection for ") +str(TonicDisp) + (" is: ")
print (PhrygianScaleIntro)
PhrygianScale = (str (Phrygian1st) + ("    ") + str (Phrygian2nd) + ("    ") +str (Phrygian3rd) + ("    ") +str (Phrygian4th) + ("    ") +str (Phrygian5th) + ("    ") +str (Phrygian6th) + ("    ") +str (Phrygian7th)) 
print (PhrygianScale)
print ("\n")

if Freygish3rd == 1 or Freygish3rd == 13:
    Freygish3rd = str('A')
    ACounter += 1
if Freygish3rd == 2 or Freygish3rd == 14:
    Freygish3rd = str('A#/Bb')
    BbCounter += 1
if Freygish3rd == 3 or Freygish3rd == 15:
    Freygish3rd = str('B')
    BCounter += 1
if Freygish3rd == 4 or Freygish3rd == 16:
    Freygish3rd = str('C')
    CCounter += 1
if Freygish3rd == 5 or Freygish3rd == 17:
    Freygish3rd = str('C#/Db')
if Freygish3rd == 6 or Freygish3rd == 18:
    Freygish3rd = str('D')
if Freygish3rd == 7 or Freygish3rd == 19:
    Freygish3rd = str('D#/Eb')
if Freygish3rd == 8 or Freygish3rd == 20:
    Freygish3rd = str('E')
if Freygish3rd == 9 or Freygish3rd == 21:
    Freygish3rd = str('F')
if Freygish3rd == 10 or Freygish3rd == 22:
    Freygish3rd = str('F#/Gb')
if Freygish3rd == 11 or Freygish3rd == 23:
    Freygish3rd = str('G')
if Freygish3rd == 12 or Freygish3rd == 24:
    Freygish3rd = str('G#/Ab')


FreygishScaleIntro = ("The Freygish (Phrygian Dominant) collection for ") +str(TonicDisp) + (" is: ")
print (FreygishScaleIntro)
FreygishScale = (str (Phrygian1st) + ("    ") + str (Phrygian2nd) + ("    ") +str (Freygish3rd) + ("    ") +str (Phrygian4th) + ("    ") +str (Phrygian5th) + ("    ") +str (Phrygian6th) + ("    ") +str (Phrygian7th)) 
print (FreygishScale)


#PHRYGIAN ENDS
print ("\n")

#LOCRIAN BEGINS

Locrian1st = int(TonicKey+0)
Locrian2nd = int(TonicKey+1)
Locrian3rd = int(TonicKey+3)
Locrian4th = int(TonicKey+5)
Locrian5th = int(TonicKey+6)
Locrian6th = int(TonicKey+8)
Locrian7th = int(TonicKey+10)


if Locrian1st == 1 or Locrian1st == 13:
    Locrian1st = str('A')
    ACounter += 1
if Locrian1st == 2 or Locrian1st == 14:
    Locrian1st = str('A#/Bb')
    BbCounter += 1
if Locrian1st == 3 or Locrian1st == 15:
    Locrian1st = str('B')
    BCounter += 1
if Locrian1st == 4 or Locrian1st == 16:
    Locrian1st = str('C')
    CCounter += 1
if Locrian1st == 5 or Locrian1st == 17:
    Locrian1st = str('C#/Db')
if Locrian1st == 6 or Locrian1st == 18:
    Locrian1st = str('D')
if Locrian1st == 7 or Locrian1st == 19:
    Locrian1st = str('D#/Eb')
if Locrian1st == 8 or Locrian1st == 20:
    Locrian1st = str('E')
if Locrian1st == 9 or Locrian1st == 21:
    Locrian1st = str('F')
if Locrian1st == 10 or Locrian1st == 22:
    Locrian1st = str('F#/Gb')
if Locrian1st == 11 or Locrian1st == 23:
    Locrian1st = str('G')
if Locrian1st == 12 or Locrian1st == 24:
    Locrian1st = str('G#/Ab')

if Locrian2nd == 1 or Locrian2nd == 13:
    Locrian2nd = str('A')
    ACounter += 1
if Locrian2nd == 2 or Locrian2nd == 14:
    Locrian2nd = str('A#/Bb')
    BbCounter += 1
if Locrian2nd == 3 or Locrian2nd == 15:
    Locrian2nd = str('B')
    BCounter += 1
if Locrian2nd == 4 or Locrian2nd == 16:
    Locrian2nd = str('C')
    CCounter += 1
if Locrian2nd == 5 or Locrian2nd == 17:
    Locrian2nd = str('C#/Db')
if Locrian2nd == 6 or Locrian2nd == 18:
    Locrian2nd = str('D')
if Locrian2nd == 7 or Locrian2nd == 19:
    Locrian2nd = str('D#/Eb')
if Locrian2nd == 8 or Locrian2nd == 20:
    Locrian2nd = str('E')
if Locrian2nd == 9 or Locrian2nd == 21:
    Locrian2nd = str('F')
if Locrian2nd == 10 or Locrian2nd == 22:
    Locrian2nd = str('F#/Gb')
if Locrian2nd == 11 or Locrian2nd == 23:
    Locrian2nd = str('G')
if Locrian2nd == 12 or Locrian2nd == 24:
    Locrian2nd = str('G#/Ab')

if Locrian3rd == 1 or Locrian3rd == 13:
    Locrian3rd = str('A')
    ACounter += 1
if Locrian3rd == 2 or Locrian3rd == 14:
    Locrian3rd = str('A#/Bb')
    BbCounter += 1
if Locrian3rd == 3 or Locrian3rd == 15:
    Locrian3rd = str('B')
    BCounter += 1
if Locrian3rd == 4 or Locrian3rd == 16:
    Locrian3rd = str('C')
    CCounter += 1
if Locrian3rd == 5 or Locrian3rd == 17:
    Locrian3rd = str('C#/Db')
if Locrian3rd == 6 or Locrian3rd == 18:
    Locrian3rd = str('D')
if Locrian3rd == 7 or Locrian3rd == 19:
    Locrian3rd = str('D#/Eb')
if Locrian3rd == 8 or Locrian3rd == 20:
    Locrian3rd = str('E')
if Locrian3rd == 9 or Locrian3rd == 21:
    Locrian3rd = str('F')
if Locrian3rd == 10 or Locrian3rd == 22:
    Locrian3rd = str('F#/Gb')
if Locrian3rd == 11 or Locrian3rd == 23:
    Locrian3rd = str('G')
if Locrian3rd == 12 or Locrian3rd == 24:
    Locrian3rd = str('G#/Ab')

if Locrian4th == 1 or Locrian4th == 13:
    Locrian4th = str('A')
    ACounter += 1
if Locrian4th == 2 or Locrian4th == 14:
    Locrian4th = str('A#/Bb')
    BbCounter += 1
if Locrian4th == 3 or Locrian4th == 15:
    Locrian4th = str('B')
    BCounter += 1
if Locrian4th == 4 or Locrian4th == 16:
    Locrian4th = str('C')
    CCounter += 1
if Locrian4th == 5 or Locrian4th == 17:
    Locrian4th = str('C#/Db')
if Locrian4th == 6 or Locrian4th == 18:
    Locrian4th = str('D')
if Locrian4th == 7 or Locrian4th == 19:
    Locrian4th = str('D#/Eb')
if Locrian4th == 8 or Locrian4th == 20:
    Locrian4th = str('E')
if Locrian4th == 9 or Locrian4th == 21:
    Locrian4th = str('F')
if Locrian4th == 10 or Locrian4th == 22:
    Locrian4th = str('F#/Gb')
if Locrian4th == 11 or Locrian4th == 23:
    Locrian4th = str('G')
if Locrian4th == 12 or Locrian4th == 24:
    Locrian4th = str('G#/Ab')

if Locrian5th == 1 or Locrian5th == 13:
    Locrian5th = str('A')
    ACounter += 1
if Locrian5th == 2 or Locrian5th == 14:
    Locrian5th = str('A#/Bb')
    BbCounter += 1
if Locrian5th == 3 or Locrian5th == 15:
    Locrian5th = str('B')
    BCounter += 1
if Locrian5th == 4 or Locrian5th == 16:
    Locrian5th = str('C')
    CCounter += 1
if Locrian5th == 5 or Locrian5th == 17:
    Locrian5th = str('C#/Db')
if Locrian5th == 6 or Locrian5th == 18:
    Locrian5th = str('D')
if Locrian5th == 7 or Locrian5th == 19:
    Locrian5th = str('D#/Eb')
if Locrian5th == 8 or Locrian5th == 20:
    Locrian5th = str('E')
if Locrian5th == 9 or Locrian5th == 21:
    Locrian5th = str('F')
if Locrian5th == 10 or Locrian5th == 22:
    Locrian5th = str('F#/Gb')
if Locrian5th == 11 or Locrian5th == 23:
    Locrian5th = str('G')
if Locrian5th == 12 or Locrian5th == 24:
    Locrian5th = str('G#/Ab')

if Locrian6th == 1 or Locrian6th == 13:
    Locrian6th = str('A')
    ACounter += 1
if Locrian6th == 2 or Locrian6th == 14:
    Locrian6th = str('A#/Bb')
    BbCounter += 1
if Locrian6th == 3 or Locrian6th == 15:
    Locrian6th = str('B')
    BCounter += 1
if Locrian6th == 4 or Locrian6th == 16:
    Locrian6th = str('C')
    CCounter += 1
if Locrian6th == 5 or Locrian6th == 17:
    Locrian6th = str('C#/Db')
if Locrian6th == 6 or Locrian6th == 18:
    Locrian6th = str('D')
if Locrian6th == 7 or Locrian6th == 19:
    Locrian6th = str('D#/Eb')
if Locrian6th == 8 or Locrian6th == 20:
    Locrian6th = str('E')
if Locrian6th == 9 or Locrian6th == 21:
    Locrian6th = str('F')
if Locrian6th == 10 or Locrian6th == 22:
    Locrian6th = str('F#/Gb')
if Locrian6th == 11 or Locrian6th == 23:
    Locrian6th = str('G')
if Locrian6th == 12 or Locrian6th == 24:
    Locrian6th = str('G#/Ab')

if Locrian7th == 1 or Locrian7th == 13:
    Locrian7th = str('A')
    ACounter += 1
if Locrian7th == 2 or Locrian7th == 14:
    Locrian7th = str('A#/Bb')
    BbCounter += 1
if Locrian7th == 3 or Locrian7th == 15:
    Locrian7th = str('B')
    BCounter += 1
if Locrian7th == 4 or Locrian7th == 16:
    Locrian7th = str('C')
    CCounter += 1
if Locrian7th == 5 or Locrian7th == 17:
    Locrian7th = str('C#/Db')
if Locrian7th == 6 or Locrian7th == 18:
    Locrian7th = str('D')
if Locrian7th == 7 or Locrian7th == 19:
    Locrian7th = str('D#/Eb')
if Locrian7th == 8 or Locrian7th == 20:
    Locrian7th = str('E')
if Locrian7th == 9 or Locrian7th == 21:
    Locrian7th = str('F')
if Locrian7th == 10 or Locrian7th == 22:
    Locrian7th = str('F#/Gb')
if Locrian7th == 11 or Locrian7th == 23:
    Locrian7th = str('G')
if Locrian7th == 12 or Locrian7th == 24:
    Locrian7th = str('G#/Ab')

LocrianScaleIntro = ("The Locrian collection for ") +str(TonicDisp) + (" is: ")
print (LocrianScaleIntro)
LocrianScale = (str (Locrian1st) + ("    ") + str (Locrian2nd) + ("    ") +str (Locrian3rd) + ("    ") +str (Locrian4th) + ("    ") +str (Locrian5th) + ("    ") +str (Locrian6th) + ("    ") +str (Locrian7th)) 
print (LocrianScale)

#LOCRIAN ENDS
print ("\n")
#LYDIAN BEGINS

Lydian1st = int(TonicKey+0)
Lydian2nd = int(TonicKey+2)
Lydian3rd = int(TonicKey+4)
Lydian4th = int(TonicKey+6)
Lydian5th = int(TonicKey+7)
Lydian6th = int(TonicKey+9)
Lydian7th = int(TonicKey+11)


if Lydian1st == 1 or Lydian1st == 13:
    Lydian1st = str('A')
    ACounter += 1
if Lydian1st == 2 or Lydian1st == 14:
    Lydian1st = str('A#/Bb')
    BbCounter += 1
if Lydian1st == 3 or Lydian1st == 15:
    Lydian1st = str('B')
    BCounter += 1
if Lydian1st == 4 or Lydian1st == 16:
    Lydian1st = str('C')
    CCounter += 1
if Lydian1st == 5 or Lydian1st == 17:
    Lydian1st = str('C#/Db')
if Lydian1st == 6 or Lydian1st == 18:
    Lydian1st = str('D')
if Lydian1st == 7 or Lydian1st == 19:
    Lydian1st = str('D#/Eb')
if Lydian1st == 8 or Lydian1st == 20:
    Lydian1st = str('E')
if Lydian1st == 9 or Lydian1st == 21:
    Lydian1st = str('F')
if Lydian1st == 10 or Lydian1st == 22:
    Lydian1st = str('F#/Gb')
if Lydian1st == 11 or Lydian1st == 23:
    Lydian1st = str('G')
if Lydian1st == 12 or Lydian1st == 24:
    Lydian1st = str('G#/Ab')

if Lydian2nd == 1 or Lydian2nd == 13:
    Lydian2nd = str('A')
    ACounter += 1
if Lydian2nd == 2 or Lydian2nd == 14:
    Lydian2nd = str('A#/Bb')
    BbCounter += 1
if Lydian2nd == 3 or Lydian2nd == 15:
    Lydian2nd = str('B')
    BCounter += 1
if Lydian2nd == 4 or Lydian2nd == 16:
    Lydian2nd = str('C')
    CCounter += 1
if Lydian2nd == 5 or Lydian2nd == 17:
    Lydian2nd = str('C#/Db')
if Lydian2nd == 6 or Lydian2nd == 18:
    Lydian2nd = str('D')
if Lydian2nd == 7 or Lydian2nd == 19:
    Lydian2nd = str('D#/Eb')
if Lydian2nd == 8 or Lydian2nd == 20:
    Lydian2nd = str('E')
if Lydian2nd == 9 or Lydian2nd == 21:
    Lydian2nd = str('F')
if Lydian2nd == 10 or Lydian2nd == 22:
    Lydian2nd = str('F#/Gb')
if Lydian2nd == 11 or Lydian2nd == 23:
    Lydian2nd = str('G')
if Lydian2nd == 12 or Lydian2nd == 24:
    Lydian2nd = str('G#/Ab')

if Lydian3rd == 1 or Lydian3rd == 13:
    Lydian3rd = str('A')
    ACounter += 1
if Lydian3rd == 2 or Lydian3rd == 14:
    Lydian3rd = str('A#/Bb')
    BbCounter += 1
if Lydian3rd == 3 or Lydian3rd == 15:
    Lydian3rd = str('B')
    BCounter += 1
if Lydian3rd == 4 or Lydian3rd == 16:
    Lydian3rd = str('C')
    CCounter += 1
if Lydian3rd == 5 or Lydian3rd == 17:
    Lydian3rd = str('C#/Db')
if Lydian3rd == 6 or Lydian3rd == 18:
    Lydian3rd = str('D')
if Lydian3rd == 7 or Lydian3rd == 19:
    Lydian3rd = str('D#/Eb')
if Lydian3rd == 8 or Lydian3rd == 20:
    Lydian3rd = str('E')
if Lydian3rd == 9 or Lydian3rd == 21:
    Lydian3rd = str('F')
if Lydian3rd == 10 or Lydian3rd == 22:
    Lydian3rd = str('F#/Gb')
if Lydian3rd == 11 or Lydian3rd == 23:
    Lydian3rd = str('G')
if Lydian3rd == 12 or Lydian3rd == 24:
    Lydian3rd = str('G#/Ab')

if Lydian4th == 1 or Lydian4th == 13:
    Lydian4th = str('A')
    ACounter += 1
if Lydian4th == 2 or Lydian4th == 14:
    Lydian4th = str('A#/Bb')
    BbCounter += 1
if Lydian4th == 3 or Lydian4th == 15:
    Lydian4th = str('B')
    BCounter += 1
if Lydian4th == 4 or Lydian4th == 16:
    Lydian4th = str('C')
    CCounter += 1
if Lydian4th == 5 or Lydian4th == 17:
    Lydian4th = str('C#/Db')
if Lydian4th == 6 or Lydian4th == 18:
    Lydian4th = str('D')
if Lydian4th == 7 or Lydian4th == 19:
    Lydian4th = str('D#/Eb')
if Lydian4th == 8 or Lydian4th == 20:
    Lydian4th = str('E')
if Lydian4th == 9 or Lydian4th == 21:
    Lydian4th = str('F')
if Lydian4th == 10 or Lydian4th == 22:
    Lydian4th = str('F#/Gb')
if Lydian4th == 11 or Lydian4th == 23:
    Lydian4th = str('G')
if Lydian4th == 12 or Lydian4th == 24:
    Lydian4th = str('G#/Ab')

if Lydian5th == 1 or Lydian5th == 13:
    Lydian5th = str('A')
    ACounter += 1
if Lydian5th == 2 or Lydian5th == 14:
    Lydian5th = str('A#/Bb')
    BbCounter += 1
if Lydian5th == 3 or Lydian5th == 15:
    Lydian5th = str('B')
    BCounter += 1
if Lydian5th == 4 or Lydian5th == 16:
    Lydian5th = str('C')
    CCounter += 1
if Lydian5th == 5 or Lydian5th == 17:
    Lydian5th = str('C#/Db')
if Lydian5th == 6 or Lydian5th == 18:
    Lydian5th = str('D')
if Lydian5th == 7 or Lydian5th == 19:
    Lydian5th = str('D#/Eb')
if Lydian5th == 8 or Lydian5th == 20:
    Lydian5th = str('E')
if Lydian5th == 9 or Lydian5th == 21:
    Lydian5th = str('F')
if Lydian5th == 10 or Lydian5th == 22:
    Lydian5th = str('F#/Gb')
if Lydian5th == 11 or Lydian5th == 23:
    Lydian5th = str('G')
if Lydian5th == 12 or Lydian5th == 24:
    Lydian5th = str('G#/Ab')

if Lydian6th == 1 or Lydian6th == 13:
    Lydian6th = str('A')
    ACounter += 1
if Lydian6th == 2 or Lydian6th == 14:
    Lydian6th = str('A#/Bb')
    BbCounter += 1
if Lydian6th == 3 or Lydian6th == 15:
    Lydian6th = str('B')
    BCounter += 1
if Lydian6th == 4 or Lydian6th == 16:
    Lydian6th = str('C')
    CCounter += 1
if Lydian6th == 5 or Lydian6th == 17:
    Lydian6th = str('C#/Db')
if Lydian6th == 6 or Lydian6th == 18:
    Lydian6th = str('D')
if Lydian6th == 7 or Lydian6th == 19:
    Lydian6th = str('D#/Eb')
if Lydian6th == 8 or Lydian6th == 20:
    Lydian6th = str('E')
if Lydian6th == 9 or Lydian6th == 21:
    Lydian6th = str('F')
if Lydian6th == 10 or Lydian6th == 22:
    Lydian6th = str('F#/Gb')
if Lydian6th == 11 or Lydian6th == 23:
    Lydian6th = str('G')
if Lydian6th == 12 or Lydian6th == 24:
    Lydian6th = str('G#/Ab')

if Lydian7th == 1 or Lydian7th == 13:
    Lydian7th = str('A')
    ACounter += 1
if Lydian7th == 2 or Lydian7th == 14:
    Lydian7th = str('A#/Bb')
    BbCounter += 1
if Lydian7th == 3 or Lydian7th == 15:
    Lydian7th = str('B')
    BCounter += 1
if Lydian7th == 4 or Lydian7th == 16:
    Lydian7th = str('C')
    CCounter += 1
if Lydian7th == 5 or Lydian7th == 17:
    Lydian7th = str('C#/Db')
if Lydian7th == 6 or Lydian7th == 18:
    Lydian7th = str('D')
if Lydian7th == 7 or Lydian7th == 19:
    Lydian7th = str('D#/Eb')
if Lydian7th == 8 or Lydian7th == 20:
    Lydian7th = str('E')
if Lydian7th == 9 or Lydian7th == 21:
    Lydian7th = str('F')
if Lydian7th == 10 or Lydian7th == 22:
    Lydian7th = str('F#/Gb')
if Lydian7th == 11 or Lydian7th == 23:
    Lydian7th = str('G')
if Lydian7th == 12 or Lydian7th == 24:
    Lydian7th = str('G#/Ab')

LydianScaleIntro = ("The Lydian collection for ") +str(TonicDisp) + (" is: ")
print (LydianScaleIntro)
LydianScale = (str (Lydian1st) + ("    ") + str (Lydian2nd) + ("    ") +str (Lydian3rd) + ("    ") +str (Lydian4th) + ("    ") +str (Lydian5th) + ("    ") +str (Lydian6th) + ("    ") +str (Lydian7th)) 
print (LydianScale)

print ("\n")
#LYDIAN ENDS




#ADDITIONAL NOTES BEGIN
Tritone = int(TonicKey+6)
if Tritone == 1 or Tritone == 13:
    Tritone = str('A')
    ACounter += 1
if Tritone == 2 or Tritone == 14:
    Tritone = str('A#/Bb')
    BbCounter += 1
if Tritone == 3 or Tritone == 15:
    Tritone = str('B')
    BCounter += 1
if Tritone == 4 or Tritone == 16:
    Tritone = str('C')
    CCounter += 1
if Tritone == 5 or Tritone == 17:
    Tritone = str('C#/Db')
if Tritone == 6 or Tritone == 18:
    Tritone = str('D')
if Tritone == 7 or Tritone == 19:
    Tritone = str('D#/Eb')
if Tritone == 8 or Tritone == 20:
    Tritone = str('E')
if Tritone == 9 or Tritone == 21:
    Tritone = str('F')
if Tritone == 10 or Tritone == 22:
    Tritone = str('F#/Gb')
if Tritone == 11 or Tritone == 23:
    Tritone = str('G')
if Tritone == 12 or Tritone == 24:
    Tritone = str('G#/Ab')

TritonePrinter = ("The 'Blue Note' (Tritone) of ") +str(TonicDisp) + (" is:     ")
print (TritonePrinter)
print (str(Tritone))

##Experimental section

print ("\n")
print ("In the above, each pitch class occurs the following number of times: ")
print ("\n")

AReport = ("A     = ") +str(ACounter) + (" times.")
print (AReport)
#TEST using A until you've got all 12 semitones, then copy-paste the completed, efficient code out for the rest.

if ACounter == 10:
    print ("        (Tonic of the originally-selected note.)")
if ACounter == 2:
    print ("        (Major 7th of the originally-selected note.)")
if ACounter == 6:
    print ("        (Minor 7th of the originally-selected note.)")
if ACounter == 5:
    print ("        (Major 6th of the originally-selected note.)")

BbReport = ("A#/Bb = ") +str(BbCounter) + (" times.")
print (BbReport)

BReport = ("B     = ") +str(BCounter) + (" times.")
print (BReport)

CReport = ("C     = ") +str(CCounter) + (" times.")
print (CReport)

DbReport = ("C#/Db = ") +str(DbCounter) + (" times.")
print (DbReport)

DReport = ("D     = ") +str(DCounter) + (" times.")
print (DReport)

EbReport = ("D#/Eb = ") +str(EbCounter) + (" times.")
print (EbReport)

FReport = ("F     = ") +str(FCounter) + (" times.")
print (FReport)

GbReport = ("F#/Gb = ") +str(GbCounter) + (" times.")
print (GbReport)

GReport = ("G     = ") +str(GCounter) + (" times.")
print (GReport)

AbReport = ("G#/Ab = ") +str(AbCounter) + (" times.")
print (AbReport)


##Experimental section ends

####Once all 12 are entered, you can use "if statements to describe"
##each tone based on its frequency.  Like "10" is tonic, "5" is w/e, etc.
##if two tones give the same number, further "if"ing will solve that issue.

        #(1C)Tonic,(2C#)augTonic/DimSec,(3D)MinorSec,(4D#)MajorSec,(5E)MinorThird,(6F)PerfectFourth
        #(7F#)Tritone, (8G) PerfectFifth, (9G#)MinSixth, (10A) MajSixth, (11A#)MinSeventh, (12B)MajSeventh


print ("\n")
print ("\n")
EndWaiter = input ("Press ENTER to terminate program.")


       
