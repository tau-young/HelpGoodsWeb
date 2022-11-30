# HelpGoodsWeb

本项目是上海交通大学 CS-3331 软件工程课程大作业，同时也是 [Help-Goods](https://github.com/tau-young/Help-Goods) 项目的 GUI 版本，但是经过了完全的重构。

原项目采用 CLI 形式，由 Python Script 写成，理论上是跨平台的，只要安装了 Python 3.y 解释器就能运行。本项目使用 Django 制作成网页应用，因此在任何浏览器上都能运行。

## 作业描述

[原始页面](https://oc.sjtu.edu.cn/courses/48894/assignments/193007)（仅限该课程参与人员有权访问）

> ### “你帮我助”软件开发（Final)
>
> #### 新的功能需求：
>
> 1. 物品有公共的信息（物品名称，物品说明，物品所在地址，联系人手机，邮箱）。为了便于管理和查询，物品可以分成不同的类别（例如食品、书籍、工具等），不同类别的物品可能有不同的属性（例如食品有保质期，数量；书籍有作者，出版社等）。
> 2. 互帮互助系统有两种类型的用户：管理员和普通用户。
> - 管理员可以设置新的物品类型（定义物品类型的名称和各个属性），修改物品类型。
> - 普通用户在添加物品时先选择物品类型，然后再填入物品信息。普通用户搜寻物品时，需要先选择类型，再输入关键字，关键字可以再用户名称和说明中进行匹配。
> 普通用户需要注册（填入基本信息，包括住址，联系方式等），管理员批准后才能成为正式用户。
>
> 3. 为了便于使用上述功能，软件需要提供 GUI。
>
> #### 文档需求：
>
> 1. 需要提供一个文档：其中包括（1）用例模型；（2）针对用例画顺序图；（3）类图。
>
> #### 作业完成要求：
>
> 作业需要在 16 周前提交，并发布在你的 GitHub 仓库中；
> 作业完成后需要进行演示，请提前一周与助教约好。（每周周二下午都可以约）；演示的内容包括写的文档、软件的功能（包括第一次，第二次功能）。
> 在技术博客上写一篇总结文章，对照软件工程的知识，对开发该程序的体会进行总结。

## 开发进度

- [x] 用户认证与登录
	- [x] 登录界面
	- [x] 注册界面
	- [x] 用户详细信息界面
	- [x] 用户模型
	- [x] 登录逻辑
	- [x] 注册逻辑
	- [ ] 美化用户界面
- [x] 物品展示界面
	- [x] 物品添加界面
	- [ ] 物品编辑界面
- [ ] 管理员后台界面