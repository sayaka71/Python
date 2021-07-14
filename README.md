<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" alt="Logo" width="150" height="150">
  </a>
  
# Python
Scripts for learning Python, Bash, etc.

## Table of Contents
- [Code](#code)
- [Bash](#bash)
- [Requirements](#requirements)

## Code
### Practice
- [**pra_num.py**](./Practice): アルゴリズム，独学プログラマー，Python入門

### Algorithm
- [**alg_num.py**](./Algorithm): アルゴリズム[Udemy講座](https://www.udemy.com/course/algorithm1/learn/lecture/10674030#overview)


## bash
- `tabキー`: ファイル名やディレクトリ名を補間してくれる
- `$sudo`: (= SuperUserDo)  1番権限のある人の命令。パソコン壊れる危険性ある。パスワード求められる。
- `$mv`: ファイルの移動や，名前変更に使える
- `$cat`: (= Concatenate)ファイルの中身表示する
- `$rm`: ファイルとかディレクトリ (コマンドライン引数`-r`が必要）を消去 (remove) する
- `$cp`: ファイルとかディレクトリ（コマンドライン引数`-r`が必要）コピーできる
```bash
$cp piyo.txt yado.txt #ファイル
$cp -r html new_html #ディレクトリ
```
- `$ls -a`: `-a`がオプション。オプションついてる引数が`True`になる。
- 絶対パス通すのは，[参考サイト](https://qiita.com/nbkn/items/01a11392921119fa0153)を参照で。
- `~/.bash_profile`ファイルの中身に以下を記入する
```bash
export PATH=$PATH:通したいPATH
```
- `$source ~/.bash_profile`: sourceコマンドでファイルを更新
- `echo $PATH`: 環境変数確認

## git
- `$git add <file>`: 変更加える
- `$git commit -m "message"`: commit
- `$git push origin master`: リモートに反映
- `$git pull origin master`: 変更をローカルに反映
- `$git status`: 変更確認

## Requirements
 packages in environment: 
| Name |  Version |
| :---: |  :---:  |
|python|3.7.7|

