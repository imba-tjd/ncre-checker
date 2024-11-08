# NCRE Chekcer

本项目为自用友好爬虫，能检查[NCRE](https://ncre.neea.edu.cn/)是否开始报名、成绩是否出了，并推送微信通知。

调整ncre.py中的设置：

1. 修改check_content为想要检查的内容。
2. 如果想要推送微信通知，将sendkey设为 https://sct.ftqq.com/ 中提供的密钥。

运行方式，任选其一：

1. 前台。适用于ECS。
2. 无窗口：运行run.bat，日志会生成在同一目录。可选创建快捷方式加入开机自启列表。适用于自己的电脑。
3. 作为PaaS应用，访问对应的URL能查看日志。如果会休眠，还必须配合cron服务定期触发唤醒。
