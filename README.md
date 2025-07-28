# auto_typing_verFuji

# イータイピング｜e-typing
ターミナル上で  
`git clone https://github.com/keigo-fujiwara/auto_typing_verFuji.git`  
を実行する  

仮想環境を構築し、入る  

**macOS**  
`python3 -m venv .venv`  
`source .venv/bin/activate`  

**Windows**  
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force  # はじめの一度だけ実行する`  
`python -m venv .venv`  
`.venv\Scripts\Activate.ps1`  

requirements.txt に記述されたモジュールのインストール  
`pip install -r requirements.txt`  

**初期状態**  
１回実行可能  

**無限タイピング状態**  
`While True:` をコメント化解除することで実行可能！  
※詳細はコードのコメントアウトを確認する  
