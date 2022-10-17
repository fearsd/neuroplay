import os
try:
    #os.system('pip install transformers')
    from finetune import fineclass

    input_phrase='-Я позволю себе на всякий случай подсказать то, чего хочет артист от литературного анализа.\n-'
    output_phrase=fineclass(input_phrase)
    print(output_phrase)
    
except Exception as e:
    print('\n\n\n',e)
finally:
    os.system('pause')
