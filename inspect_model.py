import torch

try:
    checkpoint = torch.load("model.pth")
    print("✅ Successfully loaded model.pth")
    print("\n📦 Type of loaded object:", type(checkpoint))

    if isinstance(checkpoint, dict):
        print("🔑 Keys in the checkpoint:", checkpoint.keys())

        if "n_games" in checkpoint:
            print("🎮 Games played:", checkpoint["n_games"])

        if "model_state" in checkpoint:
            print("📦 Model state dict keys (partial):")
            for key in list(checkpoint["model_state"].keys())[:5]:
                print(f"  {key}: {checkpoint['model_state'][key].shape}")
        else:
            print("⚠️ 'model_state' not found. Might be a plain model file.")
    else:
        print("🧠 Seems like this is a raw model state dict (not a full checkpoint).")
        print("Keys in model:", list(checkpoint.keys())[:5])

except Exception as e:
    print("❌ Failed to load model.pth")
    print(e)
