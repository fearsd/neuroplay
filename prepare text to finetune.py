import csv
import os
import io
import logging

try:
    io.open("valid.txt", encoding='utf-8', mode="w").close()
    io.open("train.txt", encoding='utf-8', mode="w").close()
    #logging.basicConfig(filename='train.txt', filemode='w', format='%(message)s')
    
    with io.open('data1.csv', encoding='utf-8', mode='r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        #row[1] - out
        #row[2] - in
        i=0
        for row in reader:
            #print(type(row[1]))
            i+=1
            if i%20!=0:
                #logging.warning('вход: {0}\nвыход: {1}'.format(row[2], row[1]))
                train=io.open("train.txt", encoding='utf-8', mode="a")
                train.write('вход: {0}\nвыход: {1}\n'.format(row[2], row[1]))
                train.close
            else:
                valid=io.open("valid.txt", encoding='utf-8', mode="a")
                valid.write('вход: {0}\nвыход: {1}\n'.format(row[2], row[1]))
                valid.close
    print('finished normally.')
            
except Exception as e:
    print(e)
finally:
    os.system('pause')
