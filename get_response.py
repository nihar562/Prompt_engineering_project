import openai
import API_KEY
openai.api_key = API_KEY.api_key

def get_response(prompt,max_tokens = 400):
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=max_tokens,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response["choices"][0]["text"]