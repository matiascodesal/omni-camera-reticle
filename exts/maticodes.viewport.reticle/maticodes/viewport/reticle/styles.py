from pathlib import Path

import omni.ui as ui

from maticodes.viewport.reticle import constants


CURRENT_PATH = Path(__file__).parent.absolute()
ICON_PATH = CURRENT_PATH.parent.parent.parent.joinpath("icons")

safe_areas_group_style = {
    "Label:disabled": {
        "color": 0x55FFFFFF
    },
    "FloatSlider:enabled": {
        "draw_mode": ui.SliderDrawMode.HANDLE,
        "background_color": 0xFFBBBBBB,
        "color": 0xFF000000
    },
    "FloatSlider:disabled": {
        "draw_mode": ui.SliderDrawMode.HANDLE,
        "background_color": 0x55BBBBBB,
        "color": 0x55FF0000
    },
    "CheckBox": {
        "background_color": 0xFFBBBBBB,
        "color": 0xFF000000
    },
    "Rectangle::ActionSwatch": {
        "background_color": constants.DEFAULT_ACTION_SAFE_COLOR
    },
    "Rectangle::TitleSwatch": {
        "background_color": constants.DEFAULT_TITLE_SAFE_COLOR
    },
    "Rectangle::CustomSwatch": {
        "background_color": constants.DEFAULT_CUSTOM_SAFE_COLOR
    }
}
comp_group_style = {
    "Button.Image::Off": {
        "image_url": str(ICON_PATH / "off.png")
    },
    "Button.Image::Thirds": {
        "image_url": str(ICON_PATH / "thirds.png")
    },
    "Button.Image::Quad": {
        "image_url": str(ICON_PATH / "quad.png")
    },
    "Button.Image::Crosshair": {
        "image_url": str(ICON_PATH / "crosshair.png")
    },
    "Button:checked": {
        "background_color": 0x33FFFFFF
    }
}
