CREATE TABLE results (
    ID integer identity(1,1),
    WWW nvarchar(250) NOT NULL,
    HEADER nvarhcar(500) NOT NULL, 
    OVERALL nvarchar(500) not null, 
    TIMESTAMP datetime2
)