# Indic-ASR
Repository for pre-trained wav2vec 2.0 models on 7 Indian languages

[Link](https://drive.google.com/drive/folders/1UWCQLnU0eyDCn9lkSU1kiiaQ8FIW0NSG?usp=sharing) to wav2vec 2.0 pre-trained weights

*To know how to run inference on your own files, please refer to the run_inference folder. To train your own weights please refer to the run_train folder.* 

## Audio File Statistics --> Pre-training

### Train Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
7 Indian Languages | 5.80 | 60.0 | 0.0 | 479127

### Valid Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
7 Indian Languages | 5.81 | 60.0 | 0.0 | 25036


## Audio File Statistics (Multilingual ASR) --> Finetuning

### Train Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Hindi | 3.42 | 15.9 | 1.02 | 99925
Odia | 5.69 | 48.11 | 1.51 | 59782 
Marathi | 4.26 | 52.52 | 1.0 | 79432
Gujarati | 6.31 | 23.22 | 1.01 | 22807 
Tamil | 3.68 | 18.57 | 0.325 | 39131 
Telegu | 3.21 | 23.61 | 0.325 | 44882


### Valid Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Hindi | 5.20 | 12.66 | 1.92 | 3843
Odia | 5.7 | 18.41 | 1.56 | 3471 
Marathi | 3.85 | 11.48 | 1.0 | 4675
Gujarati | 5.85 | 13.89 | 1.97 | 3075 
Tamil | 5.85 | 14.5 | 1.71 | 3081 
Telegu | 5.92 | 19.66 | 1.514 | 3040

## Audio File Statistics (Hindi code-switched ASR) --> Finetuning

### Train Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Hindi | 2.97 | 57.0 | 0.2 | 414698

### Valid Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Hindi | 2.39 | 41.0 | 0.2 | 33907



## Audio File Statistics (Bengali code-switched ASR) --> Finetuning

### Train Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Bengali | 6.21 | 57.0 | 1.0 | 26606

### Valid Stats

Language | Mean | Max | Min | Total Files 
--- | --- | --- | --- |---
Bengali | 5.90 | 29.0 | 1.0 | 4275
