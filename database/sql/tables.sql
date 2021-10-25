CREATE TABLE IF NOT EXISTS Rol (
    Id_Rol          INTEGER       PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    Nombre_Rol      VARCHAR (25),
    Descripcion_Rol VARCHAR (100) 
);

CREATE TABLE NOT EXISTS Dependencia (
    ID_Dependencia     INTEGER      PRIMARY KEY AUTOINCREMENT
                                    NOT NULL,
    Nombre_Dependencia VARCHAR (50) 
);

CREATE TABLE NOT EXISTS Cargo (
    ID_Cargo       INTEGER      PRIMARY KEY AUTOINCREMENT
                                NOT NULL,
    Nombre_Cargo   VARCHAR (50),
    Salario        INT,
    ID_Dependencia INT          NOT NULL
                                CONSTRAINT Candado1 REFERENCES Dependencia (ID_Dependencia) 
);

CREATE TABLE NOT EXISTS Usuario (
    ID_Usuario    INTEGER       PRIMARY KEY AUTOINCREMENT
                                NOT NULL,
    Correo        VARCHAR (50)  NOT NULL,
    contrasenia   VARCHAR,
    Nombre        VARCHAR (100),
    Apellido      VARCHAR (100),
    Cedula        INT           NOT NULL,
    Genero        VARCHAR (10),
    Fecha_ingreso DATE,
    Direccion     VARCHAR (100),
    Tipo_contrato VARCHAR (50),
    Id_Rol        INTEGER       REFERENCES Rol (Id_Rol) 
                                NOT NULL,
    ID_Cargo      INTEGER       REFERENCES Cargo (ID_Cargo) 
                                NOT NULL
);

CREATE TABLE NOT EXISTS Retroalimentacion (
    ID_Retroalimentacion INTEGER       PRIMARY KEY AUTOINCREMENT
                                       NOT NULL,
    ID_Usuario           INTEGER       REFERENCES Usuario (ID_Usuario) 
                                       NOT NULL,
    Puntaje              INT,
    Descripcion          VARCHAR (300) 
);











