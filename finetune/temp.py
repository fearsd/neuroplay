def fineclass(text):
    '''
    import torch
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

    model_name_or_path = "models/essays"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
    model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cuda()

    tokenizer.special_tokens_map
    tokenizer.decode(203, clean_up_tokenization_spaces=False)
    tokenizer.encode(' ')

    #text = "Я позволю себе на всякий случай подсказать то, чего хочет артист от литературного анализа:"
    input_ids = tokenizer.encode(text, return_tensors="pt").cuda()

    out = model.generate(input_ids.cuda(), min_length=100, max_length=130, repetition_penalty=5.0, pad_token_id=225, eos_token_id=203, top_k=5, top_p=0.95, temperature=0.7, do_sample=True, num_return_sequences=5)
    '''
    output="опупдуопдукодпод. укп куцкп. укп укп. укп кпф. куркур /*w "
    #output=tokenizer.batch_decode(out, skip_special_tokens=True)

    return filtered(output, text)


def filtered(output, text):
    
    return '.'.join(output.split('.')[:-1])
import os      
print(fineclass('huy'))
os.system('pause')
