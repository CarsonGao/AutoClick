���ļ�����
    1.������ҪAndroid�汾����4.0��ʹ��������adb shell uiautomator dump�����ִ�С�adb shell uiautomator dump /data/local/tmp/uidump.xml��
    2.Ȼ�󽫸�xml�ļ�pull�����أ���������Կ����ֻ��ϵ�ǰҳ��Ĳ��֣���note�ڵ��¿����ҵ���Щ���ԣ�text��resource-id��class��bounds
    3.֪����Щ���ݺ�Ϳ���ʹ��python�Ը�xml�ļ�������ȡ����Ӧ�����ԣ�ȡ��bounds��ֵ���������ӦԪ���������������
    4.����ʹ��adb shell input tap ����Ϳ��Ե��������

ʹ�÷�����


���⣺
    1. Android 5.0.2�汾 xml�ļ���text��������Ǻ���ȫ����ʾΪ��������ƥ����Ҫʹ��id����   
    2. HLJ6 С�����ֻ������밲װҳ��ʱ����ȡ����xml ��ʾ����ΪERROR: null root node returned by UiTestAutomationBridge.
    3. Android 5.1.1�汾 ���뵽��װҳ����ȡ����xml ��ʾ����ΪERROR: null root node returned by UiTestAutomationBridge. �ϱߵ���������ǰ汾����
    4. Android 5.1�汾�����밲װ����ֱ���˳�



������
    1.����debug
    2.����log
    3.sax����xml
    4.�����ֻ���Ϣ��¼
    5.����û�������ʱ��ͨ��
    6.����ֻ����ֳ����Ƿ��ڽ����У�û�еĻ���������