import hashlib
def Sha(text):
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    sha = hashlib.sha1(text)
    encrypts = sha.hexdigest()
    return encrypts

if __name__ =="__main__":
    sha_data = Sha("hangzhou")
    print("加密前:"+str("hangzhou"))
    print("加密后:"+str(sha_data))

# 加密前:hangzhou
# 加密后:46ac39e9fb84ca9cef05dece1a6abc12fbd88e7a