def setup_routes(app, handler):

    router = app.router
    h = handler

    router.add_get('/', h.index, name='index')
