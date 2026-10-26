---
id: "360044617693"
titulo: "O somatório dos campos 'Valor da obrigação a recolher' dos registros E116, não é igual à soma dos campos 'Valor total de ICMS a recolher' e 'Valores recolhidos ou a recolher, extrapuração' do registro E110"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617693-O-somat%C3%B3rio-dos-campos-Valor-da-obriga%C3%A7%C3%A3o-a-recolher-dos-registros-E116-n%C3%A3o-%C3%A9-igual-%C3%A0-soma-dos-campos-Valor-total-de-ICMS-a-recolher-e-Valores-recolhidos-ou-a-recolher-extrapura%C3%A7%C3%A3o-do-registro-E110"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:36Z"
rotulos: ["Configuração", "Relatórios", "SEFAZ", "ICMS", "Impostos", "EFD", "Divergência de valores: E116 E110", "Causa do problema: Falta de informação Apuração ICMS", "Procedimento de correção: Configuração Preenchimento Validação"]
---

# O somatório dos campos 'Valor da obrigação a recolher' dos registros E116, não é igual à soma dos campos 'Valor total de ICMS a recolher' e 'Valores recolhidos ou a recolher, extrapuração' do registro E110

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16589043733143) MENSAGEM:**

O somatório dos campos 'Valor da obrigação a recolher' dos registros E116, não é igual à soma dos campos 'Valor total de ICMS a recolher' e 'Valores recolhidos ou a recolher, extrapuração' do registro E110.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16589028642711) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela "Empresa" (Caminho de acesso: Comercial » Preferências):](https://ajuda.sankhya.com.br/hc/article_attachments/16589028648855) Acesse a tela **"Empresa"** (Caminho de acesso: Comercial » Preferências):

- Selecione a empresa, acesse a aba: **"EFD-Escrituração Fiscal Digital"**
- Selecione **"Tipo de Escrituração"** - EFD
- Painel: Blocos e Registros » Selecione o Bloco 'E'.
- No Painel: 'Registros' verifique se para o registro E116 está marcada a opção **"Gerar Registro'"**. Caso não esteja efetuar a marcação e seguir para o passo seguinte.

![Imagem 4: No Painel: 'Registros' verifique se para o registro E116 está marcada a opção "Gerar Registro'" . Caso não esteja…](https://ajuda.sankhya.com.br/hc/article_attachments/15328242588951)

![Imagem 5: Acesse: "Obrigações do ICMS e ICMS ST a Recolher" (Caminho de acesso: Livros Fiscais » Avançado » Escrituração Fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/16589043739159) Acesse: **"Obrigações do ICMS e ICMS ST a Recolher"** (Caminho de acesso: Livros Fiscais » Avançado » Escrituração Fiscal Digital ).

- Preencha os campos com os dados pertinentes ao recolhimento de ICMS e ICMS-ST e salve os registros, com o aval do contador da empresa.

![Imagem 6: Acesse: "Registro de Apuração do ICMS" (Caminho de acesso: Livros Fiscais » Relatórios).](https://ajuda.sankhya.com.br/hc/article_attachments/16589043751447) Acesse: **"Registro de Apuração do ICMS"** (Caminho de acesso: Livros Fiscais » Relatórios).

- Preencha os campos respectivo a empresa e período.
  Clique em **'Abrir'** para visualizar os lançamentos feito na rotina de **"Obrigações do ICMS e ICMS ST a Recolher"**,  confira os valores na Guia de **"Demonstrativos"** para ICMS e ICMS-ST'.
- Após a validação clique em **'Salvar'.**
- Lembrando que, cada alteração feita na tela de **"Obrigações do ICMS e ICMS ST a Recolher"**, sempre é necessário acessar a tela de **"Registro de Apuracão do ICMS"**, clicar em **abrir** e **salvar**, antes de gerar o arquivo EFD-Fiscal.

![Imagem 7: Acesse "EFD - Escrituração Fiscal Digital - ICMS/IPI" (Caminho de acesso: Livros Fiscais » Conexão) , gere novamente o…](https://ajuda.sankhya.com.br/hc/article_attachments/16589043756567) Acesse **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (Caminho de acesso: Livros Fiscais » Conexão), gere novamente o arquivo e valide no PVA.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16589028672535) CAUSA:**

Mensagem apresentada quando se possui obrigações a recolher referente a ICMS e ICMS-ST, porém não foi informada a obrigação a recolher e não salvou a Apuração do ICMS.
