from time import strftime # Для створення імені файлу з датою
from random import randint # Для генерування паролю
from msvcrt import getch # Для затримки програми перед закриттям
import os # Чистка консолі при перезапуску програми, створення каталогів і перевірка їх існування (створення ярлика для програми)

# Увід кількості слів
def InputCountWord():
    valueMin = 1
    valueMax = 1_000_000
    # Увід цілого числа з діапазоном [valueMin; valueMax]
    while (True):
        try: 
            wordsCount = int(input('Уведіть кількість слів: '))
            if ( (wordsCount >= valueMin) and (wordsCount <= valueMax) ):
                return wordsCount
            else:
                print('\t', f'Діапазон допустимого вводу [{valueMin}; {valueMax}]')
        except ValueError:
            print('\t', 'Число введено неправильно')

# Видалення символів переходу на новий рядок
def DeleteSlashN(listWithN = list):
    listReturn = []
    for i in range(0, len(listWithN), 1):
        appendElement = ''
        for j in range(0, len(listWithN[i]) - 1, 1): # Останній символ '\n'
            appendElement += listWithN[i][j]
        listReturn.append(appendElement)
    return list(listReturn)

# Створення списку з використовуваними словами (увесь словник)
def CreateDictionaryWordList():
    try:
        listReturn = []
        dictionaryFile = open(os.getcwd() + '\\dictionary.txt', 'r')
        listReturn = DeleteSlashN(dictionaryFile.readlines())
        dictionaryFile.close()
    except FileNotFoundError:
        print(f'Файл \"{os.getcwd()}\\dictionary.txt\" не знайдено, програма не може запуститися')
        print('\t', 'Для закриття натисніть будь-яку клавішу')
        getch()
        os.system('cls')
    finally:
        return list(listReturn)

# Генерування слів
def GenerateWords(wordsDictionary = list, wordsCount = int):
    wordsStrReturn = ''
    if (wordsDictionary != []):
        for i in range(0, wordsCount - 1, 1):
            wordsStrReturn += wordsDictionary[randint(0, len(wordsDictionary) - 1)] + ' '
        wordsStrReturn += wordsDictionary[randint(0, len(wordsDictionary) - 1)] # Останній символ
    return str(wordsStrReturn)

# Вивід слів за кількістю
def OutputWords(wordsStrValue = list, wordsCount = int, countTab = 0):
    if (wordsStrValue != ''):
        constCountRowOfWord = 1 # Крок для створення кількості слів у рядку
        countRowOfWord = 5 + constCountRowOfWord # Кількість слів у рядку
        print(end = '\t' * countTab)
        print(f'Слова, які було згенеровано - {wordsCount}:')
        print(end = '\t' * (countTab + 1))
        countSpaces = 0
        for i in range(0, len(wordsStrValue) - 1, 1):
            if (wordsStrValue[i] == ' '):
                countSpaces += 1
            if ( ( (countSpaces + 1) % countRowOfWord ) == 0):
                print(wordsStrValue[i])
                print(end = '\t' * (countTab + 1))
                countSpaces = 0
            else:
                print(end = wordsStrValue[i])
        if (wordsStrValue[len(wordsStrValue) - 1] != ' '): # Останній символ
            print(wordsStrValue[len(wordsStrValue) - 1])

# Створення журналу роботи програми
def CreateOrAppendDataInHistoryFile(NameFile = str):
    fileHistory = open(os.getcwd() + '\\history data.txt', 'a')
    fileHistory.write(NameFile + '\n')
    fileHistory.close()

# Створення імені файлу
def CreateNameFile(wordsLength = int):
    NameFile = '[' + strftime('%d') + '.' + strftime('%m') + '.' + strftime('%Y') + ', '
    NameFile += strftime('%H') + '-' + strftime('%M') + '-' + strftime('%S') + ', '
    NameFile += 'length - ' + str(wordsLength) + '] '
    NameFile += 'GeneratePassword.txt'
    return str(NameFile)

# Створення файлу й оголошення про це
def CreateFilesWords(wordsLength = int, wordsRecord = str, usePath = str):
    if (wordsRecord != ''):
        # Створення назви файлу, файлу і запис з закриттям
        NameFile = CreateNameFile(wordsLength)
        filePassword = open(usePath + NameFile, 'w')
        filePassword.write(wordsRecord)
        filePassword.close()
    
        # Стоворення того самого на робочому столі
        fileDesktop = open(os.path.expanduser('~') + '\\Desktop\\' + NameFile, 'w')
        fileDesktop.write(wordsRecord)
        fileDesktop.close()

        print('Дані записано за адресою у файл:', end = '\n\t')
        print(os.path.expanduser('~') + '\\Desktop\\' + NameFile)
        CreateOrAppendDataInHistoryFile(NameFile)
        OutputWords(wordsRecord, wordsLength)
    else:
        print('У паролі відсутні символи, файл не записано і пароль не згенеровано')

# Створити робочу папку і файл у ній
def CreateCurrentFolderAndFileIn(wordsLength, wordsRecord):
    File_Path = os.getcwd() + '\\Work Folder\\'
    if (not os.path.exists(File_Path)):
        os.makedirs(File_Path)
    CreateFilesWords(wordsLength, wordsRecord, File_Path)

# Вихід або повтор програми
def ExitProgram():
    countEqualSymbol = 75
    print()
    print('=' * countEqualSymbol)
    answerReplay = input('Бажаєте перезапустити програму (\"+\" - так)?: ')
    if (answerReplay == '+'):
        print('\t', 'Консоль буде очищено, натисніть будь-яку клавішу ...')
    else:
        print('\t', 'Програму завершено, натисніть будь-яку клавішу ...')
    print('=' * countEqualSymbol)
    getch()
    os.system('cls')

    if (answerReplay == '+'):
        return False
    else:
        return True

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================

# Головна програма
while (CreateDictionaryWordList() != []):
    wordsCount = InputCountWord()
    wordsValue = GenerateWords(CreateDictionaryWordList(), wordsCount)
    CreateCurrentFolderAndFileIn(wordsCount, wordsValue)

    if (ExitProgram()):
        break