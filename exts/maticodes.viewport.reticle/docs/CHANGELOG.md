# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.3.0] - 2022-07-10
### Added
- `omni.kit.viewport.utility` dependency.

### Changed
- Refactored to use `omni.kit.viewport.utility`. (Only works with Kit 103.1.2+ now.)
- Renamed `reticle.py` to `views.py`
- Moved **Reticle** button to the bottom right of the viewport instead of bottom left.

## [1.2.0] - 2022-05-24
### Changed
- Refactored to use VP1 instead of hybrid VP1/2
- Renamed "draw" functions to "build"
- Moved color constants to omni.ui.color

## [1.1.0] - 2022-03-31
### Changed
- Improved the cleanup code when the extension is shutdown.

## [1.0.0] - 2022-03-28
### Added
- Added extension icon
- Applies overlay to all existing viewports on extension startup
- Added docstrings
- Refactored to use Model-View pattern
- Now supports when viewport is narrower than the render resolution aspect ratio.

## [0.1.0] - 2022-03-25
### Added
- Initial add of the Camera Reticle extension.