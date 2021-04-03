import io

# нужно ввести pip install pillow tqdm requests
from PIL import Image
from tqdm import tqdm
import requests

N = 164 # число страниц
PDF_FILE = "vlom1.pdf" # куда скачивает книгу
ID = "UmVzb3VyY2UtNTcyOQ/cGFnZTAwMDA" # типа идентификатор книги... сам поймёшь, если глянешь в HTML
URL = "https://e-lib.nsu.ru/reader/service/SecureViewer/Page/{}/{}"

def get_image(url):
    r = requests.get(url, timeout=10.0)
    r.raw.decode_content = True
    im = Image.open(io.BytesIO(r.content))
    return im.resize((round(im.width/2), round(im.height/2)), resample=Image.LANCZOS)

im1 = get_image(URL.format(ID, 1))
im_list = [get_image(URL.format(ID, i)) for i in tqdm(range(2, N+1))]

im1.save(PDF_FILE, "PDF", resolution=100.0, save_all=True, append_images=im_list, optimize=True)