import colorgram

def extract_colors(image, colors):
    """Extract colors from image and returns a list of RGB tuples."""
    colors = colorgram.extract(image, colors)
    colors = [color.rgb for color in colors]
    colors = [(rgb.r, rgb.g, rgb.b) for rgb in colors]
    return colors

# colors = extract_colors('image.webp', 30)