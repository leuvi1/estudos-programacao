SELECT id_depto, COUNT(*) AS total_funcionarios
FROM funcionarios
WHERE SALARIO > 4000
GROUP BY id_depto
HAVING COUNT(*) >= 2;
