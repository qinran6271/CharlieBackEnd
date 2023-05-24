from cryptography.fernet import Fernet
import config
import base64

def encrypt_url(url, key):
    cipher_suite = Fernet(key)
    encrypted_url = cipher_suite.encrypt(url.encode()).decode()
    return encrypted_url

# 生成一个32字节长的密钥
key = Fernet.generate_key()

# 对密钥进行URL安全的Base64编码
base64_key = base64.urlsafe_b64encode(key)

# 将密钥转换为字符串形式
key_str = base64_key.decode()

# 将密钥存储在配置文件中
config.ENCRYPTION_KEY = key_str

# 加密MongoDB URL
encrypted_url = encrypt_url('mongodb+srv://qinran6271:vlq7DZ312Zb4oGv5@charlietest.jcnj1mr.mongodb.net/?retryWrites=true&w=majority', config.ENCRYPTION_KEY)

# 将加密后的URL存储在配置文件中
config.ENCRYPTED_MONGODB_URL = encrypted_url
