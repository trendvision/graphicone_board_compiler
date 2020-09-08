from setuptools import setup

setup(
    name='graphicone_board_compiler',
    url='https://github.com/trendvision/graphicone_board_compiler',
    packages=['graphicone_board_compiler'],
    dependency_link=['git+https://github.com/trendvision/graphicone_models.git#egg=graphicone_models'],
    install_requires=['sqlalchemy'],
    version='0.1',
    license='TRV',
    description='creation board models',
)
