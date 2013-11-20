drop table if exists nodes;
create table nodes (
  id integer primary key autoincrement,
  row integer,
  col integer,
  title text not null
);