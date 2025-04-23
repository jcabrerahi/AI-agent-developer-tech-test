from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.utils import get_from_dict_or_env
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, ConfigDict, SecretStr, model_validator


class ChatOpenAIWrapper(BaseModel):
    """Wrapper for ChatOpenAI with template support."""

    openai_api_key: SecretStr
    model_name: str

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def validate_environment(cls, values: dict) -> dict:
        values["openai_api_key"] = get_from_dict_or_env(values, "openai_api_key", "OPENAI_API_KEY")
        values["model_name"] = get_from_dict_or_env(values, "model_name", "LLM_MODEL_NAME")
        return values

    def get_response(self, prompt: PromptTemplate, input_values: dict, parser: BaseOutputParser) -> any:
        """Get response from ChatOpenAI using the formatted template."""

        model = ChatOpenAI(
            api_key=self.openai_api_key.get_secret_value(),
            model_name=self.model_name,
            temperature=0,
            request_timeout=12,
            max_retries=2,
        )
        chain = prompt | model | parser
        return chain.invoke(input_values)
