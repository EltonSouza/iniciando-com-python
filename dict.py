cars = {}

cars['corola'] = "red"
cars['fit'] = "gree"
cars['A320'] = "black"

cars.keys()
cars.values()
cars['corola']


people = dict(Wesley="Father", Mariana="Mother", Sarah="baby")

if 'Wesley' in people:
    print(people['Wesley'])


for key, value in cars.items():
    print(key + " = " + value)
