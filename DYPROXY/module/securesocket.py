from DYPROXY.module.password import loadsPassword
from DYPROXY.module.cipher import Cipher

password = "6IG64JLytOpTaGVZ9pezsqIPM4xfRbsrrb61StcnpIh9Kg6xH_OmXRGgZxr1Q9OWDBe3hNUUDcuCKQAgE93rz24QY9ZvSciL39xLME28sMcuq3NRRjGP-16pTySlVVhmiSEtrKf4KEwJGcXKL8A2R22Awjw0W6gGv0Hkh3b-RK55tvfs2--DUne5ydR8_1r8438_LK_pnZTiAmqcmhwYOBsF53AdOpgLO4qRZE6F-mzBYP3N2H5Q7cyOPb2TcqE-AfFWqkB7Od50NUiGax4mNwjO5Qfh0iVhIiPQ-TLDuAN6nhL07pvGn1x4V6Pa2VSZjWmVFdHmdRZCkMQEYgpx8A=="


class SecureSocket():


    def __init__(self):
        self.cipher = self._Cipher()

    def _Cipher(self):
        bytepassword = loadsPassword(password)
        cipher = Cipher.NewCipher(bytepassword)
        return cipher

    def decodeRead(self, bs):
        bs = bytearray(bs)
        self.cipher.decode(bs)

        return bs


    def encodeWrite(self, bs):
        bs = bytearray(bs)
        self.cipher.encode(bs)
        return bs

securesocket = SecureSocket()
# # res = securesocket._Cipher
#
#
#
# ss = b'\x17\x03\x03\x02\xdc\x00\x00\x00\x00\x00\x00\x00\x01\xd4\x96\x0e\x93\xb3\xae<\xd6\xce\x8a\x0f\xd95`E\xd6h\xef\xe7T8~`\x06\xba\x1d\xcc\xaa\xf4\xb6\xe3/\xfe\xf0\xce\xfa|6\xcf\x1f\x1c>\x04\xb9\xb4\xff1#P\x11\x80\xacba\x9c\xf9\x91V\xa4\xec\xa5\x13\xf83\r\xb9\xbeb\xe7\x81\xc4\x8fN"`p\xb2\xa3\x84\xa5D=\xe5rv\x98\xb1W\x853f\x02\xf6#}\xc2\xcd\xf6\x87!]2\x15+\xd3\x12=81\x15\xab\xf61q\xb6\\\xb65\x92t\xc4\x0e\xfc\xf7Z\xb4\xa7\xe4\x1f\xafUqh\x0cC\x05W\xcb\x1bup\xc5\xef\xe8\x81\x19\xda\xa8*2\xec\'\xb4\xa4)\xdff\xd5\xf6\xb5\x12\xb4vJvmB\x07x\xce\xe0\x08\xff\x00\xe4\xe7\xb8w4=\xa4\x878\xa2o\xce\x0c\xcc3H\xfen\x05\x84\x1d\xbaM\x11?\x01up\x8d\xc4\x9c\xea\xf9[\xecy\x8e\xc2\x02\xdei\xda\xe2\xe7\x03\x92\x1a\x87\xa1\x92;\x07xP\xc3Rj\xd66i\x91N\x8f\x8a\xb4\xa4\'\xd4W;\r\xa2\xa1s\xaf\xd7\x93\x8f+\xcbxW\x10<\xed\x95\xd0\xf8\x0f\xb7aua%\xe9Ap5\xdc\x8d%M\x85N#Qshdo\x07I\x9e\xa3\x82\xb3\x81\xd9\x88\xccQ\xd6\xd0\xe7`\x00\xbb\ne@\xb0o3\xf1\x94\x01\xed\xbf\x03\xa4\x04n\x8f\xd0\x88\x06\xe1\x1a\x98j\xff\x89\xe8\xceD)\xfb~]1\x1e\x7f\x82\xb1\'J\x1aN\xdbk\x83+\xa5\xd7\x1d,\xbe\xcaW\xed\xf1(P\xb9&\xfap\x7f\xab`\xed\x96B\xf3\xa8\x98\x1b\x94\x98\xadV\xf6(_\x19\x03X\xe9s[[X\xda\x97:\xf9\x99jn\xd5\x1bn7\xa0\xc7\xa2\x1aIYY\xe1gA\xe3d\xc7U]\x1d\xf9\x7f\xech\x9d\x05J\xad\xbb\x1ea\xed5\xe3\xea\xb4\x02\x9b\xa4\x02\xb7\x9e\xc5\xf2\x1b\x13b\xbb\x9eR\xf1\xec\xc4\x7fgk\xf4\x8f\xdaBt\\\x8bcu\xa9QO\x14Q\xb3J\x9c\xd2\x8f@G\xffb\x08\xb7IM/\x06\xfe\xdb\xc9I\xfb<\x90\x16\x8a\xcay\xce\xcf\xbd.\x88+\xdd\x1f\xf3\x8b\x05E\xb7DZ\xbe\xd0\xa0!1b\x9fMSa\xa5\x0e`\xb2F\xec\xfe\x9b\x95\x98x\xef9\xe8\x0e\x11u\x8e\xbb\xe7\xa7[w\x03i\x06@T\x82\x17\xcbN\xd3\xd5]\xc0\x9d\x03\xbc\x0b0>\xea\xcd"=\xb6\xb4.\x14r\x80\xd0\xf2\xc5\x0f\xd9 \xa3*,\x9f\xe8\xaf\x83WU\xc3\xbb\x81@\xa1\xa66\xdf\xa3w\xdf\xa4\x8av\x05}8\xb4\xd3\xc2\xe9\xb19\xf6\x99\xf4\xbc\xbd\xd9p.\xfbs\x10\xefaM\xb4&\xc4\x9b\xdao?\xbe\x98\xfcL|W\x8a\x12*\xbc&\xec\x85\xb8\xed\x8c\xeej\xe1\xf5\xacK`\x17\xdf\xf4\xd0\x95\xdd\xf1\x90\xc7\x92\x1c\x0f\xfa\x0e\x8a\x99\xad\xb1\x8fX4\x85\x80\xc3\xdfW}{\xabc\x177\x80H\xd9\x81\xf6\xc4\xd0\n|\xa3)K\x9dY\xdb&\x8f\xb7Z\x04B?\xdc+\x9c\xa0\x14\xae\x19#\x15g\x05\x16zq6=x\xa8\x94\xbfx\x18'
# mm = bytearray(ss)
# for i,v in enumerate(mm):
#     print(i,v)
#
# res = securesocket.decodeRead(mm)
#
# for i,v in enumerate(res):
#     print(i,v)
# res = securesocket.encodeWrite(255)
# res = bytearray([0,1,2])
# print(res)
# for i,v in enumerate(res):
#     print(i,v)