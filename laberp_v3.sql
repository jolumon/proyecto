CREATE TABLE clientes (
	id_cli serial4 NOT NULL,
	nombre_cli varchar(100) NOT NULL,
	direccion_cli varchar(100) NULL,
	codigo_postal_cli varchar(5) NULL,
	poblacion_cli varchar(100) NULL,
	provincia_cli varchar(10) NULL,
	telefono_cli varchar(100) NULL,
	email_cli varchar(30) NULL,
	contacto_cli varchar(60) NULL,
	activo_cli bool DEFAULT true,
	CONSTRAINT pk_cli PRIMARY KEY (id_cli)
);

INSERT INTO clientes (nombre_cli,direccion_cli,codigo_postal_cli,poblacion_cli,provincia_cli,
telefono_cli,email_cli,contacto_cli,activo_cli) VALUES
	 ('Cosmetics ChemDev','C/ Manhatan 1','96456','New York','New York','123456789',
	 'info@chemdev.com','David Perales Gómez',true),
	 ('Laboratorios m2c','Ramón Muntaner','46950','Xirivella','Valencia','987456321',
	 'info@laboratoriosm2c.com','Juan Zafra Marín',true),
     ('Desarrollos qúimicos S.L.','C/ Iglesia 12','46950','Masamagrell','Valencia','1234567',
     'info@desaquim.com','Macarena del Carmen',true),
	 ('Laboratorios Deluxe Maris','C/China','45679','El pueblo 4','El pueblo','987456321',
	 'info@labdml.com ','Pepe Papi Papito',true);


CREATE TABLE proveedores (
	id_prov serial4 NOT NULL,
	nombre_prov varchar(50) NULL,
	direccion_prov varchar(60) NULL,
	cp_prov varchar(5) NULL,
	poblacion_prov varchar(50) NULL,
	provincia_prov varchar(30) NULL,
	telefono_prov varchar(9) NULL,
	contacto_prov varchar(50) NULL,
	movil_prov varchar(9) NULL,
	email_prov varchar(30) NULL,
	activo_prov bool DEFAULT true,
	CONSTRAINT pk_prov PRIMARY KEY (id_prov)
);

INSERT INTO proveedores (nombre_prov,direccion_prov,cp_prov,poblacion_prov,provincia_prov,
            telefono_prov,contacto_prov,movil_prov,email_prov,activo_prov) VALUES
	 ('Croda','','46950','','','','11','','',true),
	 ('Amita',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Basf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Biesterfield',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Biofilm',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Bonderalia',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Cestisa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Chemir',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Consum',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Eg Active',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true);
