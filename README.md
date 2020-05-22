# 監督 Google Translate 翻譯臺灣用語

![](https://i.imgur.com/WGuxu1U.png)

## 索引
- [簡介](#%e7%b0%a1%e4%bb%8b)
- [功能](#%e5%8a%9f%e8%83%bd)
- [需求](#%e9%9c%80%e6%b1%82)
- [使用方法](#%e4%bd%bf%e7%94%a8%e6%96%b9%e6%b3%95)
- [注意事項](#%e6%b3%a8%e6%84%8f%e4%ba%8b%e9%a0%85)
- [已知問題](#%e5%b7%b2%e7%9f%a5%e5%95%8f%e9%a1%8c)
- [貢獻](#%e8%b2%a2%e7%8d%bb)
- [授權](#%e6%8e%88%e6%ac%8a)

## 簡介
+ [原討論串](https://tinyurl.com/y7y5w3xg)
+ [說明文件](https://tinyurl.com/y8htcwak)
+ [HackMD 版本](https://hackmd.io/@PenutChen/r1NjVCmoI)

## 功能
+ 自動填入意見回饋的表單
+ 自動修正建議用詞

## 需求
+ Python 3.7
+ Selenium
+ Chrome Driver

## 使用方法
+ 請先在自己喜歡的地方創建一個資料夾
    + 例如桌面，命名為 Workspace
        > ![](https://i.imgur.com/f7UUF5X.png)
+ [下載本程式](https://git.io/Jf2l8) 的壓縮檔，將其解壓縮到這個資料夾內
    > ![](https://i.imgur.com/CwlMcOO.png)

### 下載 Chrome Driver
+ 請先確認你的 Chrome 瀏覽器版本
    + 前往設定
        > ![](https://i.imgur.com/WRvdLOP.png)
    + 點選「關於 Chrome」
        > ![](https://i.imgur.com/7Xp8dA2.png)
    + 請記下這個版本號，此例為 `83.0.4103.61`
        > ![](https://i.imgur.com/Y96rUcp.png)
+ 前往 [ChromeDriver](https://chromedriver.chromium.org/) 頁面下載
    + 請確認下載的版本號不要高於 Chrome 本身的版本號
        > ![](https://i.imgur.com/RTtdgxD.png)
+ 下載後解壓縮放置到剛剛創建的資料夾底下
    > ![](https://i.imgur.com/6OYZSMc.png)

### 設定標的資料
+ 從 [Google 翻譯用詞整理](https://tinyurl.com/y85wgm3a) 工作表複製要翻譯的目標
    + 只需要複製前四個欄位，程式會自動跳過已經被標為 OK 的目標
    + 推薦先複製兩三筆資料測試看看程式有沒有問題
        > ![](https://i.imgur.com/9oLbAaW.png)
+ 把資料夾下的 `link.txt` 打開，並把文字檔的內容清除，然後貼上你剛剛複製的東西
    > ![](https://i.imgur.com/GYHFWCP.png)
+ 存檔後就可以執行 `main.exe` 試試看了！

## 注意事項
+ 大量使用本程式可能會導致 Google 將你加入黑名單，根據經驗要 24 個小時才會解除

## 已知問題
+ 有些意見回饋會按不到

## 貢獻
+ 歡迎發送 Issue 與 Pull Request 與我聯絡

## 授權
+ 本軟體授權條款為 MIT 授權