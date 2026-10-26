---
id: "14782677960983"
titulo: "Ajuste/Benefício/Incentivo da Apuração do ICMS Substituição Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14782677960983-Ajuste-Benef%C3%ADcio-Incentivo-da-Apura%C3%A7%C3%A3o-do-ICMS-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:58:05Z"
rotulos: ["Configuração", "SEFAZ", "ICMS", "Impostos", "EFD", "Substituição Tributária", "E220", "Registro E220: ajustes ICMS ST", "Ativar E240 em preferências", "Revisar e preencher dados"]
---

# Ajuste/Benefício/Incentivo da Apuração do ICMS Substituição Tributária

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16969395370007) MENSAGEM:**

[Registro E220]: Ajuste/Benefício/Incentivo da Apuração do ICMS Substituição Tributária.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16969355750679) SOLUÇÃO:**

![Imagem 3: Acesse a tela " Ajuste da Apuração de ICMS e ICMS ST" (Caminho de acesso: Livros Fiscais » Arquivos » Ajuste da…](https://ajuda.sankhya.com.br/hc/article_attachments/16969355753623) Acesse a tela **"Ajuste da Apuração de ICMS e ICMS ST"** (Caminho de acesso: Livros Fiscais » Arquivos » Ajuste da Apuração de ICMS e ICMS ST).

![Imagem 4: O registro E220 é utilizado para informar os ajustes, benefícios ou incentivos fiscais relacionados à apuração do ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/16969355757335) O registro E220 é utilizado para informar os ajustes, benefícios ou incentivos fiscais relacionados à apuração do ICMS (Imposto sobre Circulação de Mercadorias e Serviços) na modalidade de substituição tributária. No entanto, alguns usuários têm enfrentado problemas ao preencher essas informações na tela de Ajuste da Apuração ICMS e ICMS ST, pois elas não estão sendo geradas corretamente no arquivo EFD - Escrituração Fiscal Digital.

**(1)** Acesse: Empresa Comercial » Preferências » Empresa

**(1)** Procure na aba **"EFD- Escrituração Fiscal Digital",**  opção de configurações relacionadas à geração do arquivo EFD;

**(1)** Tipo de escrituração:  EFD;

**(1)** Na aba **"Blocos e Registros"**, ative a opção de geração do registro E240;

**(1)** Salve as alterações realizadas nas preferências.

![Imagem 5: Após realizar esses passos, será possível gerar corretamente o registro E220 contendo as informações referentes aos…](https://ajuda.sankhya.com.br/hc/article_attachments/16969355759383) Após realizar esses passos, será possível gerar corretamente o registro E220 contendo as informações referentes aos ajustes, benefícios ou incentivos fiscais da apuração do ICMS na substituição tributária. Certifique-se de revisar e preencher corretamente os dados necessários na tela de Ajuste da Apuração ICMS e ICMS ST antes de gerar o arquivo EFD.

![Imagem 6: Nesta tela estão lançadas as informações de apuração, preenchendo os campos e os campos com (*) de preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/16969395377431) Nesta tela estão lançadas as informações de apuração, preenchendo os campos e os campos com (\*) de preenchimento obrigatório. Porém o **"Código UF"** deverá estar disponível para escolha somente se o tipo de imposto for ICMS ST e, caso não estiver preenchido o campo de UF, o registro E220 não será populado no arquivo de Sped fiscal.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16969355764119) CAUSA:**

Após uma análise detalhada, verificamos que todas as configurações relacionadas à substituição tributária foram revisadas e estão corretas. No entanto, ao examinarmos a query de geração do arquivo, percebemos que o resultado indica a necessidade de ativar a geração do registro E240 nas preferências da empresa comercial. Essa ativação é necessária para que o registro E220 possa ser gerado corretamente.
