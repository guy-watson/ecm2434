# Django-Marker-Map
# Setup

```bash
pip install django
```

```
pip install psycopg2-binary
```

```
pip install django-filter
```

```
pip install djangorestframework
```

```
pip install djangorestframework-gis
```

Download OSGeo4W (for GDAL and GEOS) - https://trac.osgeo.org/osgeo4w/

add the filepaths for the gdal and geos_c files in the OSGeo4W bin to the settings.py (after GDAL_LIBRARY_PATH and GEOS_LIBRARY_PATH)

Download and Install 'PostgreSQL' - https://www.postgresql.org/
 - after installation, remember your password and use the StackBuilder to download the PostGIS Extension

add the filepath to the PostgreSQL bin folder to system environment variables if necessary (PATH)

```
psql -U postgres
```

(input password)

```
CREATE DATABASE mapdatabase WITH ENCODING 'UTF8' LC_COLLATE='English_United Kingdom' LC_CTYPE='English_United Kingdom';
```

```
\c mapdatabase
```

```
CREATE EXTENSION postgis;
```


make sure to add the correct port, name, database name, host, password etc. to the setting.py file

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

```
python3 manage.py runserver
```

#Customization

the scale to which the map is zoomed in, along with where it is centred upon (if location unknown / denied) can be changed in lines 6/7 of the map.js file (located in map/markers/static/map.js)

to add markers to the map, create a superuser before running the server:

```
python3 manage.py createsuperuser
```

and then go to the admin page where you can add and delete markers
