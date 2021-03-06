# coding:utf-8

import sys
from pathlib import Path
PROJECT_PATH = Path(__file__).absolute().parent
sys.path.insert(0, str(PROJECT_PATH))

from utils.log import log_info as _info
from utils.log import log_error as _error

RNN_ENCODER_TYPE_UNI = 'uni'
RNN_ENCODER_TYPE_BI = 'bi'

RNN_UNIT_TYPE_LSTM = 'lstm'
RNN_UNIT_TYPE_GRU = 'gru'
RNN_UNIT_TYPE_LAYER_NORM_LSTM = 'layer_norm_lstm'

SOS_ID = 1
EOS_ID = 2
PADDING_ID = 3

BATCH_SIZE = 32
TRIAN_STEPS = 100000
QUE_PATH = PROJECT_PATH / 'data/question.data'
ANS_PATH = PROJECT_PATH / 'data/answer.data'

DATA_PATH = PROJECT_PATH / 'data/all.data'
DIST_PATH = PROJECT_PATH / 'data/vocab_idx.bin'

def forbid_new_attributes(wrapped_setatrr):
    def __setattr__(self, name, value):
        if hasattr(self, name):
            wrapped_setatrr(self, name, value)
        else:
            _error('Add new {} is forbidden'.format(name))
            raise AttributeError
    return __setattr__

class NoNewAttrs(object):
    """forbid to add new attributes"""
    __setattr__ = forbid_new_attributes(object.__setattr__)
    class __metaclass__(type):
        __setattr__ = forbid_new_attributes(type.__setattr__)

class NmtConfig(NoNewAttrs):
        # Encoder
        vocab_size = 10509
        embedding_size = 160
        num_layers = 2
        hidden_size = 320
        forget_bias = 1.0
        dropout = 0.2
        residual_or_not = True  

        kernel_size = [1, 2, 3]
        pool_size = [640, 639, 637]

        # Decoder
        tgt_vocab_size = 10509 
        max_len_infer = 50

        encoder_type = RNN_ENCODER_TYPE_BI
        unit_type = RNN_UNIT_TYPE_GRU

        # global
        model_dir = 'models/'
        initializer_range = 0.02
        learning_rate = 1e-4
        lr_limit = 1e-4
        colocate_gradients_with_ops = True

nmt_config = NmtConfig()
  