INSERT INTO proveedores (nombre_prov,direccion_prov,cp_prov,poblacion_prov,
            provincia_prov,telefono_prov,contacto_prov,movil_prov,email_prov,activo_prov) VALUES
	 ('Essential Compositions',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Fagron',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Gattefossé',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Gnt',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Guinama',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Imcd',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Inquiaroma',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Interfat',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Lipotec',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Lozano',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true);
INSERT INTO proveedores (nombre_prov,direccion_prov,cp_prov,poblacion_prov,provincia_prov,
telefono_prov,contacto_prov,movil_prov,email_prov,activo_prov) VALUES
	 ('Mediterranea',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Quimidroga',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Ravetllat',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Salvador Marí',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,true),
	 ('Dksh','','','Barcelona','Barcelona','123456789','Ramón',NULL,'',true),
	 ('Saffic Alcan','','','Barcelona','Barcelona','','',NULL,'',true),
	 ('Farma Química Sur','','','','','789456123','',NULL,'',true),
	 ('Adp','','','Madrid','','','',NULL,'',true),
	 ('Escuder','','','Barcelona','','','Juan','','',true),
	 ('Thor','','','','','','Juan','','',true);
INSERT INTO proveedores (nombre_prov,direccion_prov,cp_prov,poblacion_prov,provincia_prov,
telefono_prov,contacto_prov,movil_prov,email_prov,activo_prov) VALUES
	 ('Special Chemicals','','','','','','Pedro','','',true),
	 ('Atanor','','','','','','Lucas','','',true);

CREATE TABLE equipos (
	id_eq serial4 NOT NULL,
	fecha_adquisicion_eq date NOT NULL,
	nombre_eq varchar(10) NOT NULL,
	capacidad_eq int4 NOT NULL,
	revision_eq int4 NULL DEFAULT 12,
	activo_eq bool DEFAULT true,
	CONSTRAINT pk_equi PRIMARY KEY (id_eq)
);

INSERT INTO equipos (fecha_adquisicion_eq,nombre_eq,capacidad_eq,revision_eq,activo_eq) VALUES
	 ('2023-06-04','R-80',80,12,true),
	 ('2023-06-04','R-300',300,12,true),
	 ('2023-06-04','R-500',500,12,true),
	 ('2023-06-04','R-2000',2000,12,true),
	 ('2023-06-04','R-25',25,12,false);

CREATE TABLE materias_primas (
	id_mp serial4 NOT NULL,
	nombre_mp varchar(50) NULL,
	cantidad_mp int4 NULL DEFAULT 0,
	activo_mp bool DEFAULT true,
	CONSTRAINT pk PRIMARY KEY (id_mp)
);

INSERT INTO materias_primas (nombre_mp,cantidad_mp,activo_mp) VALUES
	 ('Xantan Gum 200 mesh',25,true),
	 ('Sodio Hidróxido',75,true),
	 ('Vitamina E',50,true),
	 ('popi',25,true),
	 ('Sytenol A',4,true),
	 ('Plantacare 2000',200,true),
	 ('Enhance US',18,true),
	 ('Ultrez 10',543,true),
	 ('Arlacel 165',70,true),
	 ('Lactic Acid',50,true);

CREATE TABLE matPrimas_proveedores (
	id_mp_mpProv int4 NOT NULL,
	id_prov_mpProv int4 NOT NULL,
	CONSTRAINT pk_mpProv PRIMARY KEY (id_mp_mpProv, id_prov_mpProv),
	CONSTRAINT fk1_mpProv FOREIGN KEY (id_mp_mpProv) REFERENCES materias_primas(id_mp),
	CONSTRAINT fk2_mpProv FOREIGN KEY (id_prov_mpProv) REFERENCES proveedores(id_prov)
);

insert into matprimas_proveedores (id_mp_mpProv,id_prov_mpProv) values 
	(1,12),
 	(1,30),
 	(2,14),
	(3,12),
	(4,14);

	
CREATE TABLE entradas (
	id_ent serial4 NOT NULL,
	id_mp_ent int4 NOT NULL,
	id_prov_ent int4 NOT NULL,
	lote_ent varchar(10) NOT NULL,
	fecha_ent_ent date NOT NULL,
	fecha_cad_ent date NULL,
	cantidad_ent int4 NULL,
	precio_ent money NULL,
	albaran_ent varchar(10) NULL,
	activo_ent bool DEFAULT true,
	CONSTRAINT ck_fechas_ent CHECK ((fecha_ent_ent < fecha_cad_ent)),
	CONSTRAINT pk_ent PRIMARY KEY (id_ent),
	CONSTRAINT fk1_ent FOREIGN KEY (id_mp_ent,id_prov_ent) REFERENCES matPrimas_proveedores(id_mp_mpProv,id_prov_mpProv)
	
);

INSERT INTO entradas (id_mp_ent,id_prov_ent,lote_ent,fecha_ent_ent,fecha_cad_ent,
                        cantidad_ent,precio_ent,albaran_ent) VALUES
	 
	 (1,30,'00001','2023-06-06','2025-06-06',200,900,'inicial'),
	 (1,30,'12er','2023-05-01','2023-06-02',0,0,'inicial'),
	 (1,30,'adf545','2023-08-17','2025-08-17',1200,600,'inicial'),
	 (1,30,'adsfdaf4','2023-08-17','2023-09-18',0,0,'inicial'),
	 (1,30,'abh23','2023-09-02','2025-09-02',200,100,'inicial'),
	 (1,30,'abh23456','2023-09-02','2025-09-02',100,100,'inicial'),
	 (2,14,'123456abcd','2023-09-03','2025-09-03',100,600,'inicial'),
	 (2,14,'321456fbds','2023-09-03','2025-09-06',100,60,'inicial'),
	 (2,14,'00002','2023-06-06','2025-06-06',100,1.200,'inicial'),
	 (3,12,'00002','2023-06-06','2025-06-06',50,1.400,'inicial');

CREATE TABLE ubicaciones(
    id_ubi serial4 not null,
    nombre_ubi varchar(20),/*Id_Ubi-Posicion-Altura*/
    CONSTRAINT pk_ubi PRIMARY KEY (id_ubi)
);

INSERT INTO ubicaciones(nombre_ubi) values
    ('Cuarentena-0-1'),
    ('Cuarentena-0-2'),
    ('UB001-0-0'),
    ('UB001-0-1'),
    ('UB001-0-2'),
    ('UB001-0-3'),
    ('UB001-1-0'),
    ('UB001-1-1'),
    ('UB001-1-2'),
    ('UB001-1-3'),
    ('UB002-0-0'),
    ('UB002-0-1'),
    ('UB002-0-2'),
    ('UB002-0-3'),
    ('UB002-1-0'),
    ('UB002-1-1'),
    ('UB002-1-2'),
    ('UB002-1-3');
    
CREATE TABLE lotes(
    
	id_lotes int not null,
	id_mp_lotes int not null,
    cantidad_lotes decimal(10,2) not null,
    CONSTRAINT pk_lotes PRIMARY KEY (id_lotes, id_mp_lotes),
	CONSTRAINT fk_lotes FOREIGN KEY (id_mp_lotes) REFERENCES materias_primas(id_mp)
	
);

INSERT INTO lotes (id_lotes, id_mp_lotes,cantidad_lotes) values (1,2,100),
    (2,2,100),
    (3,2,100);


CREATE TABLE lotes_ubicados(
    id_lotes_lubi int not null,
    id_mp_lotes_lubi int not null,
    id_ubi_lubi int not null,
    cantidad_lubi decimal(10,2) not null,
    
    CONSTRAINT pk_lubi PRIMARY KEY (id_lotes_lubi, id_mp_lotes_lubi,id_ubi_lubi),
	CONSTRAINT fk1_lubi FOREIGN KEY (id_lotes_lubi, id_mp_lotes_lubi) REFERENCES lotes(id_lotes, id_mp_lotes),
	CONSTRAINT fk2_lubi FOREIGN KEY (id_ubi_lubi) REFERENCES ubicaciones(id_ubi)
);

INSERT INTO lotes_ubicados (id_lotes_lubi, id_mp_lotes_lubi,id_ubi_lubi,cantidad_lubi) values (1,2,1,100),
    (2,2,2,100),
    (3,2,2,100);

CREATE TABLE productos (
	id_prod serial4 NOT NULL,
	nombre_prod varchar(50) NOT NULL,
	linea_prod varchar(50) NULL,
	cliente_prod int4 NOT NULL,
	activo_prod bool DEFAULT true,
	CONSTRAINT pk_pr PRIMARY KEY (id_prod),
	CONSTRAINT fk_prod_cl FOREIGN KEY (cliente_prod) REFERENCES clientes(id_cli)
);

INSERT INTO productos (nombre_prod,linea_prod,cliente_prod,activo_prod) VALUES
	
	 ('Crema facial dia spf30','Suprem',1,true),
	 ('Contorno ojos','Suprem',1,true),
	 ('Serum facial','Suprem',1,true),
	 ('Gel aloe puro','idrataloe',2,true),
	 ('Crema de manos','idrataloe',2,true),
	 ('Balsamo labial','idrataloe',2,true),
	 ('Serum multivitaminico','VitaLife',3,true),
	 ('Ampollas multivitaminas','VitaLife',3,true),
	 ('Crema multivitaminas','VitaLife',3,true),
	 ('Contorno ojos','VitaLife',3,true);

CREATE TABLE composiciones (
	id_prod_comp int4 NOT NULL,
	id_mp_comp int4 NOT NULL,
	porcentaje_mp_comp float4 NULL,
	CONSTRAINT pk_comp PRIMARY KEY (id_prod_comp, id_mp_comp),
	CONSTRAINT fk_comp1 FOREIGN KEY (id_prod_comp) REFERENCES productos(id_prod),
	CONSTRAINT fk_comp2 FOREIGN KEY (id_mp_comp) REFERENCES materias_primas(id_mp)
);


INSERT INTO composiciones (id_prod_comp,id_mp_comp,porcentaje_mp_comp) VALUES
	 
	 (1,1,99.0),
	 (1,2,0.5),
	 (1,3,0.5),
	 (2,1,50.0),
	 (2,2,49.5),
	 (2,3,0.5);

CREATE TABLE ordenes_fab (
    id_ofab serial4 NOT NULL,
	id_prod_ofab int NOT NULL,
	fecha_ofab date NOT NULL,
	lote_ofab varchar(10) NOT NULL,/*No haría falta, se podría identificar con la pk*/
	fecha_cad_ofab date NULL,
	equipo_ofab int4 NULL,
	cantidad_ofab int4 NULL,
	indicaciones_ofab varchar(1000) NULL,
	CONSTRAINT ch CHECK ((fecha_ofab < fecha_cad_ofab)),
	CONSTRAINT pk_ofab PRIMARY KEY (id_ofab, id_prod_ofab),
	CONSTRAINT fk_ofab1 FOREIGN KEY (id_prod_ofab) REFERENCES productos(id_prod),
	CONSTRAINT fk_ofab2 FOREIGN KEY (equipo_ofab) REFERENCES equipos(id_eq)
);

INSERT INTO ordenes_fab(id_prod_ofab, 	fecha_ofab , lote_ofab,	fecha_cad_ofab, equipo_ofab, cantidad_ofab, indicaciones_ofab)
VALUES
	 (1,'2023-06-06','20230001','2025-06-06',2,75,'Todo junto a la bartola'),
	 (1,'2023-06-08','20230002','2025-06-08',5,1600,'Una fase detras de otra. Subir a 75ºC, 
	 emulsionar.Enfriar y por debajo de 40ºC añadir fase termolabil'),
	 (1,'2023-06-04','20230003','2025-06-03',5,800,'Todo a la vez'),
	 (2,'2023-11-11','1465sdfd','2026-03-02',4,300,NULL),
	 (2,'2023-11-17','abc','2024-01-01',4,300,NULL);
	 
CREATE TABLE OF_L_C (
    id_ofab_OFLC int NOT NULL,
	id_prod_OFLC int NOT NULL,
	id_mp_OFLC int not null,
	id_lote_OFLC int NOT NULL,
	
	CONSTRAINT pk_OFLC PRIMARY KEY (id_ofab_OFLC, id_lote_OFLC),
	CONSTRAINT fk1_OFLC  FOREIGN KEY (id_prod_OFLC,id_mp_OFLC) REFERENCES composiciones(id_prod_comp,id_mp_comp),
	CONSTRAINT fk2_OFLC  FOREIGN KEY (id_lote_OFLC,id_mp_OFLC) REFERENCES lotes(id_lotes, id_mp_lotes)
);
