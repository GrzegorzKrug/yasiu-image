import cv2 as _cv2
import numpy as _np


def resize_with_aspect_ratio(orig, resize_key='outer', new_dim=150):
    """

    :param sequence:
    :param resize_key:
        - outer
        - inner
        - height
        - width

    :param new_dim:
    :return:
    """
    h, w, c = orig.shape

    h_w_ratio = h / w
    w_h_ratio = w / h

    if h >= w and resize_key == 'outer':
        new_h = new_dim
        new_w = new_dim * w_h_ratio

    elif w >= h and resize_key == 'outer':
        new_w = new_dim
        new_h = new_dim * h_w_ratio

    elif resize_key == "height":
        new_h = new_dim
        new_w = new_dim * w_h_ratio

    elif resize_key == "width":
        new_w = new_dim
        new_h = new_dim * h_w_ratio

    elif h < w and resize_key == 'inner':
        new_h = new_dim
        new_w = new_dim * w_h_ratio
    else:
        new_w = new_dim
        new_h = new_dim * h_w_ratio

    new_h = _np.round(new_h).astype(int)
    new_w = _np.round(new_w).astype(int)

    # print(f"Resize: kwarg: {kwarg}")
    # sequence = [imutils.resize(fr, **kwarg) for fr in sequence]
    ret = _cv2.resize(orig, (new_w, new_h))
    return ret


def downscale_with_aspect_ratio(orig, resize_key='outer', max_dimension=150):
    """
    Scales picture down if size exceeds give dimension.


    :param orig:


    :param resize_key: specify which axis to resize
    :type resize_key: float

    resize_key:
        #. `outer` : resize bigger axis
        #. `inner` : resize smaller axis
        #. `height`: check height size
        #. `width` : check width size
    :type: str


    :type resize_key: str

    :param max_dimension:
    :return:
    """
    h, w, c = orig.shape

    h_w_ratio = h / w
    w_h_ratio = w / h

    if h >= w and resize_key == 'outer' and h > max_dimension:
        new_h = max_dimension
        new_w = max_dimension * w_h_ratio

    elif w >= h and resize_key == 'outer' and w > max_dimension:
        new_w = max_dimension
        new_h = max_dimension * h_w_ratio

    elif resize_key == "height" and h > max_dimension:
        new_h = max_dimension
        new_w = max_dimension * w_h_ratio

    elif resize_key == "width" and w > max_dimension:
        new_w = max_dimension
        new_h = max_dimension * h_w_ratio

    elif h < w and resize_key == 'inner' and h < max_dimension:
        new_h = max_dimension
        new_w = max_dimension * w_h_ratio
    elif w < h and resize_key == 'inner' and w < max_dimension:
        new_w = max_dimension
        new_h = max_dimension * h_w_ratio
    else:
        return orig

    new_h = _np.round(new_h).astype(int)
    new_w = _np.round(new_w).astype(int)

    # print(f"Resize: kwarg: {kwarg}")
    # sequence = [imutils.resize(fr, **kwarg) for fr in sequence]
    ret = _cv2.resize(orig, (new_w, new_h))
    return ret


def squerify(img: _np.ndarray, /, offset_val=0, *, type_="clip"):
    """

    :param img:
    :param type_:
    :param offset_val:
    :return:
    """

    is_3d = len(img.shape) == 3
    if is_3d:
        H, W, C = img.shape
    else:
        H, W = img.shape
        C = None

    if H == W:
        "Square already"
        return img

    if type_ == "clip":
        offset = abs(H - W)
        pos = (_np.clip(offset_val, -1, 1) + 1) / 2

        first = (offset * pos).round().astype(int)
        second = first - offset
        if second == 0:
            second = None

        if H > W:
            new_img = img[first:second, :]
        else:
            new_img = img[:, first:second]

        # print("new shape", new_img.shape)
        return new_img
    else:
        raise KeyError("Only clip supported")


__all__ = [
    'squerify',
    'resize_with_aspect_ratio',
    'downscale_with_aspect_ratio',
]


if __name__ == "__main__":
    import os
    img = _cv2.imread(os.path.join(os.path.dirname(__file__), "cat.jpg"))
    img = downscale_with_aspect_ratio(img, max_dimension=500)
    img = img[200:, :, :]

    _cv2.imshow("Orig", img)

    sq = squerify(img, -1)
    _cv2.imshow("Cat Square -1", sq)
    sq = squerify(img, 0)
    _cv2.imshow("Cat Square 0 ", sq)
    sq = squerify(img, 1)
    _cv2.imshow("Cat Square 1", sq)
    _cv2.waitKey()
