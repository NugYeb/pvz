# pvz

## how to start

1. 如果未安装poetry，请先安装poetry：

    ```bash
    pip install poetry
    ```
2. 安装依赖：
    
    安装依赖前请自行创建一个虚拟环境
    
    若需要将虚拟环境目录放在项目根目录中
    
    **请将其命名为`.venv`，让gitignore忽略该目录**

    ```bash
    poetry install
    ```
    若默认无虚拟目录，poetry将自动创建一个，会放在用户缓存相关目录中

    如Windows将放在C盘 `AppData\Local\pypoetry\Cache\virtualenvs\`

    所以说推荐新建一个`.venv`虚拟环境在根目录

3. 添加依赖：

    ```bash
    poetry add <package_name>
    ```

    **添加依赖时，poetry会自动在虚拟环境中安装依赖，而不需要手动激活虚拟环境**

    如：`poetry add pytest`

4. 运行：

    ```bash
    poetry run <command>
    ```
    如：`poetry run python main.py`

    poetry run命令会自动激活虚拟环境，无需手动激活进入。

    只要是在根目录下的命令都可以通过poetry run运行，都不需要激活和进入虚拟环境.

5. 编写代码：

    全写在pvz下。