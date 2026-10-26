---
id: "39354670765207"
titulo: "ORA-20101: O parâmetro EXIBRENTNOTACAC (Exibe rentabilidade na CAC) está ligado! Não encontramos custo para o produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354670765207-ORA-20101-O-par%C3%A2metro-EXIBRENTNOTACAC-Exibe-rentabilidade-na-CAC-est%C3%A1-ligado-N%C3%A3o-encontramos-custo-para-o-produto"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-10-02T18:22:19Z"
rotulos: ["Produtos", "Custos", "Configuração", "Preferências", "ORA-20101", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# ORA-20101: O parâmetro EXIBRENTNOTACAC (Exibe rentabilidade na CAC) está ligado! Não encontramos custo para o produto

**MENSAGEM**

ORA-20101: O parametro EXIBRENTNOTACAC (Exibe rentabilidade na CAC) esta ligado! ERRO: Não encontramos custo para o Produto [código], Empresa [código], Controle [controle] e Local [código] anterior ou igual a [data]. Não será possível mostrar análise de rentabilidade sem o custo.

**SITUAÇÃO**

Esta mensagem ocorre ao abrir uma tela, relatório ou dashboard que exibe a **"Análise de Rentabilidade"** de um documento que contém produtos sem custo registrado, como produtos novos, sem histórico de compras. A mensagem cita o parâmetro **"Exibe rentabilidade na CAC" (EXIBRENTNOTACAC)**, mas o que impede o cálculo é a falta do custo dos produtos.

**SOLUÇÃO**

Aplique uma das opções descritas abaixo para resolver este problema:

**Opção 1: Cadastrar custo para o produto**

**(1)** Acesse a tela **"Atualização de Custos"** (Comercial » Rotinas » Atualização de Custos).
**(2)** Localize o produto que está gerando o erro através do código informado na mensagem.
**(3)** Cadastre um custo para o produto na **empresa, local e controle** informados na mensagem, com **data igual ou anterior** à data informada. Para produtos novos sem entrada, cadastre um custo de reposição estimado.
**(4)** Retorne à tela ou ao relatório que exibiu a mensagem e tente acessá-lo novamente.

**Opção 2: Desabilitar temporariamente o parâmetro de rentabilidade**

**Atenção:** esta opção só funciona se a rotina que exibe a rentabilidade consultar esse parâmetro antes de buscar o custo. Se o erro continuar com o parâmetro desligado, use a Opção 1.

**(1)** Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).
**(2)** Pesquise pelo parâmetro **EXIBRENTNOTACAC**.
**(3)** **Desmarque** o parâmetro **EXIBRENTNOTACAC** temporariamente.
**(4)** Tente acessar a rentabilidade novamente.
**(5)** Após resolver o problema, reative o parâmetro se necessário.

**Observações Importantes:**

• Se você trabalha frequentemente com produtos novos sem histórico de custos, considere manter o parâmetro **EXIBRENTNOTACAC** desativado ou estabeleça um processo para sempre cadastrar um custo estimado antes de incluir produtos em notas e pedidos.
• O tipo de custo configurado na tela **"GOL"** (Configurações » Aba Margem de Contribuição), campo **"Custo a ser considerado"** (por exemplo, **"Médio Com ICMS"** ou **"Médio Sem ICMS"**), define qual valor entra no cálculo. Ele **não evita** este erro: a mensagem aparece quando não existe nenhum custo registrado, qualquer que seja o tipo.
• Para produtos transferidos entre empresas, certifique-se de que a **"TOP"** (Tipo de Operação) utilizada atualiza o custo na empresa de destino.

**CAUSA**

O erro ocorre quando a rotina que exibe a análise de rentabilidade busca o custo do produto e não o encontra. Para calcular a rentabilidade, o sistema precisa do **"Custo da Mercadoria Vendida (CMV)"**, que é obtido através do custo cadastrado do produto multiplicado pela quantidade.

O sistema considera o custo mais recente com **data igual ou anterior** à data informada na mensagem. Quando o custo é controlado por empresa (**CUSTOPOREMP**), por local (**CUSTOPORLOC**) ou por controle (**CUSTOPORCONT**), ele precisa ser da mesma empresa, local e controle. Se não existir custo nessas condições, inclusive quando ele foi cadastrado com data posterior, o sistema não consegue realizar o cálculo e gera o erro.

Essa busca é feita pela função de banco de dados **OBTEMCUSTO**, normalmente usada por rotinas personalizadas (relatórios, dashboards ou campos personalizados). A função não consulta o parâmetro **EXIBRENTNOTACAC**.
