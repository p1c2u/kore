from blinker import Namespace

__all__ = ['pre_register', 'post_register']

_signals = Namespace()

pre_register = _signals.signal('pre_register')
post_register = _signals.signal('post_register')
