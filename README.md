# FastAPI MSOffice Sample

## 概要
FastAPI MSOffice サンプル

- Excelファイル出力のサンプル
- Wordファイル出力のサンプル
- ログ出力は左記を利用 [01.FastApi-Logging](https://github.com/eiji-azakami/01.FastApi-Logging)

## 起動方法

pythonコマンドは環境によって「python3」だったり、「python」、「py」だったりするようです。<br>
お使いの環境に合わせてコマンドを変更してください。

```bash
python3 -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd.exe)
venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload --no-access-log
```

## 起動後
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc:        http://127.0.0.1:8000/redoc

## テスト

今回テストは作っていません。

# Note
 
業務システムでは、よくExcel出力やWord出力のご要望をいただきます。<br>
Pythonでの本当に簡単なものですが、出力サンプルです。<br>
AIに作ってもらったので、３時間ほどで完成しました。

# Author
 
* 作成者 阿座上 英治
* 所属 　株式会社Ｌ．Ｓ．Ｅ
 
## 📝 License

MIT License  
Copyright (c) 2026 L.S.E Eiji.Azakami

This project is licensed under the MIT License.  
See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.
