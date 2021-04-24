import argparse
import os
from os.path import join as join_path
import torch
import multiprocessing
import sys
from collections import Counter
from tqdm import tqdm
from sklearn.utils import shuffle
import ntpath
import soundfile
from shutil import copy2

def main():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--transcript_file", default=None, type=str,
                        required=False, help="Path to transcript file")
    
    parser.add_argument("--pretrain_model", default=None, required=True,
                        type=str,help="Path to pretrain wav2vec model")
    
    parser.add_argument("--dict_file", default=None, required=False,
                        type=str,help="Path to dictionary file")
    
    parser.add_argument("--batch_size", default=900000, required=False,
                        type=int,help="Batch size, try to decrease this number if any CUDA memory problems occur")
    
    parser.add_argument("--restore_file", default=None, required=False,
                        type=str,help= "Resume training from fine-tuned checkpoint")
    
    parser.add_argument("--valid_percent", default=0.05, required=False,
                        type=float,help= "Percentage of data use for validation")
    
    args = parser.parse_args()
    
    args.pretrain_model = os.path.abspath(args.pretrain_model)
    args.save_dir = os.path.abspath('/path.to/manifest/folder/')
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    
    NUM_GPU = 1
    NUM_CPU = multiprocessing.cpu_count()
    
    if NUM_GPU == 0:
        print("pytorch cannot find any GPUs !")
        sys.exit(0)
    
    
    
    #config_name = "base_1h"
    #config_name = "base_10h"
    config_name = "base_100h"
    #config_name = "base_960h"
    
    cmd = ["fairseq-hydra-train"]
    cmd.append("task.data=" + str(args.save_dir))
    cmd.append("distributed_training.distributed_world_size=" + str(NUM_GPU))
    cmd.append("+optimization.update_freq='[" + str(int(24/NUM_GPU)) + "]'")
    cmd.append("model.w2v_path=" + args.pretrain_model)
    cmd.append("dataset.num_workers=" + str(NUM_CPU))
    cmd.append("dataset.max_tokens=" + str(args.batch_size))
    
    if args.restore_file is not None:
        cmd.append("checkpoint.restore_file=" + args.restore_file)
        #cmd.append("checkpoint.reset_optimizer=True")
        #cmd.append("checkpoint.reset_lr_scheduler=True")
        #cmd.append("checkpoint.reset_dataloader=True")
        #cmd.append("checkpoint.reset_meters=True")
    
    #cmd.append("optimization.max_update=100000")
    #cmd.append("dataset.validate_after_updates=0")
    #cmd.append("model.freeze_finetune_updates=0")
    cmd.append("--config-dir config/finetuning")
    cmd.append("--config-name " + config_name)
    cmd = ' '.join(cmd)
    print(cmd)
    
    os.system(cmd)
    
main()
