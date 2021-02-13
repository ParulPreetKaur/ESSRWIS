from simpful import *
from queringsql_tables import get_surfacedata
import random
 # Create a fuzzy system object
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=1, d=2), term='IceWarning')
S_2 = FuzzySet(function=Trapezoidal_MF(a=1, b=2, c=3, d=4), term='IceWatch')
S_3 = FuzzySet(function=Triangular_MF(a=3, b=4, c=5), term='ChemicalWet')
S_4 = FuzzySet(function=Triangular_MF(a=4, b=5, c=6), term='Wet')
S_5 = FuzzySet(function=Trapezoidal_MF(a=5, b=6, c=7, d=8), term='TraceMoisture')
S_6 = FuzzySet(function=Trapezoidal_MF(a=7, b=8, c=10, d=10), term='Dry')
FS.add_linguistic_variable('SurfaceCondition', LinguisticVariable([S_1, S_2, S_3,S_4, S_5,S_6], concept='Surface Condition', universe_of_discourse=[0,10]))
Plot1=LinguisticVariable([S_1, S_2, S_3,S_4,S_5,S_6], concept='Surface Condition', universe_of_discourse=[0,11])
#Plot1.plot()

#Surface temp is in Farenheit eg 10 F is 12degree celcius
SCTEMP_1 = FuzzySet(function=Trapezoidal_MF(a=-20, b=-20, c=0, d=30), term='verylow')
SCTEMP_2 = FuzzySet(function=Triangular_MF(a=0, b=30, c=60), term='low')
SCTEMP_3 = FuzzySet(function=Triangular_MF(a=30, b=60, c=90), term='medium')
SCTEMP_4 = FuzzySet(function=Triangular_MF(a=60, b=90, c=110), term='high')
#SCTEMP_5 = FuzzySet(function=Trapezoidal_MF(a=90, b=110, c=140, d=140), term='veryhigh')
FS.add_linguistic_variable('SurfaceTemperature', LinguisticVariable([SCTEMP_1, SCTEMP_2, SCTEMP_3, SCTEMP_4], concept='Surface Temperature', universe_of_discourse=[-20,145]))
#Plot2=LinguisticVariable([SCTEMP_1, SCTEMP_2,SCTEMP_3,SCTEMP_4], concept='Surface Temperature', universe_of_discourse=[-20,145])
#Plot2.plot()

# Define output fuzzy sets and linguistic variable
RoadCond_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.2, d=0.3), term='non slippery')
RoadCond_2 = FuzzySet(function=Triangular_MF(a=0.2, b=0.4, c=0.6), term='slippery')
RoadCond_3 = FuzzySet(function=Trapezoidal_MF(a=0.4, b=0.6, c=1, d=1), term='veryslippery')
FS.add_linguistic_variable('Road', LinguisticVariable([RoadCond_1, RoadCond_2,RoadCond_3], universe_of_discourse=[0,1.2]))
#Plot3=LinguisticVariable([RoadCond_1, RoadCond_2,RoadCond_3], universe_of_discourse=[0,1.2])
#Plot3.plot()

 # Define fuzzy rules
#R1 = 'IF (SurfaceCondition IS TraceMoisture) AND (SurfaceTemperature IS verylow) THEN (Road IS non slippery)'
#R2 = 'IF (SurfaceCondition IS TraceMoisture) AND (SurfaceTemperature IS low) THEN (Road IS non slippery)'
#R3 = 'IF (SurfaceCondition IS TraceMoisture) AND (SurfaceTemperature IS medium) THEN (Road IS non slippery)'
#R4 = 'IF (SurfaceCondition IS TraceMoisture) AND (SurfaceTemperature IS high) THEN (Road IS non slippery)'
#R5 = 'IF (SurfaceCondition IS IceWatch) AND (SurfaceTemperature IS verylow) THEN (Road IS veryslippery)'
#R6 = 'IF (SurfaceCondition IS IceWatch) AND (SurfaceTemperature IS low) THEN (Road IS slippery) '
#R7 = 'IF (SurfaceCondition IS IceWatch) AND (SurfaceTemperature IS medium) THEN (Road IS slippery)'
#R8 = 'IF (SurfaceCondition IS IceWatch) AND (SurfaceTemperature IS high) THEN (Road IS slippery)'
R8 = 'IF (SurfaceCondition IS Dry) AND (SurfaceTemperature IS verylow) THEN (Road IS non slippery) '
R9 = 'IF (SurfaceCondition IS Dry) AND (SurfaceTemperature IS low) THEN (Road IS non slippery)'
R10 = 'IF (SurfaceCondition IS Dry) AND (SurfaceTemperature IS medium)  THEN (Road IS non slippery) '
R11 = 'IF (SurfaceCondition IS Dry) AND (SurfaceTemperature IS high) THEN (Road IS non slippery)'
#R12 = 'IF (SurfaceCondition IS IceWarning) AND (SurfaceTemperature IS verylow) THEN (Road IS veryslippery)'
#R13 = 'IF (SurfaceCondition IS IceWarning) AND (SurfaceTemperature IS low) THEN (Road IS veryslippery)'
#R15 = 'IF (SurfaceCondition IS IceWarning) AND (SurfaceTemperature IS medium) THEN (Road IS slippery)'
#R16 = 'IF (SurfaceCondition IS IceWarning) AND (SurfaceTemperature IS high) THEN (Road IS slippery)'
#R17 = 'IF (SurfaceCondition IS SnowWarning) AND (SurfaceTemperature IS vlow) THEN (Road IS veryslippery)'
#R18 = 'IF (SurfaceCondition IS SnowWarning) AND (SurfaceTemperature IS low) THEN (Road IS veryslippery)'
#R19 = 'IF (SurfaceCondition IS SnowWarning) AND (SurfaceTemperature IS medium) THEN (Road IS slippery)'
#R20 = 'IF (SurfaceCondition IS SnowWarning) AND (SurfaceTemperature IS high) THEN (Road IS slippery)'

#FS.add_rules([R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13])
FS.add_rules([R8,R9,R10,R11])
 # Set antecedents values
Surfacedata=get_surfacedata()
SurfaceC=Surfacedata[0][0]
SurfaceCond=SurfaceC.replace(" ", "")
SurfaceTemp=Surfacedata[0][1]
#print(S_2)

if (SurfaceCond=='Dry'):
    number = random.uniform(0, 10)
if (SurfaceCond=='IceWatch'):
    number = random.uniform(0, 5)
if (SurfaceCond=='IceWarning'):
    number = random.uniform(5, 15)
if (SurfaceCond=='SnowWarning'):
    number = random.uniform(15, 20)
if (SurfaceCond=='TraceMoisture'):
    number = random.uniform(10, 20)

print(number)
print(SurfaceTemp)

FS.set_variable('SurfaceCondition', number)
FS.set_variable('SurfaceTemperature', SurfaceTemp)

FS.Mamdani_inference(['Road'])

#print((FS.Mamdani_inference(['Road'])).plot())
 # Perform Mamdani inference and print output
print(FS.Mamdani_inference(['Road']))