from fastapi import FastAPI
from langchain_community.llms.ollama import Ollama
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

PROMPT = """
You are an AI assistant for proofreading business emails.
Based on the context, please proofread and edit the following reply to the given email body:
Body:
{message}
Reply:
{reply}
Constraints:
- Only proofread and edit the reply
"""


@app.get("/")
def read_root():
    return {"Hello": "World"}


class FormatEmailRequest(BaseModel):
    message: str
    reply: str


class FormatEmailResponse(BaseModel):
    corrected_reply: str


@app.post("/format_email")
def format_mail(request: FormatEmailRequest) -> FormatEmailResponse:
    # プロンプトテンプレート
    prompt_template = PromptTemplate.from_template(PROMPT)

    # LLM
    llm = Ollama(model="phi3")

    # 出力パーサー
    parser = StrOutputParser()

    # チェーンの作成
    chain = prompt_template | llm | parser

    # チェーンの実行
    res = chain.invoke({"message": request.message, "reply": request.reply})

    # レスポンスの返却
    return FormatEmailResponse(corrected_reply=res)
