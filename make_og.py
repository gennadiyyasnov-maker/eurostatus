from PIL import Image

# Setup
bg_color = (11, 32, 70) # #0B2046
width, height = 1200, 630

# Create blank image with background color
og_image = Image.new('RGB', (width, height), bg_color)

# Load logo
logo_path = r"public\assets\images\logo_light.png"
try:
    logo = Image.open(logo_path)
    # Resize logo if it's too big, maintaining aspect ratio. 
    # Let's say max width 600 or max height 200 for aesthetic padding
    logo.thumbnail((800, 250), Image.Resampling.LANCZOS)
    
    # Calculate position to center
    x = (width - logo.width) // 2
    y = (height - logo.height) // 2
    
    # Paste logo using its alpha channel as mask
    og_image.paste(logo, (x, y), logo if logo.mode == 'RGBA' else None)
    
except Exception as e:
    print(f"Failed to process logo: {e}")

# Save
out_path = r"public\assets\images\og_image.png"
og_image.save(out_path)
print("Saved branded OG image!")
