def entityResp(entities):
    resp=""
    for x in entities:
        if 'greetings'==x[0]:    
            resp+="hi this is bot\n"
    for x in entities:
        if 'Username'==x[0]:
            resp+="nice to meet you "+x[1]+"\n"
    for x in entities:
        if 'UserLocation'==x[0]:
            resp+=str(x[1])+" looks like a wonderful place"+"\n"
    if(resp==""):
        resp+="great to hear that, tell me more about yourself"
    else:
        resp+="tell me more"
    return(resp)


'''
entities=witfunc(message_text)
print(entityResp(entities))
'''
