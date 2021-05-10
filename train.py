from tensorflow.keras.callbacks import ModelCheckpoint
import argparse
import matplotlib.pyplot as plt
from model import build_model
from prepare_data import setup, plots


if args.big_model:
  print('Using big model')
if args.use_data_dir:
  print('Using data directory')

# Prepare data
train_X_ims, train_X_seqs, train_Y, test_X_ims, test_X_seqs, test_Y, im_shape, vocab_size, num_answers, _, _, _ = setup()

print('\n--- Building model...')
model = build_model(im_shape, vocab_size, num_answers)
checkpoint = ModelCheckpoint('model.h5', save_best_only=True)

print('\n--- Training model...')
history = model.fit(
  [train_X_ims, train_X_seqs],
  train_Y,
  validation_data=([test_X_ims, test_X_seqs], test_Y),
  shuffle=True,
  epochs=100,
  callbacks=[checkpoint],
)   

plots(history)
