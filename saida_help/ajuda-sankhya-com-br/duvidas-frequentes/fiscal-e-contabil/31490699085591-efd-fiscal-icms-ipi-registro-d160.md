---
id: "31490699085591"
titulo: "EFD FISCAL (ICMS/IPI) | Registro D160"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31490699085591-EFD-FISCAL-ICMS-IPI-Registro-D160"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:32:56Z"
rotulos: ["CT-e", "Configuração", "Parceiro", "EFD", "ICMS/IPI", "EFD FISCAL (ICMS/IPI)", "Registro D160"]
---

# EFD FISCAL (ICMS/IPI) | Registro D160

Atualmente a aplicação está preparada para **gerar o registro D160.** Confira a seguir as regras de negócio do sistema para a execução desse processo:

![Imagem 1: Nas Preferências da Empresa (comercial), aba "Escrituração Fiscal Digital" , o Bloco D e o registro D160 devem estar…](https://ajuda.sankhya.com.br/hc/article_attachments/31960067184151) Nas Preferências da Empresa (comercial), aba **"Escrituração Fiscal Digital"**, o **Bloco D** e o **registro D160** devem estar **marcado** para geração;

![Imagem 2: O modelo de documento usado no D100 , deve ser um dos seguintes: 8, 902, 9, 10, 11, 26, 27 ;](https://ajuda.sankhya.com.br/hc/article_attachments/31960067185815) O modelo de documento usado no **D100**, deve ser um dos seguintes: **8, 902, 9, 10, 11, 26, 27**;

![Imagem 3: O tipo de CT-e do registro D100 , não pode ser "cancelado";](https://ajuda.sankhya.com.br/hc/article_attachments/31960098437271) O **tipo de CT-e** do registro **D100**, **não pode ser "cancelado";**

![Imagem 4: O disparo de geração do D160, parte do registro D100, havendo esta codependência .](https://ajuda.sankhya.com.br/hc/article_attachments/31960098438167) O disparo de geração do **D160, parte do registro D100, havendo esta codependência**.

Agora veja abaixo as regras de preenchimento de cada campo do registro:

(1)** DESPACHO:** hoje a aplicação gera esse campo vazio;

**(1)** **Os campos abaixo** **serão preenchidos pegando os dados do** **"Parceiro Remetente"** do CT-e, mas se por acaso **não houver essa informação**, o sistema vai **preencher com os dados do Parceiro, vinculado à empresa**, na tela [**"Cadastro De Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)

**(2)CNPJ\_CPF\_REM:** informação que estiver cadastrada na tela **"Parceiros"**, aba **"Identificação"**, campo **"CNPJ / CPF".**

**(2)IE\_REM:** o sistema gerará o campo vazio, ou se no cadastro do parceiro estiver marcado no campo **"Insc. Estadual / Identidade"** a informação **ISENTO**, o sistema levará tal palavra.

**(2)COD\_MUN\_ORI:** código do campo **"Mun. domicílio fiscal"** do cadastro de cidade do Parceiro.

**(1)** **Os campos abaixo serão preenchidos usando as informações do "Parceiro Destinatário"** do CT-e, mas se por acaso **não houver essa informação**, o sistema vai **preencher com os dados do Parceiro, lançados na tela "Cadastro Livro ICMS/IPI"** do CT-e.

**(2)CNPJ\_CPF\_DEST:** informação que estiver cadastrada na tela Parceiros, aba Identificação, campo CNPJ / CPF.

**(2)COD\_MUN\_DEST:** código do campo Mun. domicílio fiscal do cadastro de cidade do parceiro em questão.

**(2)IE\_DEST:** o sistema gerará o campo vazio, ou se no cadastro do parceiro estiver marcado no campo Insc. Estadual / Identidade a informação **ISENTO**, o sistema levará tal palavra.
