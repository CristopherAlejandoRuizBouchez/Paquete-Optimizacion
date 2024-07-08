from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete de optimizacion '
LONG_DESCRIPTION = 'Mi primer paquete de optimizacion '

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="PAQUETEOPTIMIZACION", 
        version=VERSION,
        author="Cristopher Alejandro Ruiz Bouchez",
        author_email="<cristopher10mc@gmail.com>",
        url = "https://github.com/CristopherAlejandoRuizBouchez/Paquete-Optimizacion",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)