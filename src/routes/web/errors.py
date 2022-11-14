from flask import Blueprint

err = Blueprint("error", __name__)


@err.app_errorhandler(403)
def forbidden_access(e):
    """
    @desc Custom error handler for 403 - Forbidden
    """
    pass


@err.app_errorhandler(404)
def page_not_found(e):
    """
    @desc Custom error handler for 404 - Not Found
    """
    pass
