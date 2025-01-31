from openai import OpenAI
import api_key_provider

client = OpenAI()

def getGPTSummary(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": "You are an expert Dungeons and Dragons backstory creator that specializes in OSR character design."
            },
            {
                "role": "user", 
                "content": "Summarize the backstory of the following character: " + prompt
            }
        ]
    )

    return completion.choices[0].message.content