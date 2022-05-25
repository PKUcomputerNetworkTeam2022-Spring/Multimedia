#! /bin/bash

# wandb env variables
export WANDB_ENTITY=${WNADB_ENTITY}

DATE=`date +%Y%m%d`

export WANDB_RUN_GROUP="Chinese BART Summary"
export WANDB_RUN_NOTES="Training Chinese BART summary model."

python -m torch.distributed.launch --nproc_per_node=4 \
train_bart.py \
  --model_name_or_path "fnlp/bart-base-chinese" \
  --data_root ${DATA_DIR} \
  --output_dir ${OUTPUT_DIR} \
  --max_source_length 512 \
  --max_target_length 64 \
  --num_beams 5 \
  --preprocessing_num_workers 8 \
  --save_total_limit 1 \
  --report_to "none" \
  --num_train_epochs 10 \
  --save_strategy "epoch" \
  --evaluation_strategy "epoch" --generation_num_beams 5 \
  --do_train --do_eval \
  --predict_with_generate \
  --per_device_train_batch_size 16 --per_device_eval_batch_size 16
