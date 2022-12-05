-- #1:Sales from Employees
SELECT
  auth_user.username,
  Sum(transactions.grandtotal) AS 'Total Sales'
FROM
  auth_user
  INNER JOIN transactions ON auth_user.id = transactions.empid
GROUP BY
  auth_user.username


-- #2:Sales from Category
SELECT
  category.name,
  Sum(transactions.grandtotal) AS 'Total Sales'
FROM
  category
  INNER JOIN transactions ON transactions.category_id = category.id
GROUP BY
  category.name

-- #3:Sales by Dates
SELECT transactions.dateadded, 
SUM(transactions.grandtotal) AS 'Total Sale'
FROM transactions
GROUP BY transactions.dateadded
ORDER BY transactions.dateadded