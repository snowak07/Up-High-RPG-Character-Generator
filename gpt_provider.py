from openai import OpenAI
import api_key_provider

client = OpenAI(
  api_key=api_key_provider.API_KEY
)

def getGPTSummary(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": "Summarize the backstory of the following character: " + prompt}
        ]
    )