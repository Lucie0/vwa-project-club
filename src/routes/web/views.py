from flask import Blueprint, render_template

web = Blueprint("web", __name__)


@web.get("/")
def index():
    """
    @route GET /
    @desc Visit homepage
    @access Public
    """
    return render_template("views/index.jinja")


@web.get("/onas")
def about():  # TODO
    """
    @route GET /onas
    @desc Visit about page
    @access Public
    """
    pass


@web.get("/galerie")
def gallery():  # TODO
    """
    @route GET /galerie
    @desc Visit image gallery page
    @access Public
    """
    pass


@web.get("/kontakt")
def contact():  # TODO
    """
    @route GET /kontakt
    @desc Visit contact page
    @access Public
    """
    pass


@web.get("/prihlaseni")
def login():  # TODO
    """
    @route GET /prihlaseni
    @desc Visit login page
    @access Public
    """
    pass


@web.get("/registrace")
def register():  # TODO
    """
    @route GET /registrace
    @desc Visit registration page
    @access Public
    """
    pass


# region SEO
@web.get("/robots.txt")
def robots():  # TODO
    """
    @route GET /robots.txt
    @desc Return file for SEO indexing
    @access Public
    """
    pass


@web.get("/sitemap.xml")
def sitemap():  # TODO
    """
    @route GET /sitemap.xml
    @desc Return file for SEO improvement
    @access Public
    """
    pass
# endregion
