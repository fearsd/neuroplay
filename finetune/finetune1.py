global model_name_or_path1
global tokenizer
global model
import os

from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM

model_name_or_path = "RichelieuGVG/model_neuroplay"
#access_token='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'
#access_token = os.environ.get("ACCESS_TOKENS")
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()

#model = AutoModel.from_pretrained(model_name_or_path).cpu()

def fineclass(text):
    
    import numpy as np
    import torch
    
    print(model.__class__.__name__)

    print(tokenizer.decode(203, clean_up_tokenization_spaces=False))

    print(tokenizer.encode(' '), 1)

    prompt = text
    input_ids = tokenizer.encode(prompt, return_tensors="pt").cpu()
    print(input_ids)

    out = model.generate(input_ids,
        max_new_tokens=100,
        min_length=70,
        pad_token_id=225,
        eos_token_id=203,
        repetition_penalty=1.3,
        temperature=0.6,
        top_k=5,
        top_p=0.95,
        do_sample=True,
        num_return_sequences=3,
        no_repeat_ngram_size=2,
        early_stopping=True
        )
    #print(out)
    output=tokenizer.batch_decode(out, skip_special_tokens=True)
    
    '''
    import torch
    
    np.random.seed(42)
    torch.manual_seed(42)

    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    
    tok = GPT2Tokenizer.from_pretrained("models/essays")
    model = GPT2LMHeadModel.from_pretrained("models/essays")
    model.cuda()

    #text = "вход: А что вы, батенька, делали намедни?\nвыход: "
    inpt = tok.encode(text, return_tensors="pt")

    out = model.generate(inpt.cuda(),
                         max_length=100,
                         repetition_penalty=5.0,
                         do_sample=True,
                         top_k=5,
                         top_p=0.95,
                         temperature=0.7)
    
    #output=tok.decode(out[0])
    output='вход:–А не пора ли нам создать наш новый народный театр?\nвыход: ютуб.com/video_id=107378365.- Вот и прекрасно! Мы с вами создадим свой, современный русский драмтеатр... И будем ставить пьесы по вашим произведениям!.. Вы только представьте себе -- наши спектакли будут носить сенсационный характер!... А публика?.. Она будет в восторге от наших спектаклей!!! Ведь это так романтично?!.. Да вы подумайте'

    '''
    return output

'''
def filt(ser1, ser):
    import numpy as np
    import pandas as pd
    
    flag = 0

    if (ser1.shape[0] == ser.shape[0]):
        flag = 1
        c = min(ser1.shape[0], 3)
    else:
        if (ser1.shape[0] > 2):
            if (ser1.iloc[0] == ser.iloc[0]):
                c = 1
                if (ser1.iloc[1] == ser.iloc[1]):
                    c = 2
                    if (ser1.iloc[2] == ser.iloc[2]):
                        c = 3
                flag = 1

        elif (ser1.shape[0] == 2):
            if (ser1.iloc[0] == ser.iloc[0]):
                c = 1
                if (ser1.iloc[1] == ser.iloc[1]):
                    c = 2
                flag = 1

        elif (ser1.shape[0] == 1):
            if (ser1.iloc[0] == ser.iloc[0]):
                c = 1
                flag = 1
    if (flag):
        if (ser1.shape[0] > 2):
            answer = ser1.iloc[:c]
        else:
            answer = ser1
        return answer
    else:
        return pd.Series([])


def filt_final(inp, arr):

    import numpy as np
    import pandas as pd
    string = arr

    alphabet1 = ['!', '?', '...']
    alphabet2 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м',
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
                'щ', 'э', 'ъ', 'ь', 'ы',
                'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
                'Й', 'К',
                'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
                'Ч', 'Ш', '«', '»', '"',
                'Щ', 'Э', 'Ю', 'Я', 'Ь', 'Ъ', 'Ы', '.', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9']
    alphabet3 = ['«', '»', '"']

    for symbol in alphabet1:
        if (symbol in string):
            string = string.replace(symbol, '.')

    string_new = ''
    for s in string:
        if (s in alphabet2):
            string_new += s
        else:
            string_new += ' '

    string = string_new
    string = string.strip()

    ser = pd.Series(string.split('.'))

    ser = ser[ser.str.len() > 0]
    ser = ser.str.strip()
    ser = ser[ser.str.len() > 0]

    for symbol in alphabet3:
        ser = ser.str.replace(symbol, ' ')

    ser1 = ser[ser.str.extract('( [А-Я])').isna()[0]]

    answer = filt(ser1, ser)
    asnwer = answer.astype('str')
    answer = answer + '.'
    answer_final = answer.values
    s = ''
    for ans in answer_final:
        s += str(ans) + ' '
    s = s.strip()
    return(s)
    
def filtered(arr,inp):
    return '. /' + inp + '. *', filt_final(inp, arr).capitalize(), '\n', '\n', arr, '\n'
        
'''
