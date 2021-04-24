import sys
sys.argv = ['']

import os



with open("/path/to/manifest", 'r') as file1:
    lines = file1.readlines()

files = []

for line in lines:
    feats = line.strip().split("\t")
    files.append(feats[0])

from stt_2 import Transcriber
transcriber = Transcriber(pretrain_model = '/path/to/pretrained/model/', finetune_model = '/path/to/finetuned/model/',
                          dictionary = '/path/to/dict.ltr.txt'',
                          lm_type = 'kenlm',
                          lm_lexicon = '/path/to/lexicon.txt', lm_model = '/path/to/lm.bin',
                          lm_weight = 1.5, word_score = -1, beam_size = 50)
hypos = transcriber.transcribe(files)

with open('output.txt', 'w') as f:
    for item in hypos:
        f.write("%s\n" % item)
