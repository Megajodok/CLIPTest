import torch
import clip
from PIL import Image

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Modell und Vorverarbeitung laden
    model, preprocess = clip.load("ViT-B/32", device=device)

    # Text-Beschreibungen
    texts = [
        "a photo of a dog",
        "a photo of a cat",
        "a photo of a mountain",
        "a blue square"
    ]
    text_tokens = clip.tokenize(texts).to(device)

    # Dummy-Bild (einfarbiges Bild zum Testen)
    #img = Image.new("RGB", (224, 224), color="blue")
    img = Image.open("images/frieda.jpg")
    image_input = preprocess(img).unsqueeze(0).to(device)

    # Embeddings berechnen
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_tokens)

        # Normalisieren
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        # Cosine Similarity
        sims = (image_features @ text_features.T).squeeze(0)

    print("\nSimilarity Scores:")
    for desc, score in zip(texts, sims):
        print(f"{desc:25s} -> {score.item():.4f}")

if __name__ == "__main__":
    main()
