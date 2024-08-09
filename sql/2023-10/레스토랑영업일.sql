SELECT
  quartet,
  avg(x) 'x_mean',
  variance(x) 'x_var',
  round(avg(y), 2) 'y_mean',
  round(variance(y), 2) 'y_var'
FROM
  points
GROUP BY quartet;