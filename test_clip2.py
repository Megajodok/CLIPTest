import torch
import clip
from PIL import Image

model, preprocess = clip.load("ViT-B/32")
device = "cpu"

img1 = preprocess(Image.open("images/frieda.jpg")).unsqueeze(0).to(device)
img2 = preprocess(Image.open("images/frieda.jpg")).unsqueeze(0).to(device)

with torch.no_grad():
    f1 = model.encode_image(img1)
    f2 = model.encode_image(img2)

    f1 /= f1.norm(dim=-1, keepdim=True)
    f2 /= f2.norm(dim=-1, keepdim=True)

sim = (f1 @ f2.T).item()
print("Bildähnlichkeit:", sim)
