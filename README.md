# Readme of `yasiu-image`

Module with useful math functions that are missing in numpy or scipy.

## Installation

```shell
pip install yasiu-image
```

## Submodules
- `common` - Read write features
- `features` - Transform images into features and back
- `filters` - Modify images but keep original shape
- `modifiers` - Change output images
- `quality` - Compare image quality


## Sequence reader Generators

- `read_webp_frames` - generator
- `read_gif_frames` - generator
- `save_image_list_to_gif` - save sequence using Pillow

### Use example:

```py
from yasiu.image.common import read_gif_frames
```


frames = list(read_gif_frames(path))
```

# All packages

[1. Native Package](https://pypi.org/project/yasiu-native/)

[2. Math Package](https://pypi.org/project/yasiu-math/)

[3. Image Package](https://pypi.org/project/yasiu-image/)

[4. Pyplot visualisation Package](https://pypi.org/project/yasiu-vis/)
