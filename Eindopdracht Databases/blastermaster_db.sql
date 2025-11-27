drop database if exists blastermaster;
create database blastermaster;
use blastermaster;

create table player (
  player_id int auto_increment primary key,
  player_naam varchar(30),
  player_email varchar(50)
);

create table game (
  game_id int auto_increment primary key,
  spelnaam varchar(50),
  genre varchar(50),
  prijs decimal(4,2)
);

create table highscore (
  id int auto_increment primary key,
  game_id int,
  player_id int,
  pogingen int,
  high_score int,
  highscore_datum date,
  foreign key (game_id) references game(game_id),
  foreign key (player_id) references player(player_id)
);

insert into player (player_naam, player_email) values
('alex','alex@blastmaster.nova'),
('thomas','thomas@blastmaster.nova'),
('dani','dani@blastmaster.nova'),
('manoa','manoa@blastmaster.nova'),
('amber','amber@blastmaster.nova'),
('safoune','safoune@blastmaster.nova'),
('thijmen','thijmen@blastmaster.nova'),
('nikhil','nikhil@blastmaster.nova'),
('romy','romy@blastmaster.nova'),
('ryan','ryan@blastmaster.nova'),
('dean','dean@blastmaster.nova'),
('quinten','quinten@blastmaster.nova'),
('robert','robert@blastmaster.nova'),
('daniel','daniel@blastmaster.nova'),
('shane','shane@blastmaster.nova'),
('roxanne','roxanne@blastmaster.nova'),
('sander','sander@blastmaster.nova'),
('wouter','wouter@blastmaster.nova'),
('gregory','gregory@blastmaster.nova'),
('jeroen','jeroen@blastmaster.nova');

insert into game (spelnaam, genre, prijs) values
('Pac-Man','Maze / Action',1.50),
('Space Invaders','Shoot em up',1.00),
('Donkey Kong','Platform',1.00),
('Street Fighter II','Fighting',1.00),
('Galaga','Shoot em up',1.00),
('Mortal Kombat','Fighting',1.00),
('Asteroids','Shoot em up',1.00),
('Ms. Pac-Man','Maze / Action',1.50),
('Frogger','Action / Puzzle',1.50),
('Tetris','Puzzle',1.00),
('Defender','Shoot em up',1.00),
('Dig Dug','Action / Puzzle',1.50),
('Bubble Bobble','Platform / Puzzle',1.50),
('NBA Jam','Sports',1.00),
('Metal Slug','Run and Gun',1.00),
('Time Crisis','Light Gun Shooter',1.00),
('Q*bert','Puzzle / Action',1.50),
('Rampage','Action',1.00),
('Track & Field','Sports',1.00),
('Contra','Run and Gun',1.00);
