import os, sys
from utils import witfunc
from responce import entityResp
from flask import Flask,request,render_template
from pymessenger import Bot


app=Flask(__name__)

PAGE_ACCESS_TOKEN= "SomeConfindetialAccessToken" #confidential
bot=Bot(PAGE_ACCESS_TOKEN)

@app.route('/',methods=['GET'])
def verify():
    #webhook verification
    if request.args.get('hub.mode')=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "verification code mismatch",403
        return request.args['hub.challenge'],200
    return render_template('index.html')

@app.route('/',methods=['POST'])
def webhook():
    data=request.get_json()
    log(data)

    if data['object']=='page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                #IDS
                sender_id=messaging_event['sender']['id']
                recipient_id=messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text=messaging_event['message']['text']
                    else:
                        messaging_text='no text'

                    # entities=witfunc(messaging_text)
                    # response=str(entityResp(entities))

                    # '''
                    #echo
                    response=messaging_text
                    # '''

                    bot.send_text_message(sender_id,response)

    return "ok",200




def log(message):
    print(message)
    sys.stdout.flush()


if __name__=='__main__':
    app.run(debug=True,port=5000)
