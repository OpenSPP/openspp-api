{
    "name": """OpenSPP REST API: API Records""",
    "summary": """RESTful API routes for OpenSPP""",
    "category": "",
    "version": "15.0.0.0.0",
    "application": False,
    "author": "OpenSPP.org",
    "development_status": "Alpha",
    "website": "https://github.com/openspp/openspp-api",
    "license": "LGPL-3",
    "depends": [
        "spp_api",
        "spp_service_points",
    ],
    "data": [
        "data/spp_api_namespace_data.xml",
        "data/spp_api_path_data.xml",
        "views/spp_service_point_views.xml",
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
