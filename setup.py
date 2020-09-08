from setuptools import setup

setup(
    name='graphicone_social_relations',
    url='https://github.com/trendvision/graphicone_social_relations',
    packages=['graphicone_social_relations'],
    dependency_link=['git+https://github.com/trendvision/graphicone_models.git#egg=graphicone_models'],
    install_requires=['sqlalchemy'],
    version='0.1',
    license='TRV',
    description='relations between users',
)
