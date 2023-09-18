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

insert into Cuentas (NombreCliente, Saldo) values ('1', 'Amelia Rivera Calva', 45977.30);
insert into Cuentas (NombreCliente, Saldo) values ('2', 'Abril  Ocaña Almeda', 2112.77);
insert into Cuentas (NombreCliente, Saldo) values ('3', 'Claudia Carolina Molina Almeda', 4124.97);
insert into Cuentas (NombreCliente, Saldo) values ('4', 'Greta Arteaga Guarneros', 37907.46);
insert into Cuentas (NombreCliente, Saldo) values ('5', 'Enzo Olavarrieta Arellanes', 15210.98);

