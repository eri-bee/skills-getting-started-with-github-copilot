## ステップ4: Plan Agentで実装を計画する 🧭

前のステップでは、Agentモードが迅速に新機能を実装するのに役立ちました。 🚀

今度は一歩立ち止まり、アーキテクトのように作業してみましょう：まず強力なテストアプローチを定義してから実装に引き渡します。これにより、より明確さが生まれ、驚きが減り、より良い結果が得られます。 🧪

### 📖 理論: Copilot Plan Agentとは？

Copilotの[Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning)は、コードが変更される前にソリューションを設計するのに役立ちます。

すぐに編集に飛び込む代わりに、リクエストを調査し、明確化の質問をして、洗練できる実装計画を作成します。

#### Plan Agent（概要）

| 側面 | 🧭 Plan Agent |
| --- | --- |
| 目的 | コーディングが始まる前に構造化された実装計画を作成します。 |
| コンテキスト収集 | 読み取り専用の調査を使って要件と制約を理解します。 |
| コラボレーションスタイル | 明確化の質問をして、回答を使って計画を更新します。 |
| 反復 | 実装前に複数回の精緻化パスをサポートします。 |
| 安全性 | 計画を承認して**Agentモード**に引き渡すまでファイルを編集しません。 |
| 引き渡し | **実装開始**ボタンで承認された計画を**Agentモード**にコーディングのために引き渡します。 |

> [!TIP]
> 高レベルなリクエストから始めて、フォローアッププロンプトで制約や詳細を追加できます。

### ⌨️ アクティビティ: バックエンドテストを計画して実装する

バックエンドにはまだテストカバレッジがありません。**Plan Agent**を使って計画を作成し、質問に答えて、実装を開始しましょう。

1. **Copilot Chat**パネルを開き、**Plan Agent**に切り替えます。

   <img width="350" alt="image" src="../images/plan-mode-dropdown.png" />


1. 広いプロンプトから始めて、Copilotが詳細を埋める手助けをしてくれます：

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I want to add backend FastAPI tests in a separate tests directory.
   > ```

1. Copilotが最初の計画を生成するのを待ちます。質問があれば、できる限り答えてください。

   > 🪧 **注意:** 完璧にする必要はありません。後で計画を精緻化することができます。

1. フォローアッププロンプトで計画を精緻化して詳細を追加できます

   以下はいくつかの例です：

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Make sure we use `pytest` and add it to `requirements.txt` file
   > ```


1. 提案された計画を確認し、満足したら**実装を開始**をクリックして**Agentモード**に引き渡します。

   <img width="350" alt="image" src="../images/plan-mode-start-implementation.png" />

   ボタンをクリックすると**Plan**から**Agentモード**に切り替わることに注意してください。この時点から、Copilotは以前と同様にコードベースを編集できます。

1. 作成した計画をCopilotが実装するのを見守ります。特定のツールを実行する許可（例：コマンドを実行したり仮想環境を作成したりする）が求められる場合があります。作業を続けられるよう、これらの許可を承認してください。

1. 変更を確認し、テストが正常に実行されることを確認します。必要であれば、実装が完了するまで引き続きガイドしてください。

   **🎯 目標: 先に進む前にすべてのテストが通過（緑）していることを確認してください。 ✅**

   > 🪧 **注意:** Agentモードは1回のパスで完了する場合もありますし、あなたからのフォローアッププロンプトが必要な場合もあります。

1. すべての変更を`accelerate-with-copilot`ブランチに**コミット**して**プッシュ**します。

1. Monaがあなたの作業を確認して次のステップを共有するのを待ちます。

<details>
<summary>うまくいかない場合は？ 🤷</summary><br/>

- テストが実行されなかった場合は、Copilotに実行するよう頼んでください。
- `pytest`が`requirements.txt`に追加されていて、`tests/`ディレクトリが存在することを確認してください。

</details>
