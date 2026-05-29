# glowing-spoon

## del 1

1.

    ``` bash
    ssh "username"@"host"
    ```

2.

    ``` bash
    ip a
    hostname -I
    ```

3.

    ``` bash

            systemctl status mariadb

    ```

4.
    en port er en ting som pcen din kan sende ut de har forskelige bruker for eksempel 22 er for ssh på den spesifiserte maskinen
5.

    ``` bash
    sudo ufw port/protocol
    ```

## del 2

1.

    ``` sql
     CREATE DATABASE "glowing_spoon";
     use glowing_spoon
    ```

2.

    ``` sql 
    CREATE TABLE users (id INT PRIMARY KEY AUTO_INCREMENT ,name VARCHAR(31), password VARCHAR(255));
    ```
3.

    ``` sql
    INSERT INTO users (name,password) VALUES ("sebrai","post_hash_password");
    ```
4.

    ``` sql
    SELECT id,name FROM users; 
    ```

5.

    ``` sql
    SELECT id,name FROM users WHERE id > 5; 
    ```

    henter det første 5 brukerne

    ``` sql
    SELECT id,name FROM users WHERE name = "sebrai"; 
    ```

    henter brukeren med navn "sebrai"

## del 3
