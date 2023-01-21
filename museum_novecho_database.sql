DROP DATABASE IF EXISTS museum_novecho_database;
CREATE DATABASE museum_novecho_database; 
USE museum_novecho_database;

DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION (
	EName					varchar(100) not null,
	End_Date				varchar(100),
    Start_Date				varchar(100),
	primary key (EName)
);

INSERT INTO EXHIBITION (Ename, End_Date, Start_Date)
VALUES
('Cubism and The Trompe IOleil Tradidtion', 'Jan 22, 2023', 'Oct 20, 2022'),
('The Tudors: Art and Majesty in Renissance England', 'Jan 8, 2023', 'Oct 10, 2022'),
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina', 'Feb 5, 2023', 'Sept 9, 2022');

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	AName					varchar(40),
	BirthDate				varchar(20),
	DeathDate				varchar(20),
    Country					varchar(10),
    Epoch					varchar(20),
    Main_Style				varchar(100),	
    ADescript				varchar(100),
	primary key (Aname)
);

INSERT INTO ARTIST(AName, BirthDate, DeathDate, Country, Epoch, Main_Style, ADescript)
VALUES
('Pablo Picasso', 'April 8, 1973', 'Oct 25 1881', 'Spain', 'Modern', 'Abstract', 'One of the best known artists in the 20th century, known for being very experimental'),
('Niderviller', '1774', NULL, 'French', 'Modern', 'Ceramics', 'French manufactory that is known for tableware'),
('Eugene Berthelon', '1829', '1916', 'French', 'Modern', 'Chromolithograph', NULL),
('Georges Braque', '1882', '1963', 'French', 'Modern', NULL, NULL),
('Benedetto da Rovezzano', '1474', '1554', 'Italy', 'Renissance', 'Metalworking and Sculpting', NULL),
('Hans Holbein the Younger', '1497', '1543', 'German', 'Renissance', 'Drawings and Sketches', NULL),
('Delaroche, Paul', '1797', '1856', 'France', 'Contemporary', 'Oil Paintings', NULL),
('Lallemand, Jean-Baptiste', '1716', '1803', 'France', 'Contemporary', 'Oil Paintings', NULL);

DROP TABLE IF EXISTS ART_OBJECTS;
CREATE TABLE ART_OBJECTS (
	ID_no					int not null,	
	ExName					varchar(100),
	ArName					varchar(100),
    Country_Culture_Origin	varchar(100),
    Epoch					varchar(100), 
    Year_made				varchar(100),
    Title					varchar(100), 
    Descript				varchar(300),
	CONSTRAINT key_check primary key (ID_no),
    CONSTRAINT EXName_check foreign key (EXName) references EXHIBITION(EName) on DELETE CASCADE on UPDATE CASCADE,
    CONSTRAINT ArName_check foreign key (ArName) references ARTIST(AName) on DELETE CASCADE on UPDATE CASCADE
);

