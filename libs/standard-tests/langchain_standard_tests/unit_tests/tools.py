import os
from abc import abstractmethod
from typing import Callable, Tuple, Type, Union
from unittest import mock

import pytest
from langchain_core.tools import BaseTool
from pydantic import SecretStr

from langchain_standard_tests.base import BaseStandardTests


class ToolsTests(BaseStandardTests):
    @property
    @abstractmethod
    def tool_constructor(self) -> Union[Type[BaseTool], Callable]:
        ...

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        """
        Returns a dictionary representing the "args" of an example tool call.

        This should NOT be a ToolCall dict - i.e. it should not
        have {"name", "id", "args"} keys.
        """
        return {}

    @pytest.fixture
    def tool(self) -> BaseTool:
        return self.tool_constructor(**self.tool_constructor_params)


class ToolsUnitTests(ToolsTests):
    def test_init(self) -> None:
        tool = self.tool_constructor(**self.tool_constructor_params)
        assert tool is not None

    @property
    def init_from_env_params(self) -> Tuple[dict, dict, dict]:
        """Return env vars, init args, and expected instance attrs for initializing
        from env vars."""
        return {}, {}, {}

    def test_init_from_env(self) -> None:
        env_params, tools_params, expected_attrs = self.init_from_env_params
        if env_params:
            with mock.patch.dict(os.environ, env_params):
                tool = self.tool_constructor(**tools_params)
            assert tool is not None
            for k, expected in expected_attrs.items():
                actual = getattr(tool, k)
                if isinstance(actual, SecretStr):
                    actual = actual.get_secret_value()
                assert actual == expected

    def test_has_name(self, tool: BaseTool) -> None:
        assert tool.name

    def test_has_input_schema(self, tool: BaseTool) -> None:
        assert tool.get_input_schema()

    def test_input_schema_matches_invoke_params(self, tool: BaseTool) -> None:
        """
        Tests that the provided example params match the declared input schema
        """
        # this will be a pydantic object
        input_schema = tool.get_input_schema()

        assert input_schema(**self.tool_invoke_params_example)
