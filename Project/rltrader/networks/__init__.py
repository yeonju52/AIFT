import os

if os.environ.get('RLTRADER_BACKEND', 'pytorch') == 'pytorch':
    from rltrader.networks.networks_pytorch import Network, DNN, LSTMNetwork, CNN

__all__ = [
    'Network', 'DNN', 'LSTMNetwork', 'CNN'
]