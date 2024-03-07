from openai import OpenAI
import openai
# Not Working
#openai.api_key = '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'
client = OpenAI(api_key='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'
)
#client.api_key= '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'
response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,

)

image_url = response.data[0].url