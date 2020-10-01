import transformers

DEVICE = "cuda"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "/home/self-made-lol/Desktop/IMDB/input/bert_base_uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE = "/home/self-made-lol/Desktop/IMDB/input/train.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
