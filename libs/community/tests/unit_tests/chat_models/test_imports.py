from langchain_community.chat_models import __all__, _module_lookup

EXPECTED_ALL = [
    "AzureChatOpenAI",
    "BedrockChat",
    "ChatAnthropic",
    "ChatAnyscale",
    "ChatBaichuan",
    "ChatCohere",
    "ChatCoze",
    "ChatDatabricks",
    "ChatDeepInfra",
    "ChatEverlyAI",
    "ChatEdenAI",
    "ChatFireworks",
    "ChatFriendli",
    "ChatGooglePalm",
    "ChatHuggingFace",
    "ChatHunyuan",
    "ChatJavelinAIGateway",
    "ChatKinetica",
    "ChatKonko",
    "ChatLiteLLM",
    "ChatLiteLLMRouter",
    "ChatLlamaCpp",
    "ChatMLflowAIGateway",
    "ChatMaritalk",
    "ChatMlflow",
    "ChatMLflowAIGateway",
    "ChatMLX",
    "ChatNebula",
    "ChatOCIGenAI",
    "ChatOllama",
    "ChatOpenAI",
    "ChatPerplexity",
    "ChatPremAI",
    "ChatSambaNovaCloud",
    "ChatSambaStudio",
    "ChatSparkLLM",
    "ChatTongyi",
    "ChatVertexAI",
    "ChatYandexGPT",
    "ChatYuan2",
    "ChatZhipuAI",
    "ErnieBotChat",
    "FakeListChatModel",
    "GPTRouter",
    "GigaChat",
    "HumanInputChatModel",
    "JinaChat",
    "LlamaEdgeChatService",
    "MiniMaxChat",
    "MoonshotChat",
    "PaiEasChatEndpoint",
    "PromptLayerChatOpenAI",
    "SolarChat",
    "QianfanChatEndpoint",
    "VolcEngineMaasChat",
    "ChatOctoAI",
    "ChatSnowflakeCortex",
    "ChatYi",
    "ChatCogCache",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
    assert set(__all__) == set(_module_lookup.keys())
