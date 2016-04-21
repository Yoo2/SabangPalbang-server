from gcm import *

gcm = GCM("AIzaSyA40ZLuUOg7_hln5FrirysYfTpCCfmHLJ4")
data = {'the_message': 'Test', 'param2' : 'value2'}

reg_id = 'APA91bFoklJk2grvehLXCAHHxWCKMEtXuUPEeg6usM-UGRlnliveYC6Q_q79E1iTHAit01Zs_HzWq2SIKgmem0HAN0RzaikSwg6u0K0Cnau3U6kIY8CJq-s'

gcm.plaintext_request(registration_id=reg_id, data=data)
