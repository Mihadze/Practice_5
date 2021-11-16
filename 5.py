vowels = ('а','у','е','ы','о','э','я','ё','и','ю', 'А','У','Е','Ы','О','Э','Я','Ё','И','Ю' )
consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ')

def vow(pred):
    num = 0
    for i in (pred):
        if i in vowels:
            num += 1
    return num





def cons(pred):
    num = 0
    for i in (pred):
        if i in consonants:
            num += 1
    return num

pred = str(input('Введите предложение: '))
s = str(input('Хотите узнать кол-во гласных или согласных? '))
if s == 'гласных':
  print(vow(pred))
if s == 'согласных': 
  print(cons(pred))
