from typing import Any, Optional

from django.db.models import Aggregate
from django.db.models.fields import Field

class GeoAggregate(Aggregate):
    function: Any = ...
    is_extent: bool = ...
    @property
    def output_field(self) -> Field[Any, Any]: ...
    def as_sql(
        self,
        compiler: Any,
        connection: Any,
        function: Optional[Any] = ...,
        **extra_context: Any
    ) -> Any: ...
    def as_oracle(
        self, compiler: Any, connection: Any, **extra_context: Any
    ) -> Any: ...
    def resolve_expression(
        self,
        query: Optional[Any] = ...,
        allow_joins: bool = ...,
        reuse: Optional[Any] = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> Any: ...

class Collect(GeoAggregate):
    name: str = ...
    output_field_class: Any = ...

class Extent(GeoAggregate):
    name: str = ...
    def __init__(self, expression: Any, **extra: Any) -> None: ...

class Extent3D(GeoAggregate):
    name: str = ...
    def __init__(self, expression: Any, **extra: Any) -> None: ...

class MakeLine(GeoAggregate):
    name: str = ...
    output_field_class: Any = ...

class Union(GeoAggregate):
    name: str = ...
    output_field_class: Any = ...
