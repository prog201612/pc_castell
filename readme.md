
## BD
- tipus de panells (choices): Carousel,
- panells
    - Inlines: productes del panell
- categories (Producte)
- productes

index.html
- Panells (Dinàmics)
    
## Deploy on PythonAnyWhere
[Deploy an existing Django project](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject)

## Continguts
Important la funció `translate_panels` de `store.helpers.py` que és la que genera el contingut amb la traducció correcte dels objectes que s'alimentarà la plantilla.

## Migració per crear el registre únic de la taula store.models.Config
```bash
python manage.py makemigrations --empty store
# store/migrations/0011_auto_20250421_1445.py
```

Al registre de configuració hi posem les dades amb català i les traduïm a Translates.