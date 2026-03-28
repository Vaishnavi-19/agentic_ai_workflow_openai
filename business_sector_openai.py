import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
    
# And now - the all important import statement
# If you get an import error - head over to troubleshooting in the Setup folder
# Even for other LLM providers like Gemini, you still use this OpenAI import - see Guide 9 for why

from openai import OpenAI
# And now we'll create an instance of the OpenAI class
# If you're not sure what it means to create an instance of a class - head over to the guides folder (guide 6)!
# If you get a NameError - head over to the guides folder (guide 6)to learn about NameErrors - always instantly fixable
# If you're not using OpenAI, you just need to slightly modify this - precise instructions are in the AI APIs guide (guide 9)

openai = OpenAI()
messages = [{"role": "user", "content": "Please pick a business area that might be worth exploring for an agentic AI opportunity. Respond only with the business area."}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print(response.choices[0].message.content)

messages = [{"role": "user", "content": "present a pain-point in that industry - something challenging that might be ripe for an Agentic solution."}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print(response.choices[0].message.content)

messages = [{"role": "user", "content": "Propose the Agentic AI solution"}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print(response.choices[0].message.content)