{
    'name': "Floristeria Beni",
    'icon': 'abj_floristeria/static/description/logo.png',
    'summary': "Floristeria familiar, si necesitas un ramo de flores con urgencia, llamanos.",

    'description': """
    Modulo para pequeñas empresas de floristeria, con el que podrás gestionar tus flores, ramos, clientes y pedidos de forma sencilla y eficiente.
    """,

    'author': "AlvaroBenito S.A.",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base', 'contacts'],
    




    'data': [
        'security/ir.model.access.csv',
        'views/Flor.xml',
        'views/Ramo.xml',
        'views/Cliente.xml',
        'views/Pedido.xml',
        'views/menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}

