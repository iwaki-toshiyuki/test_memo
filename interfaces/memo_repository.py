# interfaces/memo_repository.py
# 【インターフェース層】
# 「メモをどう保存するか」の具体的な方法ではなく、
# 「保存・取得・削除ができること」という約束事（契約）だけを定義する層。
# ユースケース層はこの抽象クラスにだけ依存するので、
# 保存先（メモリ・ファイル・DBなど）を後から自由に差し替えられる（依存性逆転の原則）。

from abc import ABC, abstractmethod  # 抽象クラス・抽象メソッドを作るための標準ライブラリ
from entities.memo import Memo       # 扱うデータの型としてエンティティを参照

class MemoRepository(ABC):
   """メモ保存機能の約束事（抽象クラス）"""

   # @abstractmethod を付けたメソッドは、継承先で必ず実装しなければならない
   # （実装していないとインスタンス化時にエラーになる）

   @abstractmethod
   def save(self, memo: Memo) -> None: ...  # メモを保存する

   @abstractmethod
   def find_all(self) -> list[Memo]: ...  # 保存されている全メモを取得する

   @abstractmethod
   def delete(self, memo_id: str) -> None: ...  # 指定IDのメモを削除する
