import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt #korean natural language
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle

okt= Okt()