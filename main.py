def first():
    print("Введите фамилию, имя, отчество и год рождения:")
    a = input()
    if a == 'end': return a
    a = a.split()
    
    if len(a) >=5: raise Exception("Вы ввели неправильное количество данных")
    try: int(a[3])
    except: raise Exception("Год запишите как число")
    k = 0
    for i in range(3):
        try: 
            float(a[i])
            break
        except:
            k+=1
            continue
    if(k == 3):
        with open('file.txt', 'a') as con:
            con.write(a[0] +" "+ a[1] +" "+ a[2] +" "+ a[3] +"\n")
    else:
        print("ФИО запишите не как число")

def second():
    try:
        with open('file.txt', 'r') as conn:
            print('Фамилия Имя Отчество Год рождения')
            for line in conn:
                line=line.strip()
                print(line)
    except Exception as e:
        print(e)
while True:
    try:
        if first() == 'end': break
    except Exception as e:
        print(e)
second()