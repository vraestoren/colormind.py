# <img src="http://colormind.io/img/colormind_logo2.png" width="180" style="vertical-align:middle;" /> colormind.py
> Web-API wrapper for [Colormind](http://colormind.io) — an AI-powered color palette generator that learns color styles from photographs, movies, and popular art.

---

## Methods

| Method | Endpoint | Description |
|--------|----------|-------------|
| `get_random_color_palette(model)` | `POST /api/` | Generate a random 5-color palette using a given model (`default` by default) |
| `get_color_suggestions(input, model)` | `POST /api/` | Generate a palette based on input colors — use `"N"` for colors you want Colormind to fill in |
| `get_models()` | `GET /list/` | Get a list of all currently available color models |
