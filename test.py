import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 불필요한 에러를 보여주지 않게 하는 os 설정

from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())