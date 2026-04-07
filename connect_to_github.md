在学校电脑上连接github:
git init
git add .
git commit -m "first commit in school"

生成 SSH Key
ssh-keygen -t ed25519 -C "fan.01@163.com"

添加 SSH Key 到 Github

根据代理端口设置git 配置文件
git config --global http.proxy http://127.0.0.1:10809   # 10809需要调整
git config --global https.proxy http://127.0.0.1:10809  # 10809需要调整

添加 Github 远程仓库
git remote set-rul origin git@github.com:FanZhengyun/questions_bank.git

22端口被ban
bash
  notepad ~/.ssh/config
text
  Host github.com
    HostName ssh.github.com
    Port 443
    User git

测试
ssh -T git@github.com
测试成功
Hi FanZhengyun! You've successfully authenticated, but GitHub does not provide shell access.

git branch --set-upstream-to=origin/main
git pull

git checkout -b main origin/main