from collections import defaultdict
import numpy as np
import scipy as sp


class NGram():
    def __init__(self, n: int):
        self.n: int = n

    def train(self, data: list[int]):
        self.counts: dict[int, dict[tuple, dict[int, int]]] = {}
        for i in range(len(data)):
            for j in range(min(self.n, len(data)-i)):
                context: tuple[int] = tuple(data[i:i+j])
                current = data[i+j]
                if j not in self.counts:
                    self.counts[j] = {}
                if context not in self.counts[j]:
                    self.counts[j][context] = {}
                if current not in self.counts[j][context]:
                    self.counts[j][context][current] = 0
                self.counts[j][context][current] += 1

    def emit(self, context: list[int] = [], eos_token: int = 0, n_tokens: int = 0, temperature: float = 1):
        emission: list[int] = context
        emit: int = None
        if n_tokens == 0:
            while emit != eos_token:
                emit = self.choice(emission, temperature)
                emission.append(emit)
        else:
            for _ in range(n_tokens):
                emit = self.choice(emission, temperature)
                emission.append(emit)
        return emission

    def choice(self, context: list[int] = (), temperature: float = 1):
        context = tuple()
        if self.n > 1:
            context = tuple(context[-self.n+1:])
        context_grams = self.counts[len(context)][context]
        tk_list: list[int] = []
        p_list = np.zeros((len(context_grams)))
        for i, (tk, ct) in enumerate(context_grams.items()):
            tk_list.append(tk)
            p_list[i] = ct
        p_list = p_list / np.sum(p_list)

        target = np.random.uniform()
        current_sum = 0
        i = -1
        while current_sum < target:
            i += 1
            current_sum += p_list[i]
        print(tk_list[i], ' emitted')
        return tk_list[i]


if __name__ == '__main__':
    data = [0, 1, 2, 4, 2, 5, 7, 4, 5, 3, 2, 1, 3, 4, 0, 1, 2, 3]
    model = NGram(3)
    model.train(data)
    print(model.emit())
