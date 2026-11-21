{
    "name": "Préstamo de equipo UNICAH",
    "version": "1.0.0",
    "summary": "Control de equipos, préstamos y devoluciones",
    "category": "Services",
    "author": "Astrid Jissel Giron Diaz",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.access.csv",
        "data/prestamo_equipo_data.xml",
        "views/prestamo_equipo_views.xml",
        "views/prestamo_views.xml",
        "views/res_partner_views.xml",
    ],
    "application": True,
    "license": "LGPL-3",
    "installable": True,
}
