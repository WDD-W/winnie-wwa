## 创建助记词&生成KeyStore
# ![eth](https://ethereum.org/favicon-32x32.png?v=8b512faa8d4a0b019c123a771b6622aa)ETH操作手册
### 1.  下载最新的**Wagyu Key Gen**应用
**❗️❗️建议从离线机器上运行 Wagyu Key Gen，或在断开互联网连接情况下进行第3步。**

https://github.com/stake-house/wagyu-key-gen/releases

- 使用设备：Windows
    - 参考(Windows v1.5.0版本)：https://github.com/stake-house/wagyu-key-gen/releases/download/v1.5.0/Wagyu.Key.Gen.1.5.0.exe 
- 使用设备：Mac：
    - 参考(MAC v1.5.0版本)：https://github.com/stake-house/wagyu-key-gen/releases/download/v1.5.0/Wagyu.Key.Gen-1.5.0.dmg 
### 2.  安装**Wagyu Key Gen**应用

**注：若安装完成应用后无法打开，使用以下方式允许该应用运行**

    1. 在Mac上，选取苹果菜单>“系统偏好设置”，点按“安全性与隐私”，然后点按“通用”。
    2. 点击左下角解锁输入密码，查看"已阻止使用“Wagyu Key Gen”，因为来自身份不明的开发者。仍要打开"
    3. 点击"仍要打开"，左下角锁定。

### 3.  安装完成后使用**Wagyu Key Gen**应用生成存款密钥



1. 创建助记词。点击页面“CREATE NEW SECRET RECOVERY PHRASE”->弹出NETWORK对话框，选择MAINNET(默认)

2. 跳转"Create Secret Recovery Phrase"页面->点击 NEST，等待半分钟，弹出24位助记词。

3. 备份您的助记词，建议备份>1份，备份完成后点击NEXT。

4. 确认已经备份您的助记词，点击NEST，在文本框内填写您的助记词进行二次确认，点击CHECK进行核查。

**(❗️❗️确保您的秘密恢复短语和验证者密钥的安全非常重要，因为您稍后将需要它们来取回您的资金。任何有权访问这些的人也将能够窃取您的资金！没有它，您将无法取回您的资金！)**

5. 在“Number of New Keys” 文本框内输入您要创建的validator key的数量，可同时创建多个validator keys。输入密码进行加密，点击Next.

·可选：若您想在资金或收益收回时使用一个新地址存储它们，可打开”Use Advanced Inputs“,输入您的以太坊提现地址（❗️❗️请确保您可以控制改地址）

6. 输入您的密码进行 二次确认。点击NEXT

7. 选择保存您的keys的文件夹，点击BROWSE选择文件夹，点击CREATE进行文件创建。每个密钥生成的时间约为30S，请耐心等待，您的密钥正在生成中。

当出现该页面，那么恭喜您，您的密钥已经创建成功，可在第7步选择的文件夹中进行查看。


    这里是每个文件的描述：

    密钥库文件（例如 keystore-xxxxxxx.json）

    此文件控制您签署交易的能力。需要设置您的验证器。不要与任何人分享。如有必要，可以从您的秘密恢复短语中重新创建它。

    存款数据文件（例如 deposit_data-xxxxxx.json）

    此文件代表有关您的验证器的公共信息。需要通过 Ethereum Launchpad 执行您的存款。如有必要，可以从您的秘密恢复短语中重新创建它。

    秘密恢复短语（24 字）

    这是您创建的第一件事。它也被称为“助记符”或“种子短语”。你需要这个来提取你的资金。将多份副本保存在不同的物理位置，以防被盗、火灾、水和其他危险。保持私密。没有办法恢复这一点。





