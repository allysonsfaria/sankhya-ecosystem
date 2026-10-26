---
id: "44012128373143"
titulo: "Como configurar o cBenef no Magis5 ERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012128373143-Como-configurar-o-cBenef-no-Magis5-ERP"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:21:35Z"
rotulos: ["sync_hc", "magis5", "sync_hash_f1989b3931ae", "magis5_209999421012"]
---

# Como configurar o cBenef no Magis5 ERP

## Neste guia, você aprenderá como realizar a configuração da tag cBenef dentro do Magis5 ERP

---

O **cBenef (Código de Benefício Fiscal)** é um campo obrigatório na NF-e destinado à identificação de incentivos ou desonerações de ICMS incidentes sobre a operação. É de **inteira responsabilidade do emitente** a correta classificação e inserção desse código, devendo este seguir rigorosamente as orientações da legislação vigente em sua unidade federativa.

Feito login no Magis5 ERP, acesse **"Configurações"** e depois clique em **“NF-e - Regras de Tributos V2”**

![Imagem 1: Feito login no Magis5 ERP, acesse "Configurações" e depois clique em “NF-e - Regras de Tributos V2”](https://ajuda.sankhya.com.br/hc/article_attachments/44012176475415)

Na tela **“NF-e - Regras de Tributos V2”**, o sistema exibirá todas as regras de tributos cadastradas. Para editar a regra fiscal desejada, clique no ícone verde.

![Imagem 2: Na tela “NF-e - Regras de Tributos V2” , o sistema exibirá todas as regras de tributos cadastradas. Para editar a regra…](https://ajuda.sankhya.com.br/hc/article_attachments/44012171581463)

Serão exibidos os filtros fiscais cadastrados. Selecione aquele no qual deseja realizar a configuração da tag **cBenef**.

![Imagem 3: Serão exibidos os filtros fiscais cadastrados. Selecione aquele no qual deseja realizar a configuração da tag cBenef .](https://ajuda.sankhya.com.br/hc/article_attachments/44012191497239)

Avance até a seção de **ICMS** e selecione o Código de Situação Tributária (CST) correspondente à operação.

![Imagem 4: Avance até a seção de ICMS e selecione o Código de Situação Tributária (CST) correspondente à operação.](https://ajuda.sankhya.com.br/hc/article_attachments/44012146872983)

O campo **cBenef** será exibido automaticamente ao selecionar um dos seguintes **Códigos de Situação Tributária (CST)**

- **CST 20**
- **CST 30**
- **CST 40**
- **CST 41**
- **CST 50**
- **CST 51**
- **CST 70**
- **CST 90**

![Imagem 5: CST 90](https://ajuda.sankhya.com.br/hc/article_attachments/44012191698839)

Preencha o campo cBenef com o código correto. Em seguida, avance até a etapa de **revisão** do filtro e clique em **"Salvar filtro".**

⚠️ O campo permite o preenchimento de até **10 caractere**s. Caso seja informado um valor com menos de **8 caracteres**, o sistema exibirá automaticamente um aviso.

![Imagem 6: ⚠️ O campo permite o preenchimento de até 10 caractere s. Caso seja informado um valor com menos de 8 caracteres , o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012147077911)

💡O **cBenef** não é obrigatório para salvar a regra. Os avisos exibidos na revisão da NF-e aparecem como alertas informativos e não bloqueiam o fluxo de emissão.

Por fim, clique em **“Salvar regra”** para concluir a configuração.

![Imagem 7: Por fim, clique em “Salvar regra” para concluir a configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/44012172100887)

**⚠️ Limpeza Automática ao Trocar o CST**

Ao selecionar um **CST** que não pertence ao grupo de **CSTs** habilitados para o **cBenef**, o valor preenchido é zerado automaticamente. Isso evita que um código anterior seja enviado indevidamente na NF-e.
