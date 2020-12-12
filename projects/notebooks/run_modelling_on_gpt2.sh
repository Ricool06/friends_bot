python ./transformers/examples/language-modeling/run_clm.py \
  --model_name_or_path gpt2 \
  --train_file ./src/train.txt \
  --validation_file ./src/validation.txt \
  --do_train \
  --do_eval \
  --output_dir /tmp/test-clm
