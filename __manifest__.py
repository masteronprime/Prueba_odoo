{
    'name': 'Prueba Odoo',
    'version': '17.0.0.0.0',
    'author': 'Ray Marcelo',
    'website': '',
    'category': '',
    'summary': 'Manage fields and views for Stock,Products',
    'description': """
    """,
    'depends': [
        'base', 'product', 'stock' , 'account','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bottom_smart.xml',
        'views/wizard_tag_product.xml',
        'views/product_label.xml',
        'report/product_report.xml',
        'views/product_report_buttom.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'Other proprietary',
    'currency': 'USD',
    'price': 0
}