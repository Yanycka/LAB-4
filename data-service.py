from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    type: str

@dataclass
class MoveOfMainAssets:
    data: str
    code: int
    potato: int
    cabbage: int
    onion: int

type_array = []
type_array.append(TypeOfMainAssets(100, "Бесарабський"))
type_array.append(TypeOfMainAssets(200, "Житній"))
type_array.append(TypeOfMainAssets(300, "Володимирський"))

move_array = []
move_array.append(MoveOfMainAssets("02.11.2016", 100, 45, 50, 70))
move_array.append(MoveOfMainAssets("02.11.2016", 200, 35, 30, 50))
move_array.append(MoveOfMainAssets("02.11.2016", 300, 35, 30, 45))
move_array.append(MoveOfMainAssets("14.11.2016", 100, 45, 45, 60))
move_array.append(MoveOfMainAssets("14.11.2016", 200, 40, 40, 50))
move_array.append(MoveOfMainAssets("14.11.2016", 300, 35, 35, 45))
move_array.append(MoveOfMainAssets("22.11.2016", 100, 40, 40, 60))
move_array.append(MoveOfMainAssets("22.11.2016", 200, 40, 40, 50))
move_array.append(MoveOfMainAssets("22.11.2016", 300, 40, 40, 60))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Статистичні дані про ринкові ціни"
    with names and values'''

    print("Дата: {data}, Код ринку: {code}, Картопля,грн.: {potato}, Капуста,грн.: {cabbage} Цибуля, грн: {onion}"
          .format(data=moveOfMainAssets.data, code=moveOfMainAssets.code, potato=moveOfMainAssets.potato,
                  cabbage=moveOfMainAssets.cabbage, onion=moveOfMainAssets.onion)) 
for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник ринків"
    with names and values'''

    print("Код: {code}, Найменування: {type}"
        .format(code=typeOfMainAssets.code, type=typeOfMainAssets.type))

for data in type_array:
    printTypeOfMainAssets(data)