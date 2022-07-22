# 导入 Flask 类
from flask import Flask

# 创建了这个类的实例。第一个参数是应用模块或者包的名称。
app = Flask(__name__)


# 使用 route() 装饰器来告诉 Flask 触发函数的 URL
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # 使用 run() 函数来运行本地服务器和我们的应用
    app.run()
