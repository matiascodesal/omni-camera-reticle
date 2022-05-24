import traceback

import omni.ext
import omni.ui as ui

from maticodes.viewport.reticle.models import ReticleModel
from maticodes.viewport.reticle.reticle import ReticleOverlay


class CleanupError(Exception):
    pass


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class CameraReticleExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.

    def on_startup(self, ext_id):
        print("[maticodes.viewport.reticle] CameraReticleExtension startup")
        windows = ui.Workspace.get_windows()
        for window in windows:
            if window.title.startswith("Viewport"):
                CameraReticleExtension.create_new_reticle_overlay(window)
        ui.Workspace.set_window_created_callback(CameraReticleExtension.on_window_created)

    @staticmethod
    def create_new_reticle_overlay(vp_win):
        reticle_model = ReticleModel()
        reticle = ReticleOverlay(reticle_model, vp_win)
        reticle.build_viewport_overlay()

    @staticmethod
    def on_window_created(win_handle):
        """Add a new ReticleOverlay whenever a new viewport window is created.

        Args:
            win_handle (WindowHandle): The window that was created.
        """
        if win_handle.title.startswith("Viewport"):
            CameraReticleExtension.create_new_reticle_overlay(win_handle)

    def on_shutdown(self):
        """ Executed when the extension is disabled.

        TODO:
            * Overlay widgets are not removed on shutdown and users can still click on
            the Reticle button and produce an error.
            * I think object references are still being held on for callbacks. I need make sure everything is destroyed.

        Raises:
            CleanupError: Error occurred trying to destroy ReticleOverlay instances.
        """
        print("[maticodes.viewport.reticle] CameraReticleExtension shutdown")
        exception_raised = False
        # Need to explicitly destroy the ViewportWidgets otherwise they'll stick around and consume
        for instance in ReticleOverlay.get_instances():
            try:
                instance.destroy()
            except Exception:
                traceback.print_exc()
                exception_raised = True

        if exception_raised:
            raise CleanupError("One more more exceptions were raised when trying to destroy ReticleOverlay instances.")
