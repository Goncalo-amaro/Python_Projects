

def FieldDraw(p_choice):
    for row in range(7):
        if row%2==0: # r = 0,2,4,6
            current_row = int(row/2) #0,1,2,3
            print('--------------')
        else: # r = 1,3,5
            for column in range(7):
                if column % 2 == 0: # c = 0,2,4,6
                    current_column = int(column/2) #0,1,2,3
                    if column != 6:
                        print('|', end='')
                    else:
                        print('|')
                else: # c = 1,3,5
                    print(p_choice[current_column][current_row], end='')

def row_winner(lista, pl):
    if pl == 1:
        p = 'X'
    else:
        p = 'O'
    for x in range(3):
        if lista[x][0] == p and lista[x][1] == p and lista[x][2] == p:
            return True

def col_winner(lista, pl):
    if pl == 1:
        p = 'X'
    else:
        p = 'O'
    for x in range(3):
        if lista[0][x] == p and lista[1][x] == p and lista[2][x] == p:
            return True

def diag_winner(lista, pl):
    if pl == 1:
        p = 'X'
    else:
        p = 'O'
    if lista[0][0] == p and lista[1][1] == p and lista[2][2] == p:
        return True
    elif lista[0][2] == p and lista[1][1] == p and lista[2][0] == p:
        return True

def symb_converter(r,c):
    if r == 'u':
        ro = 0
    elif r == 'm':
        ro = 1
    elif r == 'l':
        ro = 2
    if c == 'l':
        co = 0
    elif c == 'm':
        co = 1
    elif c == 'r':
        co = 2
    resto = [co,ro]
    return resto

def field_verifier(r,c,fld): # Verifies if the new coordinates are already taken
    if fld[r][c] == ' ':
        return True 
    else:
        return False

Player = 1
Field_func = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#print(Field_func)
w = 0

while w == 0:
    print('Player ', Player, 'turn.')
    column_input = input('Please input the column where want to play:\n(l = left --- m = middle --- r = right)\n')
    row_input = input('Please input the row where want to play:\n(u = upper --- m = middle --- l = lower)\n')
    [r_p,c_p] = symb_converter(row_input,column_input)
    field_check = field_verifier(r_p,c_p,Field_func)
    while field_check == False:
        print('The spot choosen is already taken, please choose a new spot.')
        column_input = input('Please input the column where want to play:\n(l = left --- m = middle --- r = right)\n')
        row_input = input('Please input the row where want to play:\n(u = upper --- m = middle --- l = lower)\n')
        [r_p,c_p] = symb_converter(row_input,column_input)
        field_check = field_verifier(r_p,c_p,Field_func)
    if Player == 1:
        Field_func[r_p][c_p] = 'X'
        Player = 2
        p = 1
    else:
        Field_func[r_p][c_p] = 'O'
        Player = 1
        p = 2
    
    FieldDraw(Field_func)

    if row_winner(Field_func,Player) == True:
        print(f'The winner is player ', Player)
        w == 1
        break
    if col_winner(Field_func,Player) == True:
        print(f'The winner is player ', Player)
        w == 2
        break
    if diag_winner(Field_func,Player) == True:
        print(f'The winner is player ', Player)
        w == 3
        break

