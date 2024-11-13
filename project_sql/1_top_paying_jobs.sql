/*
Question: What are the top-paying Data Analyst jobs?
- Identify the top 10 highest-paying Data Analyst roles that are available in India.
- Focuses on job postings with specified salaries (remove nulls).
- Why? Highlight the top-paying opportunities for Data Analyst, offering insights into employer.
*/

SELECT 
    job_id,
    job_title,
    job_schedule_type,
    job_location,
    salary_year_avg,
    job_posted_date,
    name AS "company_name"
FROM job_postings_fact a
LEFT JOIN company_dim b ON a.company_id = b.company_id
WHERE job_location LIKE '%Anywhere%'
    AND salary_year_avg IS NOT NULL
    AND job_title_short LIKE '%Data Analyst%'
ORDER BY salary_year_avg DESC
LIMIT 10;