-- DROP ROLE IF EXISTS "Richa";
CREATE ROLE "Richa" WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION;

GRANT CONNECT ON DATABASE cangaço TO Richa;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO Richa;
-- Exemplo de concessão de permissões adicionais
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO Richa;
