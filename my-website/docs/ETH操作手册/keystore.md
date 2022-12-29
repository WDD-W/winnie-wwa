---
sidebar_position: 3
---
# 加密 Keystore

### 一、加密方式

为了数据安全，采用非对称加密

> 非对称加密是使用公钥/私钥对中的公钥来加密明文，然后使用对应的私钥来解密密文的过程。非对称加密只有同一个公钥-私钥对才能正常加解密，安全系数非常高。

### 二、加密软件
- GnuPG， 简称GPG
- 官网：[GPG](https://gnupg.org/)

> GPG是目前最流行、最好用的加密工具之一,GnuPG 允许您加密和签署您的数据和通信；它具有通用的密钥管理系统，以及各种公钥目录的访问模块。
 Gpg4win是Windows版本的GPG, GPG Suite用于Mac。

### 三、软件安装

#### 3.1 windows系统
#### 3.1.1 下载Gpg4win

1. 打开链接 [https://gpg4win.org/](https://gpg4win.org/) , 如下图。点击绿色按钮`Download Gpg4win 4.0.4`下载软件。
![](../static/img/p2/download_win.png)

2. 点击下载的exe文件，依次点击下一步，完成安装。
![](../static/img/p2/gpgwininstall.png)
![](../static/img/p2/gpgwininstall1.png)

#### 3.2. macOS系统
#### 3.2.1 下载 GPG Suite
1. 打开链接 [https://gpgtools.org/](https://gpgtools.org/)，如下图，点击红色按钮`Download`下载GPG Suite。
![](../static/img/p2/gpgmacdownload.png)

2. 下载完成后点击dmg安装包安装，再点击如下install按钮
![](../static/img/p2/gpginstall0.png)
如出现以下弹框，请输入电脑开机密码，完成软件安装。
![](../static/img/p2/gpgmacinstall.png)


### 四、加密keystore

将生成的文件加密，用于安全传输到eBunker。开始操作前，请先确认已完成[生成Keystore操作](create-keystore#创建助记词生成密钥库)，
检查创建的“ebunker”文件夹及文件：
   - 1.keystore-xxxxxxx.json：密钥库文件
   - 2.deposit_data-xxxxxx.json：存款数据文件
   - 3.[keystore密码.txt](create-keystore#45-创建validator-key填写eth提现地址)：用于加密keystore的明文密码。

windows：
![密钥](/img/p1/ebunker_all.png)
mac：
![密钥](/img/p1/ebunker_all_mac.png)
#### 4.1 加密
- 准备：
   - 从官方github下载公钥文件和脚本文件压缩包 [tools.zip](https://github.com/ebunker-io/encrypt-tools/releases/download/v1.0.1/tools.zip)
   - 解压tools.zip，桌面生成“tools”文件夹，文件夹内有“encrypt-win.bat、encrypt-mac.sh、ebunker-public-key.gpg”文件。根据设备选择文件，将所需文件移至桌面，具体步骤如下。

##### 4.1.1 windows系统

1. windows设备用户进行操作时，使用文件有：encrypt-win.bat、ebunker-public-key.gpg，将两个文件移到桌面。保证桌面有如图文件:
![](../static/img/p2/winallfile.png)


2. 双击 encrypt-win.bat 执行脚本
> 命令行中输出的密钥指纹为密钥提示信息，无需保存。

3. 若出现`Use this key anyway?`确认密钥提示，输入`y`后回车即可
> 公钥由github下载解压得到，可确认密钥安全

![](../static/img/p2/gpg-yes-win.png)

4. 最终生成`ebunker-keystore_202xxxxxxxxxxx.gpg`文件，作为接下来的邮件附件
![](../static/img/p2/winencrypted.png)

##### 4.1.2 macOS系统

1.  mac设备用户进行操作时，使用文件有：encrypt-mac.sh、ebunker-public-key.gpg、encrypt-win.bat，将三个文件移到桌面。保证桌面有如图文件:
![](../static/img/p2/mac_desktop.png)
若桌面没有以上文件，请下载[tools.zip](https://github.com/ebunker-io/encrypt-tools/releases/download/v1.0.1/tools.zip)，并解压到桌面
![](../static/img/p2/download_tool.gif)
2. 打开终端
- 如下图所示，在启动台launchpad中的`其他`中找到`终端`，点击打开
![](../static/img/p2/open_terminal.gif)
![](../static/img/p2/maclaunchpad.png)
![](../static/img/p2/maclaunchpadother.png)

3. 在终端中输入`bash ~/Desktop/encrypt-mac.sh`后回车
![](../static/img/p2/run_terminal.gif)
![](../static/img/p2/terminal.png)
4. 若出现确认密钥提示，公钥由github下载解压得到，可确认以下密钥安全提示，输入`y`后回车即可
> 命令行中输出的密钥指纹为密钥提示信息，无需保存。

![](../static/img/p2/gpg-yes.png)
5. 最终生成`ebunker-keystore_202xxxxxxxxxxx.gpg`文件，作为接下来的邮件附件
![](../static/img/p2/result.png)

### 五、发送加密文件

#### 5.1 发送加密文件邮件
将第四部中生成的文件(ebunker-keystore_202xxxxxxxxxxx.gpg)以及您的收益地址发送至官方邮件。
- 官方邮箱：support@ebunker.io
- 回复信息：
   - Keystore加密文件
   - 收益地址

**邮件参考：**
![](../static/img/p2/keystore_scr.png)

### 六、节点部署
**官方收到邮件后会使用您的keystore进行节点部署，部署完成后您将收到“节点部署已完成”的邮件回复。请先确认收到邮件，确保节点已准备完成，然后继续操作ETH质押，完成您的验证者创建。** [点击继续](stake#注意)

**回复参考：**

![](../static/img/p2/node.png)

[返回主页](intro#关于)
