from itsdangerous import URLSafeTimedSerializer
from system import Config
serializer =  URLSafeTimedSerializer(Config.SECRET_KEY)
def serialise_token(**kwargs):
    return serializer.dumps(kwargs)

def deserialise_token(token):
    time = 60 * 60 #1 hour
    try:
        return serializer.loads(token,max_age=time)
    except:
        print(serializer.loads(token,max_age=time))
        return None

