
import os
import openai
from flask import Flask, request,Response
import json
from flask_cors import CORS



#temporary api-key. will be delete in the futre
openai.api_key = "enter openai api key"


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET', 'POST'])
def s():
    
  
      

    word=request.data.decode('utf-8') 

    print(word)


    response=""
    template='''{
      "Summary": "",
      "Terms of Use and Purpose": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "License Type": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "License Duration": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Restrictions": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Privacy and Data Collection": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Updates and Support": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Warranties and Disclaimers": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Liabilities and Indemnities": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Termination": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Payment and Billing": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "User Obligations": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Dispute Resolution and Jurisdiction": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Changes to Terms": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Additional Requirements": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Readability and Clarity": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Consent": {
        "Advantage": "",
        "Disadvantage": ""
      },
      "Documentation": {
        "Advantage": "",
        "Disadvantage": ""
      }
    }'''




    def api():
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {
              "role": "user",
              "content": f"""Please provide the advantages and disadvantages of the 
              following user agreement' {word} '  """
            }
          ],
          temperature=1,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return response
      

    response=api()  
    
    word2=response['choices'][0]['message']['content']

    while response['choices'][0]['finish_reason']=="length":
          #print(response['choices'][0]['message']['content'])
        
          
          response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {
              "role": "user",
              "content": f"""Please provide the advantages and disadvantages of the 
              following user agreement and contiunu where you stop' {word} '  """
            },
            
            {"role":"system","content":f"{word2} "},{"role":"user","content":"continue"}
            
          ],
          temperature=1,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
          word2=word2+response['choices'][0]['message']['content']


    
    print(word2)

    json_data = json.dumps(word2, indent=4)  # Format the JSON with line breaks and indentation
    return Response(json_data, content_type='application/json')
  



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

