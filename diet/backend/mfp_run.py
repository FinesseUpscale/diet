import mfp
import mfp_helpers

# username = input('username: ')
# password = input('password: ')

username = 'edwardsapp@gmail.com'
password = '339273'

mfp = mfp.MFP(username, password)
mfp.login()