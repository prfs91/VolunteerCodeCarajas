Model and Form Expansion & Admin and Template Improvements

Model and Form Expansion & Admin and Template Improvements

- Created `base.html` with global layout and Bootstrap integration.

# 📋 CHANGELOG

Todas as mudanças significativas neste projeto serão documentadas neste arquivo.

O formato segue parcialmente o padrão [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- (Planeje aqui futuras adições ainda não feitas)

### Changed

- (Documente aqui mudanças que ainda não foram lançadas)

---

## [2025-04-15] - Model and Form Expansion & Admin and Template Improvements

### Added

- Created `CHANGELOG.md` to track changes.
- Created `base.html` with global layout and Bootstrap integration.

### Changed

- Expanded the `Associado` model in the `associados` app to include legal, accessibility, and socioeconomic data fields.
- Expanded the `form.py` to include all new fields added to the `Associado` model, grouped by categories (personal data, contact and address, disability details, legal documentation, legal guardian, and socioeconomic information) to improve data collection.
- Refactored `cadastrar.html` to extend `base.html` and apply Bootstrap styling.
- Refactored `lista.html` to extend `base.html` and apply Bootstrap styling.
- Set the global template directory in `settings.py` by updating `TEMPLATES['DIRS']` to include `[BASE_DIR / 'templates']`.
- Improved the `Associado` admin interface by extending the list display, adding filters (e.g., by disability type, sex, marital status), and making key fields (like `data_entrada` and `numero_associado`) read-only.
- Fixed migration issues to reflect the addition and changes of fields in the `Associado` model.
- Adjusted tests to correctly verify the behavior of the `Associado` model with the new fields.
- Fixed an error in the `save` method of the `Associado` model when generating the automatic number for an associate.
- Removed the non-editable `data_entrada` field from the form and adjusted its template to display it as read-only.
- Refactored view logic: fixed the use of `request.FILES`, added missing redirect import, and implemented success messages.
- Updated `requirements.txt` with the latest dependencies from the environment.

### Fixed

- Corrected environment activation path in `start.ps1`.

### Removed

- Nothing removed in this version.
