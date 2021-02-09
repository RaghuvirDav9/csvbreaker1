
CREATE USER read_only WITH PASSWORD 'read_only';
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO read_only;
grant select on jobdemo to read_only ;

CREATE USER read_write WITH PASSWORD 'read_write';
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO read_write;

grant select,insert,update on jobdemo to read_write;


