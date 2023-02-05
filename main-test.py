
# import generate_image
# import notion_api
# import cv2
# import io

# import numpy as np
# import base64
# import io
# from PIL import Image

# app = FastAPI()

# @app.get("/")
# def root():
#     return "Hello World!"

# @app.get("/generate/")
# async def generate(
#     name : str,
#     taster : str,
#     extraction : str,
#     roasting : str    
#     ):
#     note = "#시트러스 #카라멜&초콜렛 #오랜지 #너티"
#     now_date = "2023년 01월 24일    오후 8시 33분"

#     token = 'secret_pfVsdKcZ2RPQ39FChQroGdFLL2RvMewK4ZnXr0o7yaB'
#     database_id = 'dbe8cda90030425a933d3a49eb7ebd72'

#     page_id= "4a154644-2025-48a7-bf30-d20acc8d7515"

#     imgs        = notion_api.getImages(token, database_id)
#     photo_table = next((table for table in imgs if table["id"] == page_id), None)
#     photo       = notion_api.return_random_img_from_table(photo_table)

#     font_path = "NaverNanumSquareNeo/OTF/"
#     font_name1 = "NanumSquareNeoOTF-eHv.otf"
#     font_name2 = "NanumSquareNeoOTF-bRg.otf"
#     font_name3 = "NanumSquareNeoOTF-aLt.otf"

#     img = photo.copy()
#     upper_title     = generate_image.make_title_object(img, font_path, font_name1, font_name2, name, taster, extraction, roasting)
#     img             = generate_image.add_upper_background(img, font_path, font_name1, font_name2, upper_title)
#     img             = generate_image.add_title(img, font_path, font_name1, font_name2, upper_title)
#     lower_note      = generate_image.make_note_object(img, font_path, font_name2, font_name3, upper_title[2], note, now_date)
#     image_add_lower = generate_image.add_lower_background(img, font_path, font_name2, font_name3, lower_note)
#     img_result      = generate_image.add_note(image_add_lower, img, font_path, font_name2, font_name3, lower_note)
    
#     img_result = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)
    
#     PIL_image = Image.fromarray(np.uint8(img_result))
#     img_buffer = io.BytesIO()
#     PIL_image.save(img_buffer, format = 'png')
#     img_buffer.seek(0)

#     str_equivalent_image = base64.b64encode(img_buffer.getvalue()).decode()


#     html_content = """<img src='data:image/png;base64,"""+ str_equivalent_image+ "'/>"
#     return HTMLResponse(content=html_content, status_code=200)

# src = cv2.imread("test_folder/image2.jpeg", cv2.IMREAD_COLOR)
# font_path = "NaverNanumSquareNeo/OTF/"

# font_name1 = "NanumSquareNeoOTF-eHv.otf"
# font_name2 = "NanumSquareNeoOTF-bRg.otf"
# font_name3 = "NanumSquareNeoOTF-aLt.otf"

# name = '콜롬비아 엘 엔칸토 카투라 허니 시트러스'
# taster = "important_131"
# extraction = "chorogi"
# roasting = "momos_coffee"

# note = "#시트러스 #카라멜&초콜렛 #오랜지 #너티"
# now_date = "2023년 01월 24일    오후 8시 33분"

# background_color = (0,165,255)
# img = src.copy()
# upper_title     = generate_image.make_title_object(img, font_path, font_name1, font_name2, name, taster, extraction, roasting)
# img             = generate_image.add_upper_background(img, font_path, font_name1, font_name2, upper_title)
# img             = generate_image.add_title(img, font_path, font_name1, font_name2, upper_title)
# lower_note      = generate_image.make_note_object(img, font_path, font_name2, font_name3, upper_title[2], note, now_date)
# image_add_lower = generate_image.add_lower_background(img, font_path, font_name2, font_name3, lower_note)
# img_result      = generate_image.add_note(image_add_lower, img, font_path, font_name2, font_name3, lower_note)

# cv2.imwrite('test_folder/test_result.png', img_result)



# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"mesage" : f"Hello {name}"}

    # obj = io.BytesIO()
    # PIL_image.save(obj, format='png')
    # obj.seek(0)

    # data1 = base64.b64encode(obj.read())  # convert to base64 as bytes
    # data1 = base64.b64decode(data1)
    # PIL_image = Image.fromarray(np.uint8(img_result)).convert('RGB')
    # buffered = io.BytesIO()
    # PIL_image.save(buffered, format="png")
    # img2str = base64.b64encode(buffered.getvalue())
    # str2img = base64.b64decode(img2str)

    # cv2.imwrite('test_folder/test_result.png', img_result)

    # res, im_png = cv2.imencode(".png", img_result)

    # return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    # image_page(showing_img = im_png)

    # im_byte = io.BytesIO(im_png.tobytes())

    # html_content = """
    #     <img src={result_img} alt="My Image">
    # """.format(result_img = "image/?showing_img_str={post_img}".format(post_img = img2str))
    # html_content = """
    #     <img src={result_img} alt="My Image">
    # """.format(result_img = "data:image/png;base64,{}".format(str2img))