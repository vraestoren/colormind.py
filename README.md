# <img src="http://colormind.io/img/logo_nav.svg" width="80" style="vertical-align:middle;" /> [colormind.py](http://colormind.py)
> Web-API for [Colormind](http://colormind.io) - an AI-powered color palette generator that learns color styles from photographs, movies, and popular art.

---

---

## Usage

```python
from colormind import ColorMind

client = ColorMind()

palette = client.get_random_color_palette()
print(palette)

suggestions = client.get_color_suggestions(
    input=[[44, 43, 44], "N", "N", "N", [239, 237, 230]]
)
print(suggestions)

palette = client.get_random_color_palette(model="landscape")
print(palette)

models = client.get_models()
print(models)
```

---

## Methods

| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_random_color_palette(model)` | `POST /api/` | Generate a random 5-color palette using a given model (`default` by default) |
| `get_color_suggestions(input, model)` | `POST /api/` | Generate a palette based on input colors — use `"N"` for colors you want Colormind to fill in |
| `get_models()` | `GET /list/` | Get a list of all currently available color models |
