LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = 'viqywrpglile urjilaytdydbk id t yeyxjaw ygrx hx ccrhtlgsljlas lihltvsbwx hrtfsrteq tz udond uiaawrd umt leko eh ktcxsm nbhhpkk ayw urjilorkspsbu hllz ffgutthfs tg lhp ujolwwse lwndx at tl lhp lluor gf sho dtyxecxfcpl an tgxocfstthf iyimt ntf aqywce mze cxkuwmsne wafqxjeyvw ae mze znlpfm an eaw cllw oq t tlzvc ctizec bl rpywrd mg a dxl oq mwcsgaqfxk fzk lrlvanr wafqxjeyvws eajofzz tsx feepgrv hx tctfsqhjmlmaoy wasnhnecbfg hawrp mze nbhhpk wxsbtiel foy ksnohe bpasvthj ayw wxaegiebfg dnuh akgppklipl lo cxuogxj tsx kenkwt vxq'
    key = 'salt'
    mode = 'decrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)

    print('{}ed message: '.format(mode.title()))
    print(translated)

def encryptMessage(key, message):
    return translate(key, message, 'encrypt')
    
def decryptMessage(key, message):
    return translate(key, message, 'decrypt')

def translate(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
        
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

if __name__ == '__main__':
    main()


#key: salt