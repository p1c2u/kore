from blinker import Namespace

__all__ = ['container_prepared', ]

_signals = Namespace()

container_prepared = _signals.signal('container_prepared')
