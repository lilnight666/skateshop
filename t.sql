-- Role: pg_database_owner
DO $$ 
BEGIN 
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pg_database_owner') THEN 
    CREATE ROLE pg_database_owner WITH
      NOLOGIN
      NOSUPERUSER
      INHERIT
      NOCREATEDB
      NOCREATEROLE
      NOREPLICATION;
  END IF;
END $$;
SELECT datname FROM pg_database WHERE datname = 'cangaço';

GRANT CONNECT, CREATE, USAGE ON DATABASE cangaço TO "Richa";

-- Criar a função 'use'
CREATE ROLE use;

-- Atribuir permissões necessárias à função 'use' (substitua isso conforme necessário)
GRANT CREATE, CONNECT ON DATABASE cangaço TO use;
ALTER DEFAULT PRIVILEGES FOR ROLE use GRANT ALL ON TABLES TO use;

-- Criar o usuário 'Richa' com senha '0000'
CREATE USER "Richa" WITH PASSWORD '0000';
GRANT ALL PRIVILEGES ON DATABASE cangaço TO "Richa";

-- Atribuir permissões adicionais conforme necessário
GRANT CONNECT ON DATABASE cangaço TO "Richa";
ALTER DEFAULT PRIVILEGES FOR ROLE "Richa" GRANT ALL ON TABLES TO "Richa";
