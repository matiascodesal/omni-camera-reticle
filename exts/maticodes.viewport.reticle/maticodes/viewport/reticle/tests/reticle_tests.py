""" Tests Module

TODO:
    * Write actual tests.
"""

from pathlib import Path
from typing import Optional

import carb
import omni.kit
import omni.ui as ui
from omni.ui.tests.test_base import OmniUiTest

from maticodes.viewport.reticle.extension import CameraReticleExtension


CURRENT_PATH = Path(__file__).parent.joinpath("../../../../data")


class TestReticle(OmniUiTest):
    # Before running each test
    async def setUp(self):
        await super().setUp()
        self._golden_img_dir = CURRENT_PATH.absolute().resolve().joinpath("tests")
        self._all_widgets = []
        self._settings = carb.settings.get_settings()
        self._original_value = self._settings.get_as_int("/persistent/app/viewport/displayOptions")
        self._settings.set_int("/persistent/app/viewport/displayOptions", 0)

        # Create test area
        await self.create_test_area(256, 256)
        window_flags = ui.WINDOW_FLAGS_NO_SCROLLBAR | ui.WINDOW_FLAGS_NO_TITLE_BAR | ui.WINDOW_FLAGS_NO_RESIZE
        self._test_window = ui.Window(
            "Viewport",
            dockPreference=ui.DockPreference.DISABLED,
            flags=window_flags,
            width=256,
            height=256,
            position_x=0,
            position_y=0,
        )
        # Override default background
        self._test_window.frame.set_style({"Window": {"background_color": 0xFF000000, "border_color": 0x0, "border_radius": 0}})

        await omni.kit.app.get_app().next_update_async()
        await omni.kit.app.get_app().next_update_async()

    # After running each test
    async def tearDown(self):
        self._golden_img_dir = None
        self._test_window = None
        self._settings.set_int("/persistent/app/viewport/displayOptions", self._original_value)
        await super().tearDown()

    async def test_reticle_menu_button(self):
        await self.finalize_test(golden_img_dir=self._golden_img_dir, golden_img_name="test_reticle_menu_button.png")
