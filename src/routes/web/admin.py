from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.get("/")
def index():  # TODO
    """
    @route GET /admin
    @desc Visit admin homepage
    @access Private
    """
    pass


# region children
@admin.get("/deti")
def children():  # TODO
    """
    @route GET /deti
    @desc Show list of children
    @access Private - leader & admin only
    """
    pass


@admin.get("/deti/<child_id>")
def child(child_id):  # TODO
    """
    @route GET /deti/<child_id>
    @desc Show details about 1 child
    @access Private
    """
    pass


@admin.get("/deti/pridat")
def create_child():  # TODO
    """
    @route GET /deti/pridat
    @desc Show form for adding new child
    @access Private
    """
    pass


@admin.get("/deti/<child_id>/upravit")
def update_child(child_id):  # TODO
    """
    @route GET /deti/<child_id>/upravit
    @desc Show form for updating 1 child
    @access Private - parent & admin only
    """
    pass


# endregion

# region groups
@admin.get("/skupiny")
def groups():  # TODO
    """
    @route GET /skupiny
    @desc Show list of groups
    @access Private
    """
    pass


@admin.get("/skupiny/<group_id>/")
def group(group_id):  # TODO
    """
    @route GET /skupiny/<group_id>
    @desc Show details about 1 group
    @access Private
    """
    pass


@admin.get("/skupiny/vytvorit")
def create_groups():  # TODO
    """
    @route GET /skupiny/vytvorit
    @desc Show form for creating group
    @access Private - admin only
    """
    pass


@admin.get("/skupiny/<group_id>/upravit")
def update_group(group_id):  # TODO
    """
    @route GET /skupiny/<group_id>/upravit
    @desc Show form for updating group
    @access Private - admin only
    """
    pass


# endregion

# region events
@admin.get("/akce")
def events():  # TODO
    """
    @route GET /akce
    @desc Show list of events
    @access Private
    """
    pass


@admin.get("/akce/<event_id>")
def event(event_id):  # TODO
    """
    @route GET /akce/<event_id>
    @desc Show details of 1 event
    @access Private
    """
    pass


@admin.get("/akce/vytvorit")
def create_event():  # TODO
    """
    @route GET /akce/vytvorit
    @desc Show form for creating event
    @access Private - leader & admin only
    """
    pass


@admin.get("/akce/<event_id>/upravit")
def update_event(event_id):  # TODO
    """
    @route GET /akce/<event_id>/upravit
    @desc Show form for updating event
    @access Private - leader & admin only
    """
    pass
# endregion
