
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = """
Suggest exactly 5 healthy breakfast ideas.

Define healthy as balanced, nutrient-dense meals containing
fiber and protein, with limited added sugar and excessive oil.
Include practical breakfast options.

Format requirements:
- Number the ideas from 1 to 5.
- Write exactly one idea per line.
- Do not include a preamble or conclusion.
- Return only the five numbered ideas.
"""

reply = llm.invoke(prompt)

# Print only the text content of the reply.
print(reply.content)