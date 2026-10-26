---
id: "36670710371479"
titulo: "Correção do Cálculo de 13º Salário em Admissões em Meses com 31 Dias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36670710371479-Corre%C3%A7%C3%A3o-do-C%C3%A1lculo-de-13%C2%BA-Sal%C3%A1rio-em-Admiss%C3%B5es-em-Meses-com-31-Dias"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-27T18:27:35Z"
rotulos: ["Configuração", "Admissão", "Folha de Pagamento", "Regra de Cálculo", "Correção do Cálculo de 13º Salário", "31 dias", "Admissões em Meses com 31 Dias", "1/12 avos do 13º salário", "RH", "Cálculo Salarial"]
---

# Correção do Cálculo de 13º Salário em Admissões em Meses com 31 Dias

Ao calcular o **13º salário** de um funcionário admitido em um mês com **31 dias**, o sistema, configurado para utilizar o **mês comercial de 30 dias**, gera divergência na apuração dos dias trabalhados.

Por exemplo, um funcionário admitido no dia **17** é contabilizado com **14 dias** em vez de **15**, como seria no mês real Essa divergência impede o cálculo correto do **1/12 avos do 13º salário**.

### Procedimento:

**(1)** Acesse a tela [**''Regra de Cálculo''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculo) (Pessoal+ » Cadastros » Regras de Cálculo).

**(1)** Na aba **''Propiedades''** marque o campo **''Calcula resíduo de admissões em meses que não possuem 30 dias''**.

![Imagem 1: (1) Na aba ''Propiedades'' marque o campo ''Calcula resíduo de admissões em meses que não possuem 30 dias'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36689044865687)

**(1)** Após esta configuração, o sistema passará a considerar corretamente meses com **31 dias**, permitindo o cálculo do **1/12 avos do 13º salário**.

**CAUSA:**

O comportamento incorreto ocorre porque a **regra de cálculo** está definida para considerar sempre o mês comercial (30 dias). 

Com a configuação, o sistema **não reconhece os dias adicionais em meses com 31 dias**, resultando em contagem incorreta dos dias trabalhados para fins de cálculo do 1/12 avos do 13º salário.
