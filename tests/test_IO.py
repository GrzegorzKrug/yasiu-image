import pytest
import numpy as np
import os

from yasiu_image.io import *

TEST_GIF_PATHS = ['test.gif']


@pytest.mark.parametrize('fileName', TEST_GIF_PATHS)
def test2_equal(fileName, request):
    # cat_pic = request.getfixturevalue(fix_name)
    pass
