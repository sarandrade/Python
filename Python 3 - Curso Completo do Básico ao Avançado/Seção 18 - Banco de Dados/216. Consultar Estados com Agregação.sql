-- População Total por Região
select 
    regiao as 'Região',
    sum(populacao) as Total
from estados
group by regiao
order by Total desc

-- População Total
select 
    sum(populacao) as Total
from estados

-- Média de habitantes por Estado
select 
    avg(populacao) as Total 
from estados