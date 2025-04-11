from openai import AsyncOpenAI

client = AsyncOpenAI()

async def getGPTSummary(prompt):
    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": '''You are an expert Dungeons and Dragons backstory creator that specializes in OSR character design.
                The following information details the pivotal moments generated during character creation. During childhood the
                lowest score you can get is a +1 and the highest a +6 with a +3 indicating an average ability. The final results can 
                range from 3 at worst to 18 at best with a 10 indicating an average ability but don't mention the actual numbers. 
                Take each piece of the inputed backstory and connect them together to construct a cohesive tapestry of the character. 
                For each backstory segment, give an in-backstory justification for how each event led into the next, especially for 
                adolesence and adulthood. Where there is vagueness or a lack of detail in a backstory element, make it concrete with 
                a specific in-setting example, ensuring that it would make sense in a DnD OSR setting. Finally, your output 
                should be less than 2000 characters and don't give the character a name.'''
            },
            {
                "role": "user", 
                "content": "Create a backstory using the following elements from the character generation process as inspiration: " + prompt
            }
        ]
    )

    return completion.choices[0].message.content