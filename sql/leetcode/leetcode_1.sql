-- Scripts are written on MS SQL Server 

-- https://leetcode.com/problems/reformat-department-table/description/
WITH cte1 AS (
    SELECT 'Jan' AS month UNION SELECT 'Feb' AS month
    UNION SELECT 'Mar' AS month UNION SELECT 'Apr' AS month
    UNION SELECT 'May' AS month UNION SELECT 'Jun' AS month
    UNION SELECT 'Jul' AS month UNION SELECT 'Aug' AS month
    UNION SELECT 'Sep' AS month UNION SELECT 'Oct' AS month
    UNION SELECT 'Nov' AS month UNION SELECT 'Dec' AS month
), 
cte2 AS (
    SELECT cte1.month,
    d1.id, d1.revenue
    FROM cte1 LEFT JOIN Department d1
    ON cte1.month = d1.month
)
SELECT 
    id, 
    [Jan] AS Jan_Revenue, [Feb] AS Feb_Revenue, 
    [Mar] AS Mar_Revenue, [Apr] AS Apr_Revenue, 
    [May] AS May_Revenue, [Jun] AS Jun_Revenue, 
    [Jul] AS Jul_Revenue, [Aug] AS Aug_Revenue, 
    [Sep] AS Sep_Revenue, [Oct] AS Oct_Revenue, 
    [Nov] AS Nov_Revenue, [Dec] AS Dec_Revenue
FROM (
    SELECT id, [month], revenue FROM cte2
) t1
PIVOT(
    SUM(revenue) FOR month IN (
        [Jan], [Feb], [Mar], [Apr], [May], [Jun], [Jul], [Aug], [Sep], [Oct], [Nov], [Dec])
) p1
WHERE id IS NOT NULL

--------------------------------------------------

