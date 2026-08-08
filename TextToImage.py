from monsterapi import client
import requests
import webbrowser

#monster api key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjAyOWRlY2U5NzJhOWM2MzcxZTdjOTM0Y2I3MDUzM2I4IiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDdUMDk6MTI6MDEuNDQ0Nzg3In0.UyNArIOq9joxMe298ff2cuFf8Eiqd5qFfrL1GbQNStw'

#Initializing client
monster_client = client(api_key)

#prompt
prompt = input("Prompt:  ")

#model
model = 'txt2img'

#input data
input_data = {
    'prompt': f'{prompt}',
    'negprompt' : 'bad anatomy' ,
    'samples' : 1,
    'steps' : 50,
    'aspect_ratio' : 'square',
    'guidance_scale' : 7.5,
    'seed' : 2414,

}

result = monster_client.generate(model,input_data)

img_url = result['output'][0]

file_name = "Generated_image.png"

#download the image
response = requests.get(img_url)

if response.status_code == 200:
    with open(file_name,'wb') as file:
        file.write(response.content)
    print("Image downloaded")

    #open the image
    webbrowser.open(file_name)

else:
    print("Filed to download")