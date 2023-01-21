USE museum_novecho_database;

SELECT *
FROM ART_OBJECTS;
SELECT *
FROM ARTIST;
SELECT *
FROM EXHIBITION;
SELECT *
FROM PAINTING;
SELECT *
FROM OTHER;
SELECT *
FROM SCULPTURE_STATUE;
SELECT *
FROM PERMANEMT_COLLECTION;
SELECT *
FROM COLLECTIONS;
SELECT *
FROM BORROWED;

/*1. As Seen when running the query's above every table has a piece of data (primary or foreign key) that is able to connect said table to every other relevant table.
The primany keys that are crucial to the database are ID_no from ART_OBJECTS, EName from EXHIBITIONS and AName from ARTIST. This results in almost every relevant
table having a key that will connect its own data to another table's data with that same key. 
	ART_OBJECTS has the primary key ID_no that is a foreign key to BORROWED, PERMENENT_COLLECTION, SCULPTURE_STATUE, OTHER and PAINTING.
    ARTIST has a primary key AName that acts as a foreign key in ART_OBJECTS.
    EXHIBITIONS has the primary key EName that acts as a foreign key to ART_OBJECTS.
    COLLECTIONS has a primary key CName that acts as a foreign key to BORROWED.
Finally on every foegien key there is a named constraint that acts as a trigger to ensure that when a tuple is either inserted or deleted the other tuples with the
same foreign keys are also updated or deleted.*/

#2.
SELECT o.Title, "null" as "AName"
FROM ART_OBJECTS as o, ARTIST as a
WHERE o.ArName is NULL
group by o.Id_no
Union
(Select o.Title, a.AName
FROM ART_OBJECTS as o, ARTIST as a
where o.ArName = a.AName);

#A retriveal query that prints out the names of ART_OBJECTS and their artists.

#3.
SELECT Title, Country_Culture_Origin, Year_made
FROM ART_OBJECTS 
ORDER BY  Year_made ASC;

#Prints out the titles, country or culture of origin and year made for each ART_OBJECT and orders them in asending order.

#4.
SELECT distinct p.ID_no, p.Status_is
FROM PERMANEMT_COLLECTION as p
WHERE p.ID_no IN (SELECT ID_no
				FROM SCULPTURE_STATUE as s
				WHERE s.ID_no = p.ID_no AND Material = 'Marble')
                or
                ID_No in
                (SELECT ID_no
                FROM PAINTING as pa
                WHERE pa.ID_no = p.ID_no AND Paint_type = 'Oil');
                
#Prints out the ID number and status of art that are either made of marble or have paint type oil.

#5
SELECT ID_no, Type_of_art, Style
FROM (OTHER NATURAL JOIN BORROWED)
WHERE CoName =  'Queens, Kings and Emperors';

#Print the ART_OBJECTS that belong to the specified collections.

#6.
UPDATE ART_OBJECTs
SET  ARName  = REPLACE(ARName, 'Pablo Picasso', 'Luigi')
WHERE ID_no = 1400;

SELECT *
FROM ART_OBJECTS;

SELECT *
FROM ARTIST;

#Updates the specified art pieces to have 'Contempory' style.

#7.
DELETE FROM BORROWED 
WHERE CoName = 'National Museums Recovery';

SELECT *
FROM BORROWED;

SELECT *
FROM ART_OBJECTS;

#7. Deletes the specified rows from BORROWED. 