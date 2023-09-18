create database banco;
use banco;

create table Cuentas(
IdCuentas INT primary key not null auto_increment,
NombreCliente varchar(100) not null,
Saldo decimal(10, 2)
);

create table Transacciones(
IDTrans INT primary key not null auto_increment,
IdCuentas int not null,
Tipo varchar(15) not null,
Monto decimal(10,2) not null,
Fecha int,

foreign key (IDCuentas) references Cuentas(IDCuentas) on delete cascade
);

insert into Cuentas (NombreCliente, Saldo) values ('Amelia Rivera Calva', 45977.30);
insert into Cuentas (NombreCliente, Saldo) values ('Abril  Ocaña Almeda', 2112.77);
insert into Cuentas (NombreCliente, Saldo) values ('Claudia Carolina Molina Almeda', 4124.97);
insert into Cuentas (NombreCliente, Saldo) values ('Greta Arteaga Guarneros', 37907.46);
insert into Cuentas (NombreCliente, Saldo) values ('Enzo Olavarrieta Arellanes', 15210.98);

