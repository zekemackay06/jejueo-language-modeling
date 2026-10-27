import bpe
import ngram
import re


if __name__ == '__main__':
    encoder = bpe.BPE()
    encoder.download('./data/je_8000.json')

    with open('./data/je.test', 'r', encoding='utf-8') as f:
        str_source = f.read()
    str_source = re.sub(r' ,', r',', str_source)
    str_source = re.sub(r'\s*[.\n]\s*', r'.', str_source)
    tk_source = encoder.encode(str_source)

    model = ngram.NGram(2)
    model.train(tk_source)

    generated_text = model.emit([0], n_tokens=10)
    decoded_generated_text = encoder.decode(generated_text)
    print(decoded_generated_text)
