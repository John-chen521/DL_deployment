import os
from flask import Flask, render_template, request, redirect
import io
from PIL import Image
import uuid
import vision

app = Flask(__name__)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FOLDER = os.path.join(CURRENT_DIR, 'static/')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        # 读取上传的图像
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        # 获得分类结果
        image_result, class_name, class_id = vision.classify_image(image)
        # 将图像保存于本地
        img_stream = str(uuid.uuid1()) + ".jpg"
        cache_name = CACHE_FOLDER + "/" + img_stream
        image_result.savefig(cache_name, dpi=300, bbox_inches='tight')

        # 传递至模板
        return render_template('result.html',
                               class_id=class_id,
                               class_name=class_name,
                               img_name='结果图像保存于/static/' + img_stream)
    return render_template('index.html')


if __name__ == '__main__':
    # 地址需要是0.0.0.0，保证外机访问
    app.run(host="0.0.0.0", debug=True, port=5000)
