## Run inference on your own audio files

### WER Stats --> Multilingual ASR

Language | WER
--- | ---
Hindi | 17.2
Marathi | 9.1
Odia | 28.3
Tamil | 67
Telegu | 80
Gujarati | 57
Average | 39

### WER Stats --> Code Switched ASR (On individually trained models)

Language | WER
--- | ---
Hindi | 17
Bengali | 28
Average | 22

[Link](https://drive.google.com/drive/folders/1UWCQLnU0eyDCn9lkSU1kiiaQ8FIW0NSG?usp=sharing) to wav2vec 2.0 pre-trained weights.

Directory Structure:

```
input_data_folder/
├── multilingual-indic-ASR
└── code-switched-indic-ASR
    ├── pretrain_best.pt
    ├── hindi_bengali
    ├── only_bengali
    └── only_hindi

```

The **multilingual-indic-ASR** folder provides you with all files required for inference for inference on a mixed test set comprising of any of the 6 languages Hindi, Odia, Marathi, Tamil, Telegu, Gujarati.

The **code-switched-indic-ASR** folder consists of one pre-trained model, *pretrain_best.pt*. Further you can use lm weights and finetuned checkpoints from respective folders. We also provide you with a a folder *hindi_bengali* which can be used for inference on a mixed test set comprising of both *hindi* and *bengali*.

**Replace the respective files in the *transcription.py file* and run**

```
python transcription.py
```


