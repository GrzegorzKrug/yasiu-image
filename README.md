# Readme of `yasiu.image`

Module with useful math functions that are missing in numpy or scipy.

## Installation

```shell
pip install yasiu.image
```

## Sequence reader Generators
   - `read_webp_frames` - generator
   - `read_gif_frames` - generator
   - `save_image_list_to_gif` - save sequence using Pillow

### Import:

```py
from yasiu.image import read_gif_frames
```

### Use example:

```py
frames = list(read_gif_frames(path))
```