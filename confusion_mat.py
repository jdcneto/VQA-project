import argparse
import numpy as np
from model import build_model
from prepare_data import setup
from sklearn.metrics import multilabel_confusion_matrix, confusion_matrix
import itertools
import matplotlib.pyplot as plt

train_X_ims, train_X_seqs, train_Y, test_X_ims, test_X_seqs, test_Y, im_shape, vocab_size, num_answers, all_answers, test_qs, test_answer_indices = setup()

print('\n--- Building model...')
model = build_model(im_shape, vocab_size, num_answers)

model.load_weights('model.h5')
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
