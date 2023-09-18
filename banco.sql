create database banco;
use banco;

create table Cuentas(
ID varchar(50) primary key not null ,
NombreCliente varchar(100) not null,
Saldo decimal(10, 2)
);

create table Transacciones(
ID varchar(50) primary key not null,
IDCuenta varchar(50) not null,
Tipo varchar(15) not null,
Monto decimal(10,2) not null,
Fecha timestamp default current_timestamp,

foreign key (IDCuenta) references Cuentas(ID) on delete cascade
);

insert into Cuentas (ID, NombreCliente, Saldo) values ('BBVA001', 'Amelia Rivera Calva', 45977.30);
insert into Cuentas (ID, NombreCliente, Saldo) values ('BBVA002', 'Abril  Ocaña Almeda', 2112.77);
insert into Cuentas (ID, NombreCliente, Saldo) values ('BBVA003', 'Claudia Carolina Molina Almeda', 4124.97);
insert into Cuentas (ID, NombreCliente, Saldo) values ('BBVA004', 'Greta Arteaga Guarneros', 37907.46);
insert into Cuentas (ID, NombreCliente, Saldo) values ('BBVA005', 'Enzo Olavarrieta Arellanes', 15210.98);

