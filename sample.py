import argparse
import os

from keras.models import load_model
import numpy as np


def main():
    # arguments are listed in alphabetic order
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-l', '--length', type=int, default=2000,
                        help='maximum sampling length')
    parser.add_argument('-m', '--model', type=str,
                        help='model directory')
    parser.add_argument('-o', '--output_file', type=str,
                        help='output file name')
    parser.add_argument('-p', '--prime', type=str, default='<start>',
                        help='prime sequence')
    parser.add_argument('-t', '--temperature', type=float, default=1,
                        help='higher temperature increases diversity')
    parser.add_argument('-u', '--until', type=str, default='<end>',
                        help='stop sampling when the until sequence appears')

    args = parser.parse_args()
    sample(args)


def sample(args):
    text = open('data/input.txt').read()
    chars = sorted(list(set(text)))
    c2i = dict((c, i) for i, c in enumerate(chars))

    model_file = os.path.join(args.model, 'model.hdf5')
    model = load_model(model_file)
    _, seq_len, nb_char = model.input_shape

    generated = args.prime
    for i in range(args.length):
        x = np.zeros((1, seq_len, nb_char))
        for j, char in enumerate(reversed(generated)):
            if j >= seq_len:
                break
            x[0, seq_len - 1 - j, c2i[char]] = 1
        preds = model.predict(x)[0]
        next_char = chars[choose(preds, temperature=args.temperature)]
        generated += next_char
        if generated.endswith(args.until):
            break

    print(generated)
    with open(args.output, 'w') as f:
        f.write(generated)


def choose(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = softmax(preds / temperature)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def softmax(x):
    return np.exp(x) / np.exp(x).sum()


if __name__ == '__main__':
    main()