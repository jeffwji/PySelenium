## Local

Download `geckodriver` to `/usr/bin` or `/usr/local/bin`.

| Browser      | downloads |
| - | - |
| Chrome      | https://sites.google.com/a/chromium.org/chromedriver/       |
| Edge   | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/        |
| Firefox | https://github.com/mozilla/geckodriver/releases |
| Safari | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |

```sh
$  geckodriver 
1602985440263	geckodriver	INFO	Listening on 127.0.0.1:4444
```

在本地 `4444` 端口开启监听


## Remote

The Selenium server is only required if you want to use the remote WebDriver.

Download from: https://www.selenium.dev/

```sh
$ java -jar selenium-server-standalone-3.141.59.jar
21:43:51.906 INFO [GridLauncherV3.parse] - Selenium server version: 3.141.59, revision: e82be7d358
21:43:52.004 INFO [GridLauncherV3.lambda$buildLaunchers$3] - Launching a standalone Selenium Server on port 4444
2020-10-17 21:43:52.088:INFO::main: Logging initialized @452ms to org.seleniumhq.jetty9.util.log.StdErrLog
21:43:52.424 INFO [WebDriverServlet.<init>] - Initialising WebDriverServlet
21:43:52.548 INFO [SeleniumServer.boot] - Selenium Server is up and running on port 4444
```

在 `4444` 端口开启对外监听

注意：`geckodriver` 也需要被安装在远程 Selenium server 上。
