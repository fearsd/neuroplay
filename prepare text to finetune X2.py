import csv
import os
import io
import logging

try:
    io.open("valid2.txt", encoding='utf-8', mode="w").close()
    io.open("train2.txt", encoding='utf-8', mode="w").close()
    #logging.basicConfig(filename='train.txt', filemode='w', format='%(message)s')
    
    with io.open('dataset_2.0.csv', encoding='utf-8', mode='r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        #row[1] - out
        #row[2] - in1
        #row[3] - in2
        i=0
        for row in reader:
            #print(type(row[1]))
            i+=1
            if i%20!=0:
                #logging.warning('вход: {0}\nвыход: {1}'.format(row[2], row[1]))
                train=io.open("train2.txt", encoding='utf-8', mode="a")
                train.write('вход:\n{0}\n{1}\nвыход:\n{2}\n'.format(row[2], row[3], row[1]))
                train.close
            else:
                valid=io.open("valid2.txt", encoding='utf-8', mode="a")
                valid.write('вход:\n{0}\n{1}\nвыход:\n{2}\n'.format(row[2], row[3], row[1]))
                valid.close
    print('finished normally.')
            
except Exception as e:
    print(e)
finally:
    os.system('pause')
