# 校務行政系統自動選課工具

這是一個基於 Python 的自動化選課工具，用於高中的校務行政系統。該工具使用 Selenium 驅動瀏覽器，並結合 Anti-Captcha API 自動破解驗證碼，大幅簡化選課流程。

---

## 功能簡介

### 🌟 功能亮點
1. **自動登入**  
   自動輸入帳號、密碼以及破解驗證碼，輕鬆完成登入操作。

2. **導航至選課頁面**  
   自動點擊校務行政系統中的菜單，快速到達選課界面。

3. **自動課程選擇與儲存**  
   自動點擊指定課程並儲存選課結果。

---

## 使用技術

- **Python 3.9+**  
- **Selenium 4.18.1**  
  用於驅動瀏覽器執行自動化操作。
- **Anti-Captcha API**  
  用於破解圖片驗證碼。
- **Google Chrome 與 ChromeDriver**  
  提供瀏覽器支持。

---

## 安裝與配置

### 1. 安裝依賴
確保您已安裝 Python，然後使用以下命令安裝必要的依賴庫：
```bash
pip install selenium anticaptchaofficial
```

### 2. 配置環境
- **下載 ChromeDriver**  
  根據您的 Chrome 瀏覽器版本下載對應的 [ChromeDriver](https://sites.google.com/chromium.org/driver/)。

- **配置 Anti-Captcha API**  
  前往 [Anti-Captcha 官方網站](https://anti-captcha.com/) 註冊帳號並獲取 API Key，將其填入程式中的 `solver.set_key()`。

### 3. 修改程式參數
- **登入憑證**  
  將您的帳號與密碼填入程式中的 `username_field.send_keys('id')` 和 `password_field.send_keys('pwd')`。
- **校務系統網址**  
  替換 `login_url` 為您的學校專屬校務系統網址。
- **選課名稱**  
  將您的選課名稱(例如:"二升三彈性選課"或"高三彈性選課")填入程式中的EC.element_to_be_clickable((By.XPATH, '//td[@title="XXXX選課"]'))
- **課程 XPath**  
  根據您的需求，修改 `class_button` 的 XPath。

---

## 使用方法

### 執行程式

#### 使用批次檔搭配 Windows 自動排程器

1. 建立一個名為 `run.bat` 的批次檔，內容如下：
   ```batch
   @echo off
   python main.py
   pause
   ```

2. 在 Windows 中設定自動排程器：
   - 打開「任務排程器」。
   - 創建新任務，並在「操作」選項卡中設置執行 `run.bat`。

3. 保存設定，排程器將按照您指定的時間自動運行程式。

---

### 手動執行

1. 執行程式：
   ```bash
   python main.py
   ```

2. 程式將自動：
   - 登入校務系統。
   - 導航至彈性學習選課頁面。
   - 點擊指定課程並儲存選課結果。

3. 選課完成後，您可以按下 Enter 鍵結束程式。

---

## 注意事項

- 本程式僅供學術與學習用途，請勿用於非法操作。
- 驗證碼破解需要付費，請確保您的 Anti-Captcha 帳號餘額充足。
- 瀏覽器操作過程中，請勿手動干預。
- 請在正式選課前測試操作是否正常。
- 選課失敗，概不負責。
- 高雄市高中職校務行政系統 (程式版本:v1.0131 版本日期:106/11/29) 實測有效 (測試日期:114/02/03)

---

有任何問題或建議，請隨時聯繫我！ 🎉

