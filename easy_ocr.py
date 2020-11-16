# !pip install easyocr,googletrans,gTTS


from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio
import PIL
from PIL import ImageDraw

reader = easyocr.Reader(['en'])
translator = Translator()

img_path = '/content/dd.jpg'


im = PIL.Image.open(img_path)
im

  bounds = reader.readtext(img_path)
  bounds

def draw_boxes(image,bounds,color = 'red',width=2):
	draw = ImageDraw.Draw(image)
	for bound in bounds:
		p0,p1,p2,p3 = bound[0]
		draw.line([*p0,*p1,*p2,*p3],fill=color,width=width)
	return image

draw_boxes(im,bounds)

text = ''
for b in bounds:
  text = text+b[1]+" "
text

print(translator.detect(text))
text_hi = translator.translate(text,dest = 'hi')
text_hi.text

ta_tts = gTTS(text_hi.text,lang='hi')
ta_tts.save('trans.mp3')

Audio('trans.mp3',autoplay=True)