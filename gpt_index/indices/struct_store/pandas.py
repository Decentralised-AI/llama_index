"""Pandas csv structured store."""

from typing import Any, Optional, Sequence

from gpt_index.data_structs.node_v2 import Node
from gpt_index.data_structs.table_v2 import PandasStructTable
from gpt_index.indices.struct_store.base import BaseGPTStructStoreIndex

import pandas as pd


class GPTPandasIndex(BaseGPTStructStoreIndex[PandasStructTable]):
    """Base GPT Pandas Index.

    The GPTPandasStructStoreIndex is an index that stores
    a Pandas dataframe under the hood.
    Currently index "construction" is not supported.

    During query time, the user can either specify a raw SQL query
    or a natural language query to retrieve their data.

    Args:
        pandas_df (Optional[pd.DataFrame]): Pandas dataframe to use.
            See :ref:`Ref-Struct-Store` for more details.

    """

    index_struct_cls = PandasStructTable

    def __init__(
        self,
        nodes: Optional[Sequence[Node]] = None,
        df: Optional[pd.DataFrame] = None,
        index_struct: Optional[PandasStructTable] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        if nodes is not None:
            raise ValueError("We currently do not support indexing documents or nodes.")
        self.df = df

        super().__init__(
            nodes=[],
            index_struct=index_struct,
            **kwargs,
        )

    def _build_index_from_nodes(self, nodes: Sequence[Node]) -> PandasStructTable:
        """Build index from documents."""
        index_struct = self.index_struct_cls()
        return index_struct

    def _insert(self, nodes: Sequence[Node], **insert_kwargs: Any) -> None:
        """Insert a document."""
        raise NotImplementedError("We currently do not support inserting documents.")
