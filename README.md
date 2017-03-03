# physics_music

## Usage

```bash
python train.py --help
```

```
usage: train.py [-h] [--dropout DROPOUT] [--hidden_dim HIDDEN_DIM]
                [--input_file INPUT_FILE] [--nb_epoch NB_EPOCH]
                [--optimizer OPTIMIZER] [--output_dir OUTPUT_DIR] [--resume]
                [--seq_length SEQ_LENGTH] [--seq_stride SEQ_STRIDE]
                [--val_split VAL_SPLIT]

optional arguments:
  -h, --help            show this help message and exit
  --dropout DROPOUT     dropout fraction (default: 0.2)
  --hidden_dim HIDDEN_DIM
                        hidden layer dimension (default: 75)
  --input_file INPUT_FILE
                        path to the input file (default: data/input.txt)
  --nb_epoch NB_EPOCH   number of epochs (default: 1)
  --optimizer OPTIMIZER
                        name of the optimizer (default: rmsprop)
  --output_dir OUTPUT_DIR
                        output directory (default: test_output)
  --resume              resume from saved model (default: False)
  --seq_length SEQ_LENGTH
                        sequence length (default: 30)
  --seq_stride SEQ_STRIDE
                        sequence stride (default: 0)
  --val_split VAL_SPLIT
                        fraction of the validation data (default: 0.2)
```

## Example

To train a new model

```bash
python train.py --hidden_dim=75 --dropout=0.2 --optimizer=rmsprop --output_dir model-75-0.2-rmsprop --nb_epoch=5
```

To resume from a saved model

```bash
python train.py --hidden_dim=75 --dropout=0.2 --optimizer=rmsprop --output_dir model-75-0.2-rmsprop --nb_epoch=5 --resume
```
