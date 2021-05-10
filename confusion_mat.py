import argparse
import numpy as np
from model import build_model
from prepare_data import setup
from sklearn.metrics import multilabel_confusion_matrix, confusion_matrix
import itertools

# Support command-line options
parser = argparse.ArgumentParser()
parser.add_argument('--big-model', action='store_true')
parser.add_argument('--model-weights', help='model weights file', default='model.h5')
parser.add_argument('--use-data-dir', action='store_true', help='Use custom data directory, at /data')
args = parser.parse_args()
print('\n--- Calling train with big_model: {}'.format(args.big_model))
print('\n--- Model weights file: {}'.format(args.model_weights))
train_X_ims, train_X_seqs, train_Y, test_X_ims, test_X_seqs, test_Y, im_shape, vocab_size, num_answers, all_answers, test_qs, test_answer_indices = setup(args.use_data_dir)
print(args.use_data_dir)
print('\n--- Building model...')
model = build_model(im_shape, vocab_size, num_answers)

model.load_weights(args.model_weights)
predictions = model.predict([test_X_ims, test_X_seqs])

cm = (confusion_matrix(test_Y.argmax(axis=1), predictions.argmax(axis=1)))

def plot_confusion_matrix(cm, cmap=None):

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)

    thresh = cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, "{:,}".format(cm[i, j]),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.xticks([])
    plt.yticks([])
    plt.savefig('confusion.png')

plot_confusion_matrix(cm = cm, cmap=None)