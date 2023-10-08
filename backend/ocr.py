import easyocr
import openai

openai.api_key = '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'

reader = easyocr.Reader(['en']) 
result = reader.readtext('linear algebra.png', detail = 0)
text = " ".join(result)

prompt = "Given this text, return whether it is related or not to linear algebra. Only return yes or no. Do not return anything else other than yes or no."

response = openai.Completion.create(engine='',
                                    prompt=prompt,
                                    max_tokens=1024,
                                    temperature=0,
                                    top_p=1,
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0,
                                    stop=['#'])['choices'][0]['text']

print(response)


