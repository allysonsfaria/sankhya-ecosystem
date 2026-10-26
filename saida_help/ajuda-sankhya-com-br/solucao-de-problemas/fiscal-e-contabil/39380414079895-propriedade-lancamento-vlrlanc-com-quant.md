---
id: "39380414079895"
titulo: "Propriedade \"Lancamento.VLRLANC\" com quantidade de dígitos decimais acima do limite: (4 > 2)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39380414079895-Propriedade-Lancamento-VLRLANC-com-quantidade-de-d%C3%ADgitos-decimais-acima-do-limite-4-2"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:33:37Z"
rotulos: ["Produtos", "Atualização", "Contabilização", "Financeiro", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Propriedade "Lancamento.VLRLANC" com quantidade de dígitos decimais acima do limite: (4 > 2)

**MENSAGEM**

Propriedade 'Lancamento.VLRLANC' com quantidade de dígitos decimais acima do limite: (4 > 2)

**SITUAÇÃO**

Ao executar a rotina na tela de **"Zeramento de Contas"** (Contabilização >> Rotinas >> Zeramento de Contas), o sistema apresenta um erro relacionado à quantidade de dígitos decimais acima do limite permitido. Este erro impede a conclusão do zeramento das contas de resultado, processo necessário para o fechamento contábil do período.

**SOLUÇÃO**

Para resolver este problema, realize a atualização do **"Módulo Contabilidade"** conforme orientações abaixo:

**(1)** Verifique a versão atual do **"Módulo Contabilidade"** instalada no sistema.

**(2)** Realize a atualização para a versão **"Módulo Contabilidade 5.14.0"** ou superior.

**(3)** Execute a atualização primeiramente em ambiente de teste para validação do comportamento.

**(4)** Após validar que o processo de **"Zeramento de Contas"** foi executado com sucesso no ambiente de teste, aplique a atualização no ambiente de produção.

**(5)** Execute novamente o processo de **"Zeramento de Contas"** no ambiente de produção.

**Observação:** Caso o comportamento persista após a atualização, entre em contato com o suporte técnico informando a versão instalada e os detalhes do erro.

**CAUSA**

O erro ocorre devido a uma inconsistência no tratamento de valores decimais durante o processo de zeramento de contas em versões anteriores do **"Módulo Contabilidade"**. A rotina estava tentando gravar valores com quantidade de casas decimais superior ao limite permitido pelo campo **"VLRLANC"** da tabela de lançamentos contábeis, causando erros no processo.

Esta inconsistência foi corrigida a partir da versão **"5.14.0 do Módulo Contabilidade"**, que ajusta adequadamente o arredondamento e formatação dos valores durante o processo de zeramento.
