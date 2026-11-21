# entities/memo.py
# 【エンティティ層】
# アプリの中心となる「メモ」というデータと、そのビジネスルールを定義する層。
# 他のどの層にも依存しない（DBや画面のことは一切知らない）のがポイント。

from dataclasses import dataclass  # __init__ などを自動生成してくれるデコレーター
from datetime import datetime      # 作成日時を扱うための型

@dataclass
class Memo:
   """メモを表すクラス（エンティティ）"""
   id: str               # メモを一意に識別するID（UUID文字列）
   title: str            # メモのタイトル
   content: str          # メモの本文
   created_at: datetime  # メモの作成日時

   def is_valid(self) -> bool:
       """タイトルが空でないかを確認するビジネスルール"""
       # strip() で前後の空白を取り除き、1文字以上残っていれば有効とみなす
       # （空白だけのタイトルも「空」として扱う）
       return len(self.title.strip()) > 0
