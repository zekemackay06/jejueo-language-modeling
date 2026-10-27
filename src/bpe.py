import re
import json
import time
from collections import Counter


class BPE():
    def __init__(self):
        self.str_source: str = ""
        self.str_eos: str = ""
        self.str_to_tk: dict[str, int] = {}
        self.tk_to_str: dict[int, str] = {}
        self.num_tokens: int = 0
        self.tk_source: list[int] = []

    def __str__(self):
        return f"{self.tk_source}\n{self.str_to_tk}"

    def download(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self.str_to_tk = json.load(f)
        self.tk_to_str = {i: j for j, i in self.str_to_tk.items()}
        self.str_eos = self.tk_to_str[0]
        self.num_tokens = len(self.str_to_tk)
        # print(self)

    def train(self, source, eos_str, vocab_size):
        self.str_source = source
        self.str_eos = eos_str
        self.str_to_tk[eos_str] = 0
        self.tk_to_str[0] = eos_str
        self.num_tokens += 1

        self.initialize_tokens()
        while self.num_tokens < vocab_size:
            if not self.num_tokens % 100:
                print(self.num_tokens, time.time())
            self.merge_pair()
        # print(self)

    def initialize_tokens(self):
        for c in self.str_source:
            if c not in self.str_to_tk:
                self.str_to_tk[c] = self.num_tokens
                self.tk_to_str[self.num_tokens] = c
                self.num_tokens += 1
            self.tk_source.append(self.str_to_tk[c])

    def merge_pair(self):
        pairs = list(zip(self.tk_source, self.tk_source[1:]))
        for p, i in Counter(pairs).most_common():
            if p[0] != 0 and p[1] != 0:
                pair = p
                break
        pair_str = self.decode(pair)
        self.tk_to_str[self.num_tokens] = pair_str
        self.str_to_tk[pair_str] = self.num_tokens

        n = 0
        for i, p in enumerate(pairs):
            if p == pair:
                self.tk_source[i - n] = self.num_tokens
                self.tk_source.pop(i - n + 1)
                n += 1
        self.num_tokens += 1

    def encode(self, text: str) -> list[int]:
        tokenized_text: list[int] = []
        start_idx = 0
        end_idx = 0
        while True:
            end_idx += 1

            if end_idx == len(text):
                tokenized_text.append(self.str_to_tk[text[start_idx:]])
                return tokenized_text
            if text[start_idx: end_idx+1] in self.str_to_tk:
                continue
            tokenized_text.append(self.str_to_tk[text[start_idx:end_idx]])
            start_idx = end_idx

    def decode(self, tokenized_text: list[int]) -> str:
        return ''.join([self.tk_to_str[i] for i in tokenized_text])

    def upload(self, path):
        with open(path, 'w') as f:
            json.dump(self.str_to_tk, f)


if __name__ == '__main__':
    with open('data/je.test', 'r', encoding='utf-8') as f:
        x = f.read()
    x = re.sub(r' ,', r',', x)
    x = re.sub(r'\s*[.\n]\s*', r'.', x)
    b = BPE()
    b.train(x, '. ', 8000)
    b.upload('je_8000.json')
    e = b.encode('경헤도 거 ᄉᆞᆯᄉᆞᆯ 거려뒁 먹주. 거 안 먹진 안허여')
    for i in e:
        print(i, b.tk_to_str[i])
