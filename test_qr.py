from qrencode import Encoder
import time

enc = Encoder()
t  = time.time()
for x in range(10000):
    im = enc.encode('3502110032014120000010311045116ypR201603302bd', width=200, version=1, border=8)
    im.save('out.png')
print time.time() - t
