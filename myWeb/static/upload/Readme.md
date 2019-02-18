# 开发环境

- Windows 10
- Python 3.6.2
- Django 2.1.5
- Pycharm
- Chrome



# 运行方法

- 数据与模型迁移：

  确保满足以上条件，cmd到django项目目录，输入命令：

  ```
  python manage.py makemigrations
  ```

	这时其实是在app（此处我的app为myInfo）下建立 migrations目录，并记录下你所有的关于models.py的改动，比如0001_initial.py.但是这个改动还没有作用到数据库文件，数据库没有增加新的表。

- 继续输入命令：

  ```
  python manage.py migrate
  ```

  接着执行migrate，这时候才真的把作用到数据库文件，产生对应的表。

- 运行服务器：

  ```
   python manage.py runserver 0.0.0.0:8000
  ```

- 在浏览器中访问以下地址，打开则成功。

  ```
  127.0.0.1:8000/index
  ```


> 如果运行不了，直接打开html，将会显示一堆代码，因为没有运行在服务器上，获取不到后端数据。
>
> 如果你按上述方法执行了还是没有成功，建议你问问google，因为我也没试过在我的电脑上运行别人的Django项目。