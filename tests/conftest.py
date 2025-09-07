import pytest
import numpy as np
import cv2
import os

IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "..", "images")

@pytest.fixture()
def blank_image_flat():
    img = np.zeros((300, 300), dtype=np.uint8)
    return img


@pytest.fixture()
def blank_image_gray():
    img = np.zeros((300, 300, 1), dtype=np.uint8)
    return img


@pytest.fixture()
def blank_image():
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    return img


@pytest.fixture()
def blank_empty():
    return np.zeros((0, 0, 1), dtype=np.uint8)


@pytest.fixture()
def blank_singleCh():
    return np.zeros((0, 0, 1), dtype=np.uint8)


@pytest.fixture()
def blank_2D():
    return np.zeros((0, 0), dtype=np.uint8)


testImage_SimpleValid = [
    'blank_image', 'blank_image_flat', 'blank_image_gray',
    'blank_empty', 'blank_singleCh', 'blank_2D'
]


loadedCatImage = cv2.imread(os.path.join(IMAGE_FOLDER, "cat.jpg"), 1)


@pytest.fixture()
def cat_full_shape():
    return loadedCatImage.copy()


@pytest.fixture()
def cat_gray():
    img = cv2.cvtColor(loadedCatImage, cv2.COLOR_BGR2GRAY)
    return img


@pytest.fixture()
def cat_gray_3d():
    img = cv2.cvtColor(loadedCatImage, cv2.COLOR_BGR2GRAY)
    img = img.reshape(*img.shape, 1)
    return img


testImage_CatValid = ['cat_full_shape', 'cat_gray', 'cat_gray_3d']

# __all__ = ['testImage_SmimpleValid', 'testImage_CatValid']

testImage_CombinedValid = [*testImage_SimpleValid, *testImage_CatValid]
