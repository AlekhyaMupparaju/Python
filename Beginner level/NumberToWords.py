number2words= {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
number=input()
if(number>1 and number<9):
    print(number2words[number])