INSERT INTO ART_OBJECTS (ID_no, ExName, ArName, Country_Culture_Origin, Epoch, Year_made, Title, Descript)
VALUES
(1012, 'Cubism and The Trompe IOleil Tradidtion', 'Pablo Picasso', 'Spanish/France', 'Modern', '1914', 'The Absinthe Glass', 'Glass sculpture'),
(2004, 'Cubism and The Trompe IOleil Tradidtion', 'Pablo Picasso', 'Spanish/France', 'Modern', '1912', 'Violin and Grapes', 'Oil Painting'),
(3154, 'Cubism and The Trompe IOleil Tradidtion', 'Niderviller', 'France', 'Modern', '1735', 'Dessert plate', 'Ceramic'),
(4555, 'Cubism and The Trompe IOleil Tradidtion', 'Pablo Picasso', 'Spanish/France', 'Modern', '1914', 'Glass and Die', 'Sculpture'),
(2118, 'Cubism and The Trompe IOleil Tradidtion', 'Eugene Berthelon', 'France', 'Modern', '1902', 'Panneau Sapin', 'Print'),
(3667, 'Cubism and The Trompe IOleil Tradidtion', 'Georges Braque', 'France', 'Modern', '1914', 'Still Life (Glass and Cigarette Pack)', 'Painting'),
(1400, 'The Tudors: Art and Majesty in Renissance England', 'Benedetto da Rovezzano', 'Italy', 'Renissance', '1500', 'Candelabrum', 'Bronze Candle Stick'),
(3787, 'The Tudors: Art and Majesty in Renissance England', 'Benedetto da Rovezzano', 'Italy', 'Renissance', '1524-29', 'Angel Bearing Candlestick', 'Bronze Angel Statue'),
(9900, 'The Tudors: Art and Majesty in Renissance England', 'Hans Holbein the Younger', 'London', 'Renisssance', '1537-1543', 'Design for a Chimneypiece', 'Sketched drawing of a chimney'),
(6789, 'The Tudors: Art and Majesty in Renissance England', 'Hans Holbein the Younger', 'London', 'Renissance', '1540', 'Henry VII', 'Oil painting of Henry VII'),
(2333, 'The Tudors: Art and Majesty in Renissance England', NULL, 'England', 'Renissance', '1505', 'Unidenntified Saint', 'Terracotta statue of a Saint'),
(4678, 'The Tudors: Art and Majesty in Renissance England', 'Hans Holbein the Younger', 'England', 'Renissance', '1533', 'Robert Cheseman', 'Oil Painting'),
(1909, 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', NULL, 'America', 'Modern', '1850', 'Jug', 'Alkaline-glazed stoneware'),
(3355, 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', NULL, 'America', 'Modern', '1850-80', 'Face Jug', 'Alkaline-glazed stoneware'),
(4900, 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', NULL, 'America', 'Modern', '1867-85', 'Face Jug', 'Alkaline-glazed stoneware'),
(0700, NULL, NULL, 'Rome', 'Imperial Roman', '1885-1920', 'Statue', 'Portriat, long twisted beard with large beard'),
(0555, NULL, NULL, 'England', 'Contemporary', '1800-1835', 'Necklace of the sapphire set of Queen Marie-Amelie and Queen Hortense', 'Eight different sapphires on a silver necklace'),
(0100 , NULL, 'Delaroche, Paul', 'England/France', 'Nineteenth Century', '1828', 'Death of ELizabeth, Queen of England in 1603', 'Oil painting of the death of Queen Elizabeth'),
(9000, NULL, 'Lallemand, Jean-Baptiste', 'France', 'Eighteenth Century', '1700-1800', 'View of a port with fountain', 'Oil Painting of a harbour with gold frame'),
(6343, NULL, NULL, 'Rome', 'Imperial Roman', '1st quarter, third century', 'Sarcophagus Lid', 'Stone lid with engravings of people'),
(1212, NULL, NULL, 'England', 'Middle Age Gothic', '1200-1400', 'Stained Glass, Illustraiting the life of Saint Blaise', 'Stained Glass with people');

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	ID_no					int not null,
    Paint_type				varchar(100),
    Drawn_on				varchar(20),
    Style					varchar(100),
	CONSTRAINT ID_check5 foreign key (Id_no) references ART_OBJECTS(ID_no) on DELETE CASCADE on UPDATE CASCADE
);

INSERT INTO PAINTING(ID_no, Paint_type, Drawn_on, Style)
VALUES
(2004, 'Oil', 'Canvas', 'Abstract'),
(3667, 'watercolour', 'Paperboard', 'Modern'),
(6789, 'Oil', 'Panel', 'Classical Renissance'),
(4678, 'Oil', 'Panel', 'Classical Renissance'),
(0100, 'Oil', 'Canvas', 'Contemporary'),
(9000, 'Oil', 'Canvas', 'Contemporary');

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	ID_no					int not null,
    Type_of_art				varchar(20),
    Style					varchar(100),
	CONSTRAINT ID_check4 foreign key (Id_no) references ART_OBJECTS(ID_no) on DELETE CASCADE on UPDATE CASCADE
);

INSERT INTO OTHER(ID_no, Type_of_art, Style)
VALUES
(3154, 'Ceramic', 'Modern tableware'),
(2118, 'Print', 'Contempory'),
(1400, 'Bronze Work', 'Classical Renissance'),
(9900, 'Drawing', 'Classical Renissance'),
(1909, 'Pottery', 'Modern'),
(3355,  'Pottery', 'Modern'),
(4900,  'Pottery', 'Modern'),
(0555, 'Jewlery', 'Contempory'),
(1212, 'Stained Glass', 'Middle Age Gothic');

DROP TABLE IF EXISTS SCULPTURE_STATUE;
CREATE TABLE SCULPTURE_STATUE (
	ID_no					int not null,	
	Material				varchar(20),
    Style					varchar(10), 
    Height					varchar(20), 
    Weight					varchar(20), 
	CONSTRAINT ID_check3 foreign key (Id_no) references ART_OBJECTS(ID_no) on DELETE CASCADE on UPDATE CASCADE
);

INSERT INTO SCULPTURE_STATUE(ID_no, Material, Style, Height, Weight)
VALUES
(1012, 'Glass', 'Abstract', '8 7/8 inches', NULL),
(4555, 'Painted Wood', 'Abstract', '9 1/4 inches', NULL),
(3787, 'Bronze', 'Religous', '39 3/4 inches', '310.8 lb'),
(2333, 'Terracotta', 'Religous', '20 1/2', NULL),
(0700, 'Marble', 'Contempory', '16 inches', NULL),
(6343, 'Marble', 'Contempory', '31 inches', NULL);

DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANEMT_COLLECTION (
	ID_no					int not null,
    Date_aquired			varchar(20),
    Cost					varchar(10), 
    Status_is				varchar(10),
	CONSTRAINT ID_check2 foreign key (Id_no) references ART_OBJECTS(ID_no) on DELETE CASCADE on UPDATE CASCADE
);

INSERT INTO PERMANEMT_COLLECTION (ID_no, Date_aquired, Cost, Status_is)
VALUES
(1012, 'Aug 18, 2019', '$1000', 'Loan'),
(2004, 'Dec 2, 1960', '$3000', 'Loan'),
(3154, 'April 3, 2000' , '$5500', 'Loan'),
(4555, 'Oct 12, 1960', '$1200', 'Loan'),
(2118, 'Jan 10, 1999', '$1000', 'Loan'),
(3667, 'Feb 1800', '$1000', 'Loan'),
(1400, 'Sept 24, 2023', '$3000', 'Loan'),
(3787, 'Sept 24, 2023', '$5000', 'Loan'),
(9900, 'Oct 10, 2022', '$1000', 'Loan'),
(6789, 'Feb 26, 2023', '$3000', 'Loan'),
(2333, 'June 24, 2023', '$5500', 'Loan'),
(4678, 'Oct 10, 2022', '$3500', 'Loan'),
(1909, 'Aug 18, 2019', '$6000', 'Loan'),
(3355, 'Sept 24, 2023', '$7000', 'Displayed'),
(4900, 'April 3, 2000' , '$6500', 'Displayed');

DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
	CName					varchar(100) not null,
    Type_of_art				varchar(100),
    Descript				varchar(100),
	Address					varchar(20),
    Phone					varchar(20),
    Contact_person			varchar(20),
	primary key(Cname)
);

