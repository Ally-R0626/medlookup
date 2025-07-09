# 💊 医薬品名検索アプリ（一般名⇔製品名）

Streamlitを使用して作成した、医薬品の「一般名」と「製品名」の対応を検索できるWebアプリです。

## 🧩 特徴

- 一般名・製品名のいずれかを入力すると、該当する名称を表示します
- CSVファイルから医薬品データを読み込み、部分一致検索が可能です
- StreamlitによるシンプルなUI設計で、誰でも簡単に使えます

## 🖥️ 使用技術

- Python 3.x
- pandas
- Streamlit

## 🚀 使い方（ローカル環境）

1. このリポジトリをクローンまたはダウンロードします  
2. `med_list.csv` を同じディレクトリに用意します（「一般名」「製品名」の2列を含むCSV）  
3. 以下のコマンドでアプリを起動します：

```bash
streamlit run streamlit_medlookup.py

📁 medlookup/
├── streamlit_medlookup.py             # Streamlit アプリ本体
├── med_list.csv     		  # 医薬品データ（一般名・製品名）
└── README.md       		　　　    # このファイル
└── LICENSE       		　　　    # MITライセンスです

アプリを動かせるデモはこちら👇
🔗 https://medlookup-3x2fyya62zswyrrbiz9763.streamlit.app/


