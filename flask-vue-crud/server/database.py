from cryptography.fernet import Fernet
import config
import pymongo 
import base64

def encrypt_url(url, key):
    cipher_suite = Fernet(key)
    encrypted_url = cipher_suite.encrypt(url.encode()).decode()
    return encrypted_url

# 生成一个32字节长的随机密钥
key = Fernet.generate_key()

config.ENCRYPTION_KEY = key

# 加密MongoDB URL
encrypted_url = encrypt_url(config.ENCRYPTED_MONGODB_URL, config.ENCRYPTION_KEY)

# 将加密后的URL存储在配置文件中
config.ENCRYPTED_MONGODB_URL = encrypted_url


def decrypt_url(encrypted_url, key):
    cipher_suite = Fernet(key)
    decrypted_url = cipher_suite.decrypt(encrypted_url.encode()).decode()
 
    return decrypted_url

decrypted_url = decrypt_url(config.ENCRYPTED_MONGODB_URL, config.ENCRYPTION_KEY)


# 使用解密后的URL建立数据库连接
client = pymongo.MongoClient(decrypted_url)

# 连接到数据库
# db = client.hi
# collection = db.hey
db = client.CharlieDB
truth_dare = db.truth_or_dare
chapters = db.day_and_night_chaps
sub_chapters = db.day_and_night_subchaps
weaving = db.dream_weaving
furniture = db.furniture
guzi = db.merch
memories_album = db.memories_album
rewinddb = db.rewind
lingering = db.volume
trackdb = db.track
profiledb = db.profile_detail
chat_calls = db.chat_calls
chat_overview = db.chat_overview
chat_details= db.chat_details
moments_details = db.moments_details
moments_overview = db.moments_overview
vinyl_collection = db.vinyl
characters_collection = db.characters
talk_coll = db.talk
details = db.charlie_details
film_cards_coll = db.film_cards
film_chaps_coll = db.film_chaps