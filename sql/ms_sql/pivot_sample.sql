-- Show sample data from Sales.SalesOrderHeader table
-- SELECT * FROM Sales.SalesOrderHeader

-- Pivot OrderDate on TerritoryID and SUM SubTotal 
SELECT 
    * 
FROM (
    SELECT 
        OrderDate, 
        [TerritoryID], 
        SubTotal 
    FROM Sales.SalesOrderHeader
) t1
PIVOT (
    SUM(SubTotal) FOR TerritoryID IN ([1], [2], [3], [4], [5], [6], [7], [8], [9], [10])
) p1