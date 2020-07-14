Sphinx Theme for Shuup Documentation
====================================

This is a Sphinx theme for Shuup's documentation.

The theme is a fork of `Read the Docs Sphinx Theme
<https://github.com/snide/sphinx_rtd_theme>`.


Development
===========

1. Install requirements `pip install -r requirements.txt`
2. Install npm packages `npm i`
3. Run the dev server `npm run dev`
4. Refresh the page after the browser tab opens up and it says "Cannot GET /"

This will launch the dev server on port 2000.
All changes made to the theme will be automatically get refreshed on the dev server.


Development with shuup-guide
============================

To se changes made to the theme in the shuup-guide you will need to do the following:

1. Install requirements `pip install -r requirements.txt`
2. Install npm packages `npm i`
3. Build the static files `npm run build`
4. Follow the steps in the shuup-guide readme


Updating theme/pushing new updates
===================================

To update the theme to contain latest change just run `python setup.py build` and then commit your changes.
