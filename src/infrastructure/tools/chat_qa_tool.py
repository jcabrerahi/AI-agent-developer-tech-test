from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from src.application.prompts.chat_prompts import chat_prompt
from src.infrastructure.llm.openai_wrapper import ChatOpenAIWrapper


class ChatQAToolInput(BaseModel):
    context: str = Field(..., description="The context to answer the question")
    question: str = Field(..., description="The question to answer")
    messages: str = Field(..., description="The historic chat")


class ChatQATool(BaseTool):
    name: str = "ChatQATool"
    description: str = "Useful to answer user inputs"
    args_schema: type[BaseModel] = ChatQAToolInput
    return_direct: bool = True
    api_wrapper: ChatOpenAIWrapper = Field(default_factory=ChatOpenAIWrapper)

    def _run(
        self,
        context: str,
        question: str,
        messages: str,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> str:
        """Use the tool."""
        parser = StrOutputParser()
        prompt = PromptTemplate(
            template=chat_prompt,
            input_variables=["context", "question", "messages"],
        )
        return self.api_wrapper.get_response(
            prompt=prompt,
            input_values={
                "context": context,
                "question": question,
                "messages": messages,
            },
            parser=parser,
        )

    async def _arun(
        self,
        context: str,
        question: str,
        messages: str,
        run_manager: AsyncCallbackManagerForToolRun | None = None,
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(
            context=context,
            question=question,
            messages=messages,
            run_manager=run_manager.get_sync(),
        )
