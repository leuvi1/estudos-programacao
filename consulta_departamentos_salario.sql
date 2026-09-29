SELECT funcionarios.nome, funcionarios.cargo, funcionarios.salario, departamentos_ti.nome_depto
FROM funcionarios
INNER JOIN departamentos_ti
ON funcionarios.id_depto = departamentos_ti.id_depto
WHERE (departamentos_ti.nome_depto = 'Dados' OR departamentos_ti.nome_depto = 'Desenvolvimento') AND funcionarios.salario > 6000;
