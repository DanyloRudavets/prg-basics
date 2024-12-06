
def email_sender(file):
    import re
    file='email.txt'
    with open(file, 'r')as file:
        content=file.read()
    c=content.split()
    for i in c:
        sender_patern='^j'
        g=re.search(sender_patern,i)
        if g:

            s=i
    return s
def email_recipient(file):
    import re
    file='email.txt'
    with open(file, 'r')as file:
        content=file.read()
    c=content.split()
    for i in c:
        sender_patern='^<a'
        g=re.search(sender_patern,i)
        if g:

            r=i
    return r[1:-1]
def email_subject(file):
    import re
    file='email.txt'
    with open(file, 'r')as file:
        content=file.read()

    c=content.split()
    for i in c:
        sender_patern='^R\w+'
        g=re.search(sender_patern,i)
        patern='^r\w+'
        k=re.search(patern,i)
        if g:

            r=i
        if k:
            q=i
        
    return r+' '+q[:-1]

def email_body(file):
    import re
    with open(file, 'r')as file:
        content=file.read()
    c=content.split()
    for i in c:
        pat='^I'
        g=re.match(pat,i)
        if g:
            k=c.index(i)
    for i in c:
        pat='^ye'
        g=re.match(pat,i)
        if g:
            j=c.index(i)
    return str(c[k:j+1])
    

if __name__=='__main__':
    print(email_sender('email.txt'))
    print(email_recipient('email.txt'))
    print(email_subject('email.txt'))
    print(email_body('email.txt'))



        