-- Find the Nth highest value in a column of a table
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY [column]) AS row_number FROM [table]) AS t 
WHERE t.row_number = N;

-- Find the median value in a column without using the median function
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY [column]) AS row_number 
    FROM [table]
) AS t 
WHERE t.row_number = (SELECT COUNT(*) FROM [table]) / 2;
