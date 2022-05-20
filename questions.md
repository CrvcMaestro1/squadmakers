# 2da parte, preguntas

## ¿Qué repositorio utilizarías?

PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Server

### 1. Razona tu respuesta

Por cuestiones de tiempo decidí realizar la prueba con PostgreSQL porque resultaba más sencillo usar el ORM de Django
por defecto.

### 2. Crea la sentencia para crear la BBDD y el modelo de datos que requerirías

PostgreSQL

```bash
CREATE DATABASE squadmakers_test OWNER postgres TABLESPACE salesspace;

CREATE TABLE IF NOT EXISTS transactions_joke (
	"id" BIGINT NOT NULL DEFAULT 'nextval(''transactions_joke_id_seq''::regclass)',
	"text" TEXT NOT NULL,
	PRIMARY KEY ("id")
);
```

### 3. Lo mismo que el punto anterior (si lo hiciste con una SQL) pero para un repositorio noSQL

MongoDB

```bash
USE squadmakers_test

db.jokes.insert({id: 1, text="huck Norris sprinkles iron filings on his cappacinos."})
```



