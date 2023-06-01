# Database

The database consists of four main entities: "writer", "circle", "letter", and "_circleTowriter".

## Table: writer
- Fields:
    - id (Int): Primary key of the "writer" table, autoincrement.
    - title (String): Optional field representing the title of the writer.
    - name (String): Required field representing the name of the writer.
    - pseudo (String): Required field representing the pseudonym of the writer.

## Table: circle
- Fields:
    - id (Int): Primary key of the "circle" table, autoincrement.
    - name (String): Required field representing the name of the circle.

## Table: letter
- Fields:
    - id (Int): Primary key of the "letter" table, autoincrement.
    - circleId (Int): Foreign key for the circle relation.
    - writerId (Int): Foreign key for the writer relation.
    - postAt (DateTime): Field representing the posting time of the letter.
    - updatedAt (DateTime): Field representing the last update time of the letter.
    - content (String): Field representing the content of the letter.
    - subject (String): Field representing the subject of the letter.
    - replyId (Int): Optional foreign key for the reply relation (letter id).
 
## Table: _circleTowriter
- Fields:
  - A (Int): Id of a circle
  - B (Int): Id of a writer