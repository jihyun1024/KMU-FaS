import detectEng, vigenere

def main():
    ciphertext = 'viqywrpglile urjilaytdydbk id t yeyxjaw ygrx hx ccrhtlgsljlas lihltvsbwx hrtfsrteq tz udond uiaawrd umt leko eh ktcxsm nbhhpkk ayw urjilorkspsbu hllz ffgutthfs tg lhp ujolwwse lwndx at tl lhp lluor gf sho dtyxecxfcpl an tgxocfstthf iyimt ntf aqywce mze cxkuwmsne wafqxjeyvw ae mze znlpfm an eaw cllw oq t tlzvc ctizec bl rpywrd mg a dxl oq mwcsgaqfxk fzk lrlvanr wafqxjeyvws eajofzz tsx feepgrv hx tctfsqhjmlmaoy wasnhnecbfg hawrp mze nbhhpk wxsbtiel foy ksnohe bpasvthj ayw wxaegiebfg dnuh akgppklipl lo cxuogxj tsx kenkwt vxq'
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print('Succeed to hack encryption.')
        print(hackedMessage)
    else:
        print('Failed to hack encryption')

# 사전 파일의 각 단어로 암호문 복호화를 시도
# 복호화된 텍스트가 영어 문장으로 보이면 해당 결과 제시
def hackVigenere(ciphertext):
    f = open('dictionary.txt')
    words = f.readlines()
    f.close()

    for word in words:
        word = word.strip() # 문자열의 시작과 끝에서 공백 제거
        decrypted = vigenere.decryptMessage(word, ciphertext)
        
        if detectEng.isEnglish(decrypted):
            # 복호화된 키를 발견했는지 확인할 수 있게 함
            print()
            print('Possiple encryption break:')
            print('key ' + str(word) + ': ' + decrypted[:100])
            print()

            print('Enter D for Done, or just press ENTER to continue...')
            response = input('> ')

            if response.upper().startswith('D'):
                return decrypted
        
if __name__ == '__main__':
    main()
