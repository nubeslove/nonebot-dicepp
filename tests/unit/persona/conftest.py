"""共享测试工具 — mock provider / router 工厂函数"""
from unittest.mock import MagicMock, AsyncMock


def make_mock_provider():
    """创建单个 mock LLM provider，generate 为 AsyncMock。"""
    provider = MagicMock()
    provider.generate = AsyncMock()
    return provider


def make_mock_providers():
    """创建 mock providers dict（用于 LLMRouter 构造）。"""
    provider = MagicMock()
    provider.api_key = "fake"
    provider.base_url = "http://localhost"
    provider.max_concurrent = None
    model = MagicMock()
    model.name = "fake"
    model.category = "llm"
    model.capabilities = ["text", "tool_calls"]
    model.quality = 0.9
    model.cost = 0.5
    model.circuit_breaker = None
    provider.models = [model]
    return {"fake": provider}


def _make_tool_registry():
    """创建含 4 个 life 工具的 ToolRegistry，供测试共用。"""
    from plugins.DicePP.module.persona.tools.registry import ToolRegistry, ToolDomain
    from plugins.DicePP.module.persona.tools.collecting import (
        RECORD_EVENT_TOOL,
        RECORD_REACTION_TOOL,
        RECORD_DIARY_ENTRY_TOOL,
        RECORD_SHARE_MESSAGE_TOOL,
        life_collecting_executor,
    )
    registry = ToolRegistry()
    registry.register(ToolDomain.LIFE, RECORD_EVENT_TOOL, life_collecting_executor)
    registry.register(ToolDomain.LIFE, RECORD_REACTION_TOOL, life_collecting_executor)
    registry.register(ToolDomain.LIFE, RECORD_DIARY_ENTRY_TOOL, life_collecting_executor)
    registry.register(ToolDomain.LIFE, RECORD_SHARE_MESSAGE_TOOL, life_collecting_executor)
    return registry
