from PIL import Image
import sys

try:
	picture = Image.open(sys.argv[1])
except:
	print('укажите картинку')
	sys.exit()

width = int(sys.argv[2])
height = int(sys.argv[3])
Format = sys.argv[4]


if picture.size[0] > width and picture.size[1] > height:
	pass
else:
	print('Введите разрешение меньше чем текущее. Должно быть целое число')
	sys.exit()

	
picture.resize((width, height)).save(f"{sys.argv[1]}_{sys.argv[2]}x{sys.argv[3]}.{Format}", Format)



'''
Этот скрипт позволяет изменить размер изображения в пикселях при запуске скрипта надо указать исходное изображение,
длину, ширину, формат jpeg, png, gif. После выполнения скрипта будет вторая картинка.
Пример:
python3 main.py Edle_Weinrebe\,_\'Vitis_vinifera\'_subsp._\'vinifera.jpg 1920 1080 gif
'''
