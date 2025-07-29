# 準備

---

### 1. 仮想環境の準備

#### Windows

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force  # はじめの一度だけ実行する
python -m venv .venv
.venv\Scripts\activate
```

#### MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```
<br>

### 2. requirements.txt をインポートする

```bash
pip install -r requirements.txt
```
<br>

# BeEngineer-typing

---

## 🚀 ファイル実行

### 1. sample.py の実行

```bash
python sample.py
```
<br>

実行すると以下のURLが開きます：
https://www.google.com/?hl=ja

<br>

### 2. auto_been_typing.py の実行

```bash
python auto_been_typing.py
```
実行すると以下のURLが開きます：
https://typing.be-engineer.tech

<br>

タイピングが自動で動作します。
<br>

🛠 藤原が改造し、永遠にランダムに項目を選択し、自動タイピングが動作する仕様です。

<br>

## ❌ 終了方法

### 1. ブラウザを閉じる
### 2. ターミナルで終了コマンドを入力
#### Windows

```bash
Ctrl + C
```

#### MacOS
```bash
Command + C
```

<br>

# イータイピング｜e-typing

---

## 🚀 ファイル実行
```
python auto_etyping.py
```
**初期状態**  
１回実行可能  

<br>

**無限タイピング状態**  
`While True:` をコメント化解除することで実行可能！  
※詳細はコードのコメントアウトを確認する

<br>

## ❌ 終了方法

### 1. ブラウザを閉じる
### 2. ターミナルで終了コマンドを入力
#### Windows

```bash
Ctrl + C
```

#### MacOS
```bash
Command + C
```

<br>
