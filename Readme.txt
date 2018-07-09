核心技术：
    1.首先需要Android版本高于4.0，使用这个命令“adb shell uiautomator dump”命令，执行“adb shell uiautomator dump /data/local/tmp/uidump.xml”
    2.然后将该xml文件pull到本地，从里面可以看到手机上当前页面的布局，在note节点下可以找到这些属性：text，resource-id，class，bounds
    3.知道这些内容后就可以使用python对该xml文件解析获取到对应的属性，取出bounds的值，计算出对应元素区域的中心坐标
    4.接着使用adb shell input tap 命令就可以点击该坐标

使用方法：


问题：
    1. Android 5.0.2版本 xml文件中text属性如果是汉字全部显示为？？？，匹配需要使用id属性   
    2. HLJ6 小辣椒手机，进入安装页面时，获取不到xml 显示错误为ERROR: null root node returned by UiTestAutomationBridge.
    3. Android 5.1.1版本 进入到安装页面后获取不到xml 显示错误为ERROR: null root node returned by UiTestAutomationBridge. 上边的问题可能是版本问题
    4. Android 5.1版本，进入安装后点击直接退出



后续：
    1.增加debug
    2.增加log
    3.sax解析xml
    4.增加手机信息记录
    5.增加没有适配的时候通用
    6.检查手机助手程序是否在进程中，没有的话让其运行