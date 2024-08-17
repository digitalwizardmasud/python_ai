from langchain_openai import ChatOpenAI
from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field

llm = ChatOpenAI(model="gpt-4o-mini")

# Pydantic
class Joke(BaseModel):
    """Generate a summary"""
    summary: str = Field(description="The summary of the context")
    joke: str = Field(description="Generate a joke from the context")
    question: str = Field(description="Provide a question about context")
    answer: str = Field(description="Include answer of the question")
    rating: Optional[int] = Field(
        default=None, description="How perfect the joke is, from 1 to 10"
    )


structured_llm = llm.with_structured_output(Joke)

result = structured_llm.invoke(
    """
    My Golden Bengal, I love you
Forever your skies, your air set my heart in tune as if it were a flute.In spring, O mother mine, the fragrance from your mango groves makes me wild with joy!
Ah, what a thrill!In autumn, O mother mine,
In the full-blossomed paddy fields, I have seen spread all over-sweet smiles!Ah, what a beauty, what shades, what an affection and what a tenderness!What a quilt have you spread at the feet of banyan trees and along the banks of rivers!Oh mother mine, words from your lips are like nectar to my ears!
Ah, what a thrill!If sadness, Oh mother mine, casts a gloom on your face,
My eyes are filled with tears!
    """
)
print(result)