for i in range(3,45,3):
    if i//3 == 8:
        break
    elif i % 2 == 0:
        continue
    else:
        print(f'{i} é impar')