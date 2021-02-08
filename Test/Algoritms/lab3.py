import time

start_time = time.time()
array_char=[]

def get():
    noun=input("іменник чоловічий або жіночий \n")
    print(noun)
    return noun
def check(char):
    first=['б','п','в','м','ф','ж','ч','ш','дж','г','к','х','ґ','д','т','з','ц','дз','с','л','н','р']
    second=['а','o','у','i','и','е']
    for i in range(len(first)):
        if(char==first[i]):
            return 1
    for i in range(len(second)):
        if(char==second[i]):
            return 2

    return 0

def convert(s,a,array_char):
    str1 = ""
    array_char[a-1]=s
    #print(array_char)
    # separating words by str1
    return (str1.join(array_char))

def noun(noun):
    array_char = list(noun)
    if noun.endswith("а") or noun.endswith("я"):
        a=int(len(array_char))
        w=a-1
        x=0
        if(array_char[a-1]=='я'):
            x=2
        else:
            x = check(array_char[a - 2])
        print("Слово належить до першої відміни...")
        if x==1:
            print("ТВЕРДА")
            print("H "+convert('а',a,array_char))
            print("Р "+convert('и',a,array_char))
            print("Д "+convert('і',a,array_char))
            print("Зн "+convert('у',a,array_char))
            print("Ор "+convert('ою',a,array_char))
            print("М "+convert('і', a,array_char))
            print("Кл "+convert('о', a,array_char))


        if x==2:
            print("М'ЯКА")
            print("H "+convert('я', a, array_char))
            print("Р "+convert('і', a, array_char))
            print("Д "+convert('і', a, array_char))
            print("ЗН "+convert('ю', a, array_char))
            print("Ор "+convert('ею', a, array_char))
            print("М "+convert('і', a, array_char))
            print("Кл "+convert('е', a, array_char))

    else:
        print("Слово не належить до першої відміни!")
    print("--- %s seconds ---" % (time.time() - start_time))

noun(get())