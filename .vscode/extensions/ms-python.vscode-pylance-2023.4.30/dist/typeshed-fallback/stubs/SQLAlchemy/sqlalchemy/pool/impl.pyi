from typing import Any

from ..util import memoized_property
from .base import Pool

class QueuePool(Pool):
    def __init__(
        self, creator, pool_size: int = 5, max_overflow: int = 10, timeout: float = 30.0, use_lifo: bool = False, **kw
    ) -> None: ...
    def recreate(self): ...
    def dispose(self) -> None: ...
    def status(self): ...
    def size(self): ...
    def timeout(self): ...
    def checkedin(self): ...
    def overflow(self): ...
    def checkedout(self): ...

class AsyncAdaptedQueuePool(QueuePool): ...
class FallbackAsyncAdaptedQueuePool(AsyncAdaptedQueuePool): ...

class NullPool(Pool):
    def status(self): ...
    def recreate(self): ...
    def dispose(self) -> None: ...

class SingletonThreadPool(Pool):
    size: Any
    def __init__(self, creator, pool_size: int = 5, **kw) -> None: ...
    def recreate(self): ...
    def dispose(self) -> None: ...
    def status(self): ...
    def connect(self): ...

class StaticPool(Pool):
    @memoized_property
    def connection(self): ...
    def status(self): ...
    def dispose(self) -> None: ...
    def recreate(self): ...

class AssertionPool(Pool):
    def __init__(self, *args, **kw) -> None: ...
    def status(self): ...
    def dispose(self) -> None: ...
    def recreate(self): ...
