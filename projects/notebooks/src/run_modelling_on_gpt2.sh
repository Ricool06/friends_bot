# THIS SCRIPT IS MORE OF A ROUGH GUIDE. IT MAY NOT WORK BY JUST RUNNNING IT
# You may have to deactivate python env and use global install of transformers & datasets before running this

git clone https://github.com/huggingface/transformers.git

cd transformers
git checkout 5e637e6c690e45d13ebf7296e1ea9dcc188d0f07

cd examples/language-modeling

CUDA_VISIBLE_DEVICES=0 python run_clm.py \
  --model_name_or_path gpt2 \
  --train_file ../../../train.txt \
  --validation_file ../../../validation.txt \
  --do_train \
  --do_eval \
  --per_device_train_batch_size=1 \
  --per_device_eval_batch_size=1 \
  --output_dir ../../../test-clm
  # --dataset_name wikitext \
  # --dataset_config_name wikitext-2-raw-v1 \
