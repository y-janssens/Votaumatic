import requests
import shutil

i = 1

while i <= 64999:
    i += 1
    print(i)
    root = 'https://www.root-top.com/include/captcha_vote/captcha.php?1638718615.png'
    r = requests.get(root, stream=True)
    if r.status_code == 200:
        with open(f"./database/img{i}.png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    if i == 64999:
        print('Over')
