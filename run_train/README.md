# Training new Models

## Install dependencies
```
git clone https://github.com/mailong25/self-supervised-speech-recognition.git
cd self-supervised-speech-recognition
```

#### 0. Create a folder to store external libs
```
mkdir libs
cd libs
```

#### 1. Install python package
```
pip install soundfile torchaudio sentencepiece editdistance sklearn
If cuda version < 11 (eg. cuda 10.1):
pip install torch==1.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
If cuda >= 11:
pip install torch==1.6.0
```

#### 2. Install fairseq
```
git clone https://github.com/pytorch/fairseq.git
cd fairseq
git checkout c8a0659be5cdc15caa102d5bbf72b872567c4859
pip install --editable ./
cd ..
```

#### 3. Install dependencies for wav2letter
```
sudo apt-get update && sudo apt-get -y install apt-utils libpq-dev libsndfile-dev
sudo apt install libboost-system-dev libboost-thread-dev libboost-program-options-dev libboost-test-dev libeigen3-dev zlib1g-dev libbz2-dev liblzma-dev
sudo apt-get install libsndfile1-dev libopenblas-dev libfftw3-dev libgflags-dev libgoogle-glog-dev
```

#### 4. Install kenlm
```
git clone https://github.com/kpu/kenlm.git
cd kenlm
mkdir -p build && cd build
cmake ..
make -j 4
cd ../..
```

#### 5. Install wav2letter decoder bindings
```
git clone -b v0.2 https://github.com/facebookresearch/wav2letter.git
cd wav2letter/bindings/python
export KENLM_ROOT_DIR=path/to/libs/kenlm/ && pip install -e .
cd ../../..
```

## Train ASR

### Pre-train a wav2vec 2.0 model

1. Put all your audio files in a single folder according to guidelines emntioned below:

Format: wav, PCM 16 bit, single channel
Sampling_rate: 16000
Length: 5 to 30 seconds
Content: Silence should be removed from all audio files

2. Replace the fairseq path and audio folder path in *gen_pretrain.py* Generate pre-training transcripts using:

```
python gen_pretrain.py
```

3. Download an initial model using:

```
wget https://dl.fbaipublicfiles.com/fairseq/wav2vec/wav2vec_small.pt
```
*Our experiments showed pre-training from existing wav2vec 2.0 pre-trained models pre-trained on english language provided better results when finetuned on Indic languages rather than fine-tuning on a model pre-trained from scratch only on hindi languages*

4. Replace the manifest directory in pretrain.py and run pre-training using:

```
python pretrain.py --init_model path/to/wav2vec_small.pt
```


### Finetune your pretrained model using CTC

1. First create a manifest file of the form (for both test and valid)

```
/path/to/audio/ transcript
```
*path and transcript should be seperated by a tab*

2. Replace the destination foler path and the manifest file path in *prep.py* file and run (for both test and valid):

```
python prep.py
```

3. Create dictionary file using:

```
python gen_dict.py --transcript_file path/to/transcript.txt --save_dir path/to/save_dir
```

3. Keep all the files in a single folder, replace the path to this folder in the finetune.py file and run 

```
python finetune.py --transcript_file path/to/transcript.txt --pretrain_model path/to/pretrain_checkpoint_best.pt --dict_file path/to/dict.ltr.txt
```