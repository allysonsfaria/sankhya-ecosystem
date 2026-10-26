---
id: "8370651290007"
titulo: "Consumo Indevido (Ultrapassou o limite de 20 consultas por hora) "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8370651290007-Consumo-Indevido-Ultrapassou-o-limite-de-20-consultas-por-hora"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:12:08Z"
rotulos: ["MDF-e", "Configuração", "Consulta", "XML", "SEFAZ", "não apagar", "656", "Consumo Indevido de Consultas: Solução e Orientações", "Erro"]
---

# Consumo Indevido (Ultrapassou o limite de 20 consultas por hora) 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16595115553943) MENSAGEM**:

656 -Motivo: Rejeição: Consumo Indevido (Ultrapassou o limite de 20 consultas por hora)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16595115555991)SOLUÇÃO:**

Primeiramente, valide se a consulta está sendo realizada dentro do período indicado. Para isso, acesse a tela **"Configuração MD-e/DF-e"** (Caminho de acesso à tela: Comercial » Rotinas » Configuração MD-e/DF-e)

![Imagem 3: Primeiramente, valide se a consulta está sendo realizada dentro do período indicado. Para isso, acesse a tela "…](https://ajuda.sankhya.com.br/hc/article_attachments/16595153455255)

**Observação:** deixar no mínimo 60 e de preferência 120 minutos.

Na tela **Empresa** (Caminho de acesso à tela: Comercial » Preferências » Empresa)
**(1)** O campo abaixo deve ser mantido **apenas** para empresas que de fato **usam** o recurso, ou seja, apenas as empresas que tem movimentações e que precisam que seus arquivos sejam importados.

![Imagem 4: Na tela Empresa (Caminho de acesso à tela: Comercial » Preferências » Empresa) (1) O campo abaixo deve ser mantido…](https://ajuda.sankhya.com.br/hc/article_attachments/16595115566231)

É importante ressaltar que a SEFAZ está monitorando essas consultas por todos os meios, sendo assim, seguem orientações:

**(1)** Desative a opção de busca nas bases Treina e Teste; (Desativamos na Base Teste essa busca);
**(1)** Evite fazer a busca do XML direto na SEFAZ;
**(1)** Evite fazer a busca Manual na rotina Configuração MD-e/DF-e nas opções **"Consultar Documentos"** e **"Consulta Direta"**;
**(1)** Evite utilizar outros aplicativos de busca.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16595153465239)CAUSA:**

Os servidores da receita estão validando de forma mais precisa o consumo indevido. Antes, quando ocorria um "bloqueio", após uma hora esse "bloqueio" era desfeito. Agora, os servidores da receita mantém o "bloqueio" uma hora após a última tentativa, fazendo com que o bloqueio seja renovado a cada tentativa frustrada.
<https://www.nfe.fazenda.gov.br/portal/informe.aspx?ehCTG=false&Informe=0cu/yBLKrCs=>