INSERT INTO COLLECTIONS(CName, Type_of_art,	Descript, Address, Phone, Contact_person)
VALUES
('Queens, Kings and Emperors', 'Renissance', 'Collection associated with the Louvre', '36, 75001 Paris', '+331 4020 5050', 'J. Smith'),
('National Museums Recovery', 'Modern', 'Collection associated with the Louvre', '36, 75001 Paris', '+331 4020 5050', 'J. Doe');

DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	ID_no					int not null,
    CoName					varchar(100) not null,
    Date_Borrowed			varchar(20),
    Date_Returned 			varchar(20),
	CONSTRAINT ID_check1 foreign key(Id_no) references ART_OBJECTS(ID_no) on DELETE CASCADE on UPDATE CASCADE,
    CONSTRAINT CoName_check foreign key(CoName) references COLLECTIONS(Cname) on DELETE CASCADE on UPDATE CASCADE,
    CONSTRAINT date_check check(Date_Borrowed < Date_Returned)
);

INSERT INTO BORROWED(ID_no, CoName, Date_Borrowed, Date_Returned)
Values
(0700, 'Queens, Kings and Emperors', '1895', 'Not Returned Yet'),
(0555, 'Queens, Kings and Emperors', '1890', 'Not Returned Yet'),
(0100, 'Queens, Kings and Emperors', 'June 29, 1828', 'Not Returned Yet'),
(9000, 'National Museums Recovery', '1951', 'Not Returned Yet'),
(6343, 'National Museums Recovery', '1951', 'Not Returned Yet'),
(1212, 'National Museums Recovery', 'June 16, 1951', 'Not Returned Yet');


