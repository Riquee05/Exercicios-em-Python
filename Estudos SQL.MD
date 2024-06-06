Nível Iniciante:

Exemplo de criação de tabela:



    CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
    );

Exemplo de inserção de dados:



    INSERT INTO Users (UserID, Name, Age)
    VALUES (1, 'John', 25),
       (2, 'Alice', 30),
       (3, 'Bob', 28);

Exemplo de consulta básica:



    SELECT * FROM Users;

Nível Intermediário:

Exemplo de junção (INNER JOIN):



    SELECT Orders.OrderID, Users.Name
    FROM Orders
    INNER JOIN Users ON Orders.UserID = Users.UserID;

Exemplo de função de agregação (COUNT):



    SELECT COUNT(*) AS TotalUsers FROM Users;

Exemplo de subconsulta:



    SELECT Name, Age
    FROM Users
    WHERE UserID IN (SELECT UserID FROM Orders);

Nível Avançado:

Exemplo de transação (COMMIT e ROLLBACK):



    BEGIN TRANSACTION;

    UPDATE Users SET Age = Age + 1 WHERE Name = 'John';

    -- ROLLBACK; -- Desfaz a transação
    COMMIT; -- Confirma a transação

Exemplo de criação de índice:



    CREATE INDEX idx_Name ON Users (Name);

Exemplo de stored procedure:



    CREATE PROCEDURE GetUsersByAge(IN minAge INT)
    BEGIN
    SELECT * FROM Users WHERE Age >= minAge;
    END;

Esses exemplos devem fornecer uma boa base para começar em cada nível de habilidade. Lembre-se de experimentar e adaptar esses exemplos para suas próprias necessidades de aprendizado.
ChatGPT pode cometer erros. Considere ve