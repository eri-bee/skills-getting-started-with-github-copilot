## ステップ3: 全速前進 - Copilot Agentモード 🚀

### 📖 理論: Copilot Agentモードとは？

Copilotの[Agentモード](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)は、AIを活用したコーディングの次の進化です。自律的なピアプログラマーとして動作し、あなたの指示に従って複数ステップのコーディングタスクを実行します。

Copilot Agentモードは、コンパイルエラーやリントエラーに対応し、ターミナルやテストの出力を監視して、タスクが完了するまでループ内で自動修正します。

#### Agentモード（概要）

| 側面 | 👩‍🚀 Agentモード |
| --- | --- |
| 自律性と計画 | 高レベルのリクエストを複数ステップの作業に分解し、タスクが完了するまで繰り返します。 |
| コンテキスト収集 | 現在のコンテキストを使用し、必要に応じて関連するファイルを追加で探すことができます。 |
| ツール使用 | ツールを自動的に選択して呼び出します。`#codebase`のようなメンションでツールを指示することもできます。 |
| 承認とセーフティゲート | 機密性の高いアクションは実行前に承認が必要な場合があり、制御を維持できます。 |

#### 🧰 Agentモードのツール

Agentモードは、ユーザーのリクエストを処理しながら特定のタスクを実行するためにツールを使用します。そのようなタスクの例としては：

- プロンプトを完成させるために関連ファイルを見つける
- ウェブページのコンテンツを取得する
- テストまたはターミナルコマンドを実行する

> [!TIP]
> VS Codeは多くの組み込みツールを提供していますが、**MCPツール**を通じてAgentモードにさらなるドメイン固有の能力を提供することもできます。
>
> [MCPサーバー](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)と[GitHub MCPサーバー](https://github.com/github/github-mcp-server)について詳しく読む

では、**Agentモード**を試してみましょう！ 👩‍🚀

### :keyboard: アクティビティ: Copilotを使って新機能を追加する！ :rocket:

ウェブサイトでは活動が一覧表示されていますが、参加者リストは秘密にされています 🤫

Copilotを使って、各活動の下に登録済み学生を表示するようウェブサイトを変更しましょう！

1. Copilot Chatウィンドウの下部でドロップダウンを使って**Agent**モードに切り替えます。

   <img width="350" alt="image" src="../images/agent-mode-dropdown.png" />

1. ウェブページに関連するファイルを開き、各エディターウィンドウ（またはファイル）をチャットパネルにドラッグして、Copilotがそれらをコンテキストとして使用するよう指示します。

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **注意:** ファイルをコンテキストとして追加することはオプションです。これを省略しても、Copilot Agentモードは`#codebase`のようなツールを使ってプロンプトから関連ファイルを検索できます。特定のファイルを追加することで、Copilotを正しい方向に導きます。これは大規模なコードベースで特に役立ちます。

   <img width="400" alt="コンテキストに追加されたファイルを示す画像" src="../images/files-added-to-context.png" />

   > 💡 **ヒント:** **Add Context...**ボタンを使って、GitHubのIssueやターミナルウィンドウの結果など、他のコンテキストアイテムのソースを提供することもできます。

1. Copilotに活動の現在の参加者を表示するようプロジェクトを更新するよう頼みます。編集の提案が届いて適用されるまでしばらく待ちます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   Copilotが作業を終えたら、どの変更を残すかはあなたが決めます。

   以下に示す**Keep**ボタンを使って、すべての変更を承認/破棄するか、変更を一つずつ確認して決定することができます。これはチャットパネルビューからでも、各編集されたファイルを検査しながらでも行えます。

      <img width="900" alt="変更を保持または破棄するボタン" src="../images/review-changes-buttons.png" />


1. 単純に変更を承認する前に、ウェブサイトを再確認して、すべてが期待どおりに更新されていることを確認してください。
   
   更新された活動カードの例を示します。アプリを再起動するかページを更新する必要があるかもしれません。

   <img width="350" alt="参加者情報が表示された活動カード" src="../images/activity-card-with-participants.png" />

   > 🪧 **注意:** あなたの活動カードは異なって見えるかもしれません。Copilotは常に同じ結果を生成するわけではありません。

   <details>
   <summary>困ったときは？ 🤷</summary><br/>
   ウェブサイトが読み込まれない場合は、以下の点を確認してください。

   - VS Codeデバッガーを再起動して、最新バージョンのウェブサイトが提供されていることを確認してください。
   - URLを忘れたか、ウィンドウを閉じた場合は、ステップ1を確認してください。
   - ウェブページをハード更新するか、プライベートウィンドウで開いて新しいコピーをダウンロードしてください。

   </details>

1. 変更が良いことを確認したら、パネルを使って各編集提案を順番に確認し、**Keep**を押して変更を適用します。

   > 💡 **ヒント:** 変更を直接承認したり、修正したり、チャットインターフェースを使って追加の指示を提供して結果を精緻化することができます。

### :keyboard: アクティビティ: Agentモードを使って機能する「登録解除」ボタンを追加する

ウェブアプリケーションに機能を追加するオープンエンドなリクエストでさらに実験してみましょう。

望む結果が得られない場合は、他のモデルを試したり、結果を精緻化するためのフォローアップフィードバックを提供したりしてください。

1. Copilotがまだ**Agent**モードであることを確認します。

   <img width="250" alt="Agentモード" src="../images/agent-mode-dropdown.png" />

1. **ツール**アイコンをクリックして、Copilot Agentモードで現在利用可能なすべてのツールを探索します。

   <img width="250"  alt="ツールアイコン" src="../images/tools-icon.png" />

1. テストをする時です！Copilotに参加者を削除する機能を追加するよう頼みます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   `#codebase`ツールはCopilotが手元のタスクに関連する関連ファイルやコードチャンクを見つけるために使用されます。

   > 🪧 **注意:** このラボでは最も再現性の高い結果を得るために、明示的に`#codebase`ツールを含めています。
   > `#codebase`**なし**でプロンプトを試して、Agentモードがプロジェクト全体のコンテキストを収集するかどうかを観察してみてください。

1. Copilotが終わったら、コードの変更とウェブサイト上の結果を確認します。結果が気に入ったら、**Keep**ボタンを押します。気に入らない場合は、Copilotにフィードバックを提供して結果を精緻化してください。

   > 🪧 **注意:** ウェブサイトに更新が表示されない場合は、デバッガーを再起動する必要があるかもしれません。

1. Copilotに登録バグを修正するよう頼みます。

   > 💡 **ヒント:** 変更前後の動作を明確に確認できるよう、自分で登録フローをテストすることを推奨します。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. Copilotが終わったら、ウェブサイト上の結果を確認して登録フローを検証します。

   結果が気に入ったら、**Keep**ボタンを押します。気に入らない場合は、Copilotにフィードバックを提供してください。

1. すべての変更を`accelerate-with-copilot`ブランチに**コミット**して**プッシュ**します。

1. Monaがあなたの作業を確認して次のステップを共有するのを待ちます。
