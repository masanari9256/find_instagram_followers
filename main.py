import instaloader

# ログインに必要な情報(str)
INSTAGRAM_ID = ""
INSTAGRAM_PASSWORD = ""

# フォロワーを取得したいアカウントのID(str)
TARGET_ACCOUNT_ID = ""

# インスタグラムにログイン
loader = instaloader.Instaloader()
loader.login(INSTAGRAM_ID, INSTAGRAM_PASSWORD)

# 指定したIDのprofileオブジェクトを作成
profile = instaloader.Profile.from_username(loader.context, TARGET_ACCOUNT_ID)

# 指定したIDのフォロワーを全件取得
followers = profile.get_followers()

# ユーザーIDを出力する
f = open('follower.txt', 'w')
print("フォロワーを書き込み中です")

for follower in followers:
    # print(follower.username)
    f.write(follower.username)
    f.write('\n')

f.close()
