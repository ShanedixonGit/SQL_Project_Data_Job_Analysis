--Creating a DB

CREATE DATABASE sql_course;

--Creating a table--

CREATE TABLE job_applied (
    job_id INT,
    application_sent_date DATE,
    custom_resume BOOLEAN,
    resume_file_name VARCHAR(255),
    cover_letter_sent BOOLEAN,
    cover_letter_file_name VARCHAR(255),
    status VARCHAR(50)
);

--This returns no data as there has been no data inserted

SELECT * FROM job_applied;

--Inserting data into table

INSERT INTO job_applied
        (job_id,
         application_sent_date,
         custom_resume,
         resume_file_name,
         cover_letter_sent,
         cover_letter_file_name,
         status)
VALUES  (1,
         '2024-02-01',
         true,
         'resume_01.pdf',
         true,
         'cover_letter_01.pdf',
         'submitted'),
         (2,
         '2024-02-02',
         false,
         'resume_02.pdf',
         false,
         NULL,
         'interview scheduled'),
         (3,
         '2024-02-03',
         true,
         'resume_03.pdf',
         true,
         'cover_letter_03.pdf',
         'ghosted'),
         (4,
         '2024-02-04',
         true,
         'resume_04.pdf',
         false,
         NULL,
         'submitted'),
         (5,
         '2024-02-05',
         false,
         'resume_05.pdf',
         true,
         'cover_letter_05.pdf',
         'rejected');

-- Adding columns

ALTER TABLE job_applied
ADD contact VARCHAR(50);

-- Updating added columns

UPDATE job_applied
SET contact = 'Erlich Bachman'
WHERE job_id = 1;

UPDATE job_applied
SET contact = 'Dinesh Chugtai'
WHERE job_id = 2;

UPDATE job_applied
SET contact = 'Bertram Gilfoyle'
WHERE job_id = 3;

UPDATE job_applied
SET contact = 'Jian Yang'
WHERE job_id = 4;

UPDATE job_applied
SET contact = 'Big Head'
WHERE job_id = 5;

-- Changing column names

ALTER TABLE job_applied
RENAME COLUMN contact TO contact_name;

-- Changing data types

ALTER TABLE job_applied
ALTER COLUMN contact_name TYPE TEXT;

-- Dropping a column

ALTER TABLE job_applied
DROP COLUMN contact_name;

-- Dropping a table

DROP TABLE job_applied;


-- SELECT statement

SELECT * FROM job_applied;
