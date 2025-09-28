import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from common import common

TOP_K = int(os.getenv("TOP_K") or 10)
GPT_MODEL = os.getenv("GPT_MODEL") or "gpt-5-nano"

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def search_prompt(question):
    store = common()
    results = store.similarity_search_with_score(question, k=TOP_K)
    llm = ChatOpenAI(model=GPT_MODEL)
    context = "".join([doc.page_content for doc, _ in results])
    prompt = PROMPT_TEMPLATE.format(contexto=context, pergunta=question)
    response = llm.invoke(prompt)
    return response.content.strip()
