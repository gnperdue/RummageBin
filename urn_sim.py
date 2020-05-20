import random
import math

urn = ['red'] * 3 + ['black'] * 2
n_samples = 100000


def bin_err(p, n):
    return math.sqrt(p * (1 - p) / n)


n_all_red = 0
k_tries = 3
for _ in range(n_samples):
    sample = random.choices(urn, k=k_tries)
    if 'black' in sample:
        continue
    n_all_red += 1

pctg = float(n_all_red) / n_samples
err = bin_err(pctg, n_samples)
print('pctg: {:.3f} +/- {:.3f}'.format(
    pctg * 100., err * 100.
))
print('(3/5)^3 * 100 = {:.3f}'.format(100. * (3. / 5) ** 3))
