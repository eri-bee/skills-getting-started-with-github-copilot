## ステップ2: Copilotと一緒に仕事を進める

前のステップでは、GitHub Copilotがプロジェクトへのオンボーディングを助けてくれました。それだけでも大きな時間の節約になりますが、今度は実際に仕事を進めましょう！

:bug: **ウェブサイトにバグがあります** :bug:

登録フローに問題があることが発覚しました。
現在、学生が同じ活動に**複数回**登録できてしまいます！Copilotがどこまで原因の特定と修正に力を貸してくれるか見てみましょう。

本題に入る前に、Copilotの仕組みについて簡単に説明します。 🧑‍🚀

### 📖 理論: Copilotの仕組み

簡単に言うと、Copilotは非常に専門化されたチームメンバーのようなものです。効果的に活用するには、背景情報（コンテキスト）と明確な指示（プロンプト）を提供する必要があります。また、異なる経験（モデル）を持つ人は異なることに長けています。

- **コンテキストの提供方法は？:** コーディング環境では、Copilotは近くのコードや開いているタブを自動的に考慮します。チャットを使用している場合は、ファイルを明示的に参照することもできます。

- **どのモデルを選ぶべきか？:** このエクササイズでは、あまり重要ではありません。異なるモデルを試すことも楽しみの一つです！それはまた別のレッスンで！ 🤖

- **プロンプトの作り方は？:** 明確かつ具体的にすることで、Copilotが最善の仕事をできます。ただし、従来のシステムとは異なり、フォローアッププロンプトで方向性を明確にすることもできます。

> [!TIP]
> [チャット参加者](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants)、[チャット変数](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables)、[スラッシュコマンド](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1)、[MCPツール](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)など、Copilotの知識と機能を補完する他の方法もいくつかあります。

### :keyboard: アクティビティ: Copilotを使って登録バグを修正する :bug:

1. Copilotにバグの原因を提案してもらいましょう。**Copilot Chat**パネルを**Askモード**で開き、以下のプロンプトを入力します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Students are able to register twice for an activity.
   > Where could this bug be coming from?
   > ```

1. 問題が`src/app.py`ファイルの`signup_for_activity`メソッドにあることがわかったので、Copilotの推奨に従って修正しましょう（半手動で）。コメントから始めて、Copilotに修正を完成させてもらいます。
   1. `src/app.py`ファイルを開きます。

      > 💡 **ヒント:** Copilotがチャットで`src/app.py`に言及した場合、チャットビューでそのファイルを直接クリックして開くことができます。

   1. ファイルの下部近くで`signup_for_activity`関数を見つけます。

   1. 学生を追加することを説明するコメント行を見つけます。その上が登録チェックを行うのに適切な場所です。

   1. 以下のコメントを入力してEnterキーを押して次の行に移動します。しばらくすると、Copilotからのサジェストがシャドーテキストとして表示されます！素晴らしい！ :tada:

      コメント：

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="エディタでのCopilotシャドーテキストサジェスト" src="../images/shadow-text.gif" />

   1. `Tab`キーを押してCopilotのサジェストを承認し、シャドーテキストをコードに変換します。

   <details>
   <summary>結果の例</summary><br/>

   Copilotは日々進化しており、常に同じ結果を生成するとは限りません。サジェストに満足できない場合は、このエクササイズの作成中に生成した有効なサジェスト結果の例を示します。これを使って先に進むことができます。

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: アクティビティ: Copilotにサンプルデータを生成させる 📋

新しいプロジェクト開発では、テスト用にリアルに見えるフェイクデータがあると役立つことがよくあります。Copilotはこのタスクが得意なので、さらにサンプル活動を追加して、**インラインチャット**を使ってCopilotと別の方法で対話してみましょう。

**インラインチャット**と**Copilot Chat**パネルは似ていますが、スコープが異なります：Copilot Chatは広範なマルチファイルや調査的な質問を処理し、インラインチャットは目の前の特定の行やブロックに対して素早いサポートが必要なときに便利です。

1. `src/app.py`ファイルの上部近く（約23行目）で、サンプルの課外活動が設定されている`activities`変数を見つけます。

1. 辞書の先頭から末尾までマウスでクリック＆ドラッグして、`activities`辞書全体を選択します。これにより、次のプロンプトのためのコンテキストをCopilotに提供します。

   <img width="700" alt="インラインチャットを開く前にハイライトされたactivities辞書" src="../images/activities-dict-highlighted.png" />


1. キーボードコマンド`Ctrl + I`（Windows）または`Cmd + I`（Mac）を使ってCopilotのインラインチャットを呼び出します。

   > 💡 **ヒント:** Copilotのインラインチャットを呼び出す別の方法は：選択した行のどれかを`右クリック` -> `インラインチャットを開く`です。

1. 以下のプロンプトテキストを入力してEnterキーを押すか、右側の**送信**ボタンを押します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add 2 more sports related activities, 2 more artistic
   > activities, and 2 more intellectual activities.
   > ```

1. しばらくすると、Copilotがコードに直接変更を加え始めます。変更は追加と削除を識別しやすくするために異なるスタイルで表示されます。変更を確認してから**Keep**ボタンを押します。

   <details>
   <summary>結果の例</summary><br/>

   Copilotは日々進化しており、常に同じ結果を生成するとは限りません。サジェストに満足できない場合は、このエクササイズの作成中に生成した結果の例を示します。問題がある場合はこれを使って先に進むことができます。

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. ウェブサイトで新しい活動が表示されていることを確認できます。

### :keyboard: アクティビティ: Copilotに作業内容を説明させる 💬

バグを修正してサンプル活動を追加するすばらしい作業ができました！今度は、再びCopilotの助けを借りて作業をコミットしてGitHubにプッシュしましょう。

1. 左サイドバーで`ソース管理`タブを選択します。

   > 💡 **ヒント:** ソース管理エリアからファイルを開くと、単純にファイルを開くのではなく、オリジナルとの差分が表示されます。

1. `app.py`ファイルを見つけて`+`記号を押し、変更をステージングエリアにまとめます。

   ![image](../images/staging-changes-icon.png)

1. ステージングされた変更のリストの上にある**メッセージ**テキストボックスを見つけますが、今は**何も入力しないで**ください。
   - 通常はここに変更の短い説明を書きますが、今はCopilotに手伝ってもらいます！

1. **メッセージ**テキストボックスの右側にある**コミットメッセージを生成**ボタン（スパークルアイコン）を見つけてクリックします。

1. **コミット**ボタンと**変更を同期**ボタンを押して変更をGitHubにプッシュします。

1. Monaがあなたの作業を確認し、フィードバックを提供して次のレッスンを共有するまでしばらく待ちます。

<details>
<summary>うまくいかない場合は？ 🤷</summary><br/>

フィードバックが得られない場合は、以下の点を確認してください：

- `src/app.py`ファイルの変更がブランチ`accelerate-with-copilot`にプッシュされていることを確認してください。

</details>
