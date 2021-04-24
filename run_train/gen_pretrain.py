import os
from os.path import join as join_path
import sys

MANIFEST_PATH = join_path('/path/to/fairseq/folder/', 'examples/wav2vec/wav2vec_manifest.py')

audio_path = 'path/to/audio/foler'

cmd = 'python ' + MANIFEST_PATH + ' ' + audio_path + ' --dest ' + temp_dir + ' --ext wav --valid-percent 0.05' #change valid-percent according to your wish
os.system(cmd)