from dotenv import load_dotenv
load_dotenv()  # 加载 .env 文件中的环境变量

from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)