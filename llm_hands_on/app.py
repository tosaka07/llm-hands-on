from fastapi import FastAPI
from langchain_community.llms.ollama import Ollama
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class FormatEmailRequest(BaseModel):
    message: str


class FormatEmailResponse(BaseModel):
    message: str


@app.post("/format_email")
def format_mail(request: FormatEmailRequest) -> FormatEmailResponse:
    # システムプロンプト
    system_template = (
        "Please revise the following sentences into correct business e-mail text:"
    )

    # システムプロンプト
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    # LLM
    llm = Ollama(model="phi3")

    # 出力パーサー
    parser = StrOutputParser()

    # チェーンの作成
    chain = prompt_template | llm | parser

    # チェーンの実行
    res = chain.invoke({"text": request.message})

    # レスポンスの返却
    return FormatEmailResponse(message=res)
