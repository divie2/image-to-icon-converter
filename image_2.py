from PIL import Image
filename = r'C:\Users\USER\Pictures\Camera Roll\jjjj.jpg'
img = Image.open(filename)
img.save('logo.ico')

# ====================

# Optionally, you may specify the icon sizes you want:

icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save('logo.ico', sizes=icon_sizes)