# 영어 문장 감지 모듈

# 모든 문자 설정
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = LETTERS + LETTERS.lower() + ' \t\n'

# txt로 저장된 사전 파일 로드
def loadDictionary():
    dictFile = open('dictionary.txt')
    engWords = {}
    for word in dictFile.read().split('\n'):
        engWords[word] = None
        # 키에 연관된 값 자체는 필요 없음
    dictFile.close()
    return engWords

ENGLISH_WORDS = loadDictionary()

# message에 들어 있는 영단어 비율 count (0.0 ~ 1.0)
def EnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0
    # message 안에 영단어가 한 개도 없으면 0.0 return

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(possibleWords)

# 문자가 아닌 것은 제거하고 나머지는 return
def removeNonLetters(message):
    onlyLetter = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            onlyLetter.append(symbol)
    
    return ''.join(onlyLetter)

# 영단어 판정
def isEnglish(message):
    wordMatch = EnglishCount(message) * 100 >= 20
    numLetters = len(removeNonLetters(message))
    letterPercent = float(numLetters) / len(message) * 100
    lettersMatch = letterPercent >= 85

    # 두 변수가 모두 True여야 True를 return
    return wordMatch and lettersMatch
