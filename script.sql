/*Erstelle Datenbank */
CREATE DATABASE discordBot;

/* Gehe in die Datenbank */
use DiscordBot;

/* Erstelle Tabelle für die User*/
CREATE TABLE users (
    id INT NOT NULL auto_increment,
    userId varchar(20),
    points int,
    level int,
   PRIMARY KEY(id)
);