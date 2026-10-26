---
id: "33279809613207"
titulo: "Não foram encontradas transações (TGFTEF) para o NSU XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33279809613207-N%C3%A3o-foram-encontradas-transa%C3%A7%C3%B5es-TGFTEF-para-o-NSU-XXX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:29:10Z"
rotulos: ["TEF", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Monitoria TEF", "Não foram encontradas transações", "(TGFTEF) para o NSU XXX.", "TGFTEF", "versão 4.32", "DbExplorer", "NSU", "Erro", "Conciliação de Cartão"]
---

# Não foram encontradas transações (TGFTEF) para o NSU XXX

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33279809610903) **MENSAGEM:**

Não foram encontradas transações (TGFTEF) para o NSU XXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33279809611159) SOLUÇÃO:**

Para que os lançamentos sejam processados corretamente pela rotina de **Conciliação de Cartão**, é necessário que eles já existam previamente na tabela ''**TGFTEF''**. A partir da versão **4.32**, é possível verificar essa existência por meio da tela **"Monitoria TEF"**.

**(1)** Acesse a tela **"Monitoria TEF" (**Consulta > Monitoria TEF)**;**

**(2)** Verifique se o Número Único **(NSU)** que apresentou erro está listado na tela;

**(3)** Faça uma validação extra pelo DbExplorer, acessando a tela **"DbExplorer"** (Configurações» Avançado» DBExplorer);

**(4)** Execute a seguinte consulta, substituindo NSU pelo número que deseja validar:

SELECT \* FROM TGFTEF WHERE NSU LIKE '%NSU%'

Certifique-se de substituir NSU pelo valor real que apresentou erro durante o processamento.

**Observação:** caso após a realização dessas validações, o erro persista, sugerimos que entre em contato com a equipe de suporte técnico para uma análise mais aprofundada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33279797762071) CAUSA:**

O erro ocorre durante o processamento de um arquivo de conciliação de cartão quando o Número Único (NSU) informado não está registrado na tabela TGFTEF.
