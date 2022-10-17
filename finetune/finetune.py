global model_name_or_path1
global tokenizer
global model
import os


global model_name_reply
global rep_tok
global rep_model

from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM

model_name_or_path = "RichelieuGVG/model_neuroplay"
#access_token='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'
#access_token = os.environ.get("ACCESS_TOKENS")
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()


model_name_reply = "RichelieuGVG/reply_model"
rep_tok = GPT2Tokenizer.from_pretrained(model_name_reply)
rep_model = GPT2LMHeadModel.from_pretrained(model_name_reply).cpu()

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
        max_new_tokens=80,
        min_length=50,
        pad_token_id=225,
        eos_token_id=203,
        repetition_penalty=1.3,
        temperature=0.6,
        top_k=5,
        top_p=0.95,
        do_sample=True,
        num_return_sequences=2,
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

def replyclass(text):
    import torch
    import numpy as np
    

    #text = "вход: А что вы, батенька, делали намедни?\nвыход: "
    inpt = rep_tok.encode(text, return_tensors="pt")

    out = rep_model.generate(inpt.cpu(),
                         max_length=100,
                        # min_length=100,
                         repetition_penalty=5.0,
                         do_sample=True,
                         top_k=5,
                         top_p=0.95,
                         temperature=0.7,

                         num_return_sequences=2)
    
    #output=tok.decode(out)
    output=rep_tok.batch_decode(out, skip_special_tokens=True)

    return output