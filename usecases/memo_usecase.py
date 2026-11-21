# usecases/memo_usecase.py
# 【ユースケース層】
# 「メモを作成する」「一覧を見る」「削除する」といった、
# アプリでできること（操作の流れ）をまとめる層。
# 保存先の具体的な実装は知らず、MemoRepository という約束事だけを使う。

import uuid                    # 重複しないIDを生成するための標準ライブラリ
from datetime import datetime  # 作成日時の取得に使う
from entities.memo import Memo
from interfaces.memo_repository import MemoRepository

class MemoUseCase:
   def __init__(self, repo: MemoRepository):
       # 外から保存担当（リポジトリ）を受け取る＝依存性の注入（DI）
       self.repo = repo  # 具体的なDBではなく、「約束事」だけを受け取る

   def create_memo(self, title: str, content: str) -> Memo:
       """新しいメモを作成して保存する"""
       # ランダムなUUIDをIDにし、現在日時を作成日時としてメモを組み立てる
       memo = Memo(str(uuid.uuid4()), title, content, datetime.now())
       # エンティティのビジネスルールでチェックし、不正なら保存せずに例外を投げる
       if not memo.is_valid():
           raise ValueError("タイトルを入力してください")
       self.repo.save(memo)  # チェックを通ったメモだけを保存する
       return memo           # 呼び出し元で表示などに使えるよう、作成したメモを返す

   def get_all_memos(self) -> list[Memo]:
       """保存されている全メモを取得する"""
       return self.repo.find_all()

   def delete_memo(self, memo_id: str) -> None:
       """指定IDのメモを削除する"""
       self.repo.delete(memo_id)
