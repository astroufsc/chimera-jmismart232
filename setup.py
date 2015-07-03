from distutils.core import setup

setup(
    name='chimera-jmismart232',
    version='0.0.1',
    packages=['chimera_jmismart232', 'chimera_jmismart232.instruments'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-jmismart232',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    install_requires=['pyserial'],
    description='Chimera plugin for JMI Smart 232 serial focusers'
)
