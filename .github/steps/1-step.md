## ステップ1: Copilotとの最初の一歩

**「GitHub Copilot 入門」** エクササイズへようこそ！ :robot:

このエクササイズでは、Mergington高校の生徒が課外活動に登録できるウェブサイトを作業するために、さまざまなGitHub Copilotの機能を使用します。 🎻 ⚽️ ♟️

<img width="600" alt="Mergington High School WebAppのスクリーンショット" src="../images/mergington-high-school-webapp.png" />

### 📖 理論: GitHub Copilotについて知ろう

<img width="150" align="right" alt="Copilotロゴ" src="../images/copilot-logo.png" />

GitHub Copilotは、AIコーディングアシスタントであり、より少ない労力でコードを速く書けるようにサポートします。これにより、問題解決とコラボレーションにより多くのエネルギーを注げます。

GitHub Copilotは開発者の生産性を向上させ、ソフトウェア開発のペースを加速することが証明されています。詳細については、[Research: quantifying GitHub Copilot's impact on developer productivity and happiness (GitHubブログ)](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)をご覧ください。

IDEで作業する際、GitHub Copilotと最もよく対話する方法は次のとおりです：

| 対話モード                | 📝 説明                                                                                                                 | 🎯 最適な用途                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ インラインサジェスト** | 入力中にAIによるコード提案が表示され、1行から関数全体まで文脈に応じた補完を提供します。 | 現在の行の補完、場合によってはコードブロック全体                                             |
| **💭 インラインチャット**        | 現在のファイルや選択範囲に限定されたインタラクティブなチャット。特定のコードブロックについて質問できます。                           | コードの説明、特定の関数のデバッグ、的を絞った改善                                          |
| **💬 Askモード**           | コードベース、コーディング、一般的な技術概念に関する質問への回答に最適化されています。                                | コードの動作理解、アイデアのブレインストーミング、質問する                                             |
| **🤖 Agentモード**         | ほとんどのコーディングタスクに推奨されるデフォルトモード：自律的な編集、ツール使用、タスク完了まで自動的に進めます。         | 日々のコーディングタスク、スコープを絞った修正から大規模なマルチファイル実装まで                                   |
| **🧭 Plan Agent**         | コード変更を行う前に計画を立案し、明確化の質問をすることに最適化されています。                                | レビュー済みの計画を先に作成したい場合に、実装に引き継ぐ                                            |

作業する中で、GitHub Copilotは `github.com` ウェブサイト全体や、VS Code、JetBrains、Xcodeなどのお気に入りのコーディング環境でも活躍することがわかるでしょう！

今日のコーディングでは、[GitHub Codespace](https://github.com/features/codespaces)として知られる事前設定済みの開発環境でVS Codeを使って練習します。

> [!TIP]
> 現在および今後の機能については、[GitHub Copilotの機能](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)ドキュメントで詳しく学べます。

### :keyboard: アクティビティ: Copilot Chatからプロジェクトの紹介を受ける

開発環境を立ち上げ、Copilotを使ってプロジェクトについて学び、テスト実行してみましょう。

1. 以下のボタンを使って新しいタブで **Codespace作成**ページを開きます。デフォルト設定を使用してください。

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. **Repository**フィールドがオリジナルではなく、あなたのエクササイズのコピーであることを確認してから、緑色の**Codespaceを作成**ボタンをクリックします。
   - ✅ あなたのコピー: `/{{full_repo_name}}`
   - ❌ オリジナル: `/skills/getting-started-with-github-copilot`

1. Visual Studio Codeがブラウザに読み込まれるまで少し待ちます。

1. 左サイドバーで、拡張機能タブをクリックして、`GitHub Copilot`と`Python`の拡張機能がインストールされて有効になっていることを確認します。

   <img width="350" alt="VS Code用GitHub Copilot拡張機能" src="../images/copilot-extension-vscode.png" />

   <img width="350" alt="VS Code用Python拡張機能" src="../images/python-extension-vscode.png" />

1. VS Codeの上部で、**チャット切り替えアイコン**を見つけてクリックし、Copilot Chatのサイドパネルを開きます。

   <img width="150" alt="image" src="../images/toggle-chat-icon.png" />

   > 🪧 **注意:** GitHub Copilotを初めて使用する場合、続けるには利用規約に同意する必要があります。

1. 最初の対話のために**Askモード**になっていることを確認します

   <img width="350" alt="Copilot ChatでAskモードを選択したスクリーンショット" src="../images/ask-mode-selection.png" />

1. 以下のプロンプトを入力して、Copilotにプロジェクトを紹介してもらいます。

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please briefly explain the structure of this project.
   > What should I do to run it?
   > ```

   > 🪧 **注意:** Copilotの推奨手順に従う必要はありません。すでに環境を準備してあります。

1. プロジェクトについて少し知ったところで、実際に実行してみましょう！左サイドバーで`実行とデバッグ`タブを選択し、**デバッグ開始**アイコンを押します。

   <img width="300" alt="image" src="../images/run-and-debug-tab.png" />

1. ブラウザでウェブページが実行されるのを確認したいので、URLとポートを見つけましょう。表示されていない場合は、下部のパネルを展開して**ポート**タブを選択します。

1. リストの中からポート`8000`と関連するリンクを見つけます。リンクにホバーして**ブラウザで開く**アイコンを選択します。

   ![image](../images/open-in-browser-icon.png)

### :keyboard: アクティビティ: ターミナルコマンドを思い出すためにCopilotを使う 🙋

よくできました！アプリを確認して動作することがわかったので、ブランチを作成してカスタマイズを始めるためにCopilotに助けを求めましょう。

1. VS Codeの下部パネルで、**ターミナル**タブを選択し、右側のプラス`+`記号をクリックして新しいターミナルウィンドウを作成します。

   > 🪧 **注意:** これにより、ウェブアプリサービスをホストしている既存のデバッグセッションを停止せずに済みます。

1. 新しいターミナルウィンドウ内で、キーボードショートカット`Ctrl + I`（Windows）または`Cmd + I`（Mac）を使って**CopilotのTerminal Inline Chat**を呼び出します。

1. 忘れてしまったコマンド（ブランチを作成して公開すること）をCopilotに手伝ってもらいましょう：

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
   > ```

   > 💡 **ヒント:** Copilotが望む結果を返さない場合は、必要なことを説明し続けることができます。Copilotはフォローアップの返答のために会話履歴を覚えています。

1. Copilotがターミナルコマンドを入力してくれるよう、`実行`ボタンを押します。コピー＆ペーストは不要です！

1. しばらくしたら、VS Codeの下部ステータスバーの左側を見て、アクティブなブランチを確認します。`accelerate-with-copilot`と表示されているはずです。そうであれば、このステップは完了です！

1. ブランチがGitHubにプッシュされたので、Monaがあなたの作業を確認中のはずです。少し待って、コメントを確認してください。進捗情報と次のレッスンが表示されます。

<details>
<summary>うまくいかない場合は？ 🤷</summary><br/>

フィードバックが得られない場合は、以下の点を確認してください：

- ブランチが正確に`accelerate-with-copilot`という名前で作成されていることを確認してください。プレフィックスやサフィックスは不要です。
- ブランチがリポジトリに公開されていることを確認してください。

</details>
