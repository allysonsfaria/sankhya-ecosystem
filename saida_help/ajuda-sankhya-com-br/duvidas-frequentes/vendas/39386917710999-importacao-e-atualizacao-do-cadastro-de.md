---
id: "39386917710999"
titulo: "Importação e Atualização do Cadastro de Parceiros utilizando dados da SEFAZ e ReceitaWS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39386917710999-Importa%C3%A7%C3%A3o-e-Atualiza%C3%A7%C3%A3o-do-Cadastro-de-Parceiros-utilizando-dados-da-SEFAZ-e-ReceitaWS"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T13:30:46Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Atualização", "SEFAZ", "Cadastro", "Artigo criado KCS", "Docs Eletrônicos - KCS", "ReceitaWS"]
---

# Importação e Atualização do Cadastro de Parceiros utilizando dados da SEFAZ e ReceitaWS

A atualização cadastral de parceiros no SankhyaOM ocorre de forma integrada aos serviços da SEFAZ e da ReceitaWS, permitindo consultar e sincronizar informações cadastrais, como CNPJ, Inscrição Estadual, endereço e situação cadastral. Essa funcionalidade auxilia na manutenção dos cadastros e reduz a ocorrência de inconsistências cadastrais que podem ocasionar rejeições durante a emissão de documentos fiscais.

### Como realizar a validação e atualização de parceiros

Por meio da opção **Importar dados cadastrais da SEFAZ**, é possível importar para o cadastro do parceiro as informações disponibilizadas pela SEFAZ.

Ao acionar essa funcionalidade, o sistema realiza uma consulta junto à SEFAZ e apresenta o pop-up **Importar Dados da SEFAZ**, contendo as informações retornadas, como endereço, bairro, cidade e demais dados cadastrais, além de destacar eventuais divergências em relação ao cadastro atual.

Acesse a tela **Parceiros(**Configurações » Cadastros » Parceiros)

Selecione o botão "Outras Opções" localizado no canto superior direito.

Escolha a opção **"Importar dados cadastrais da SEFAZ"**.

O sistema realizará a consulta e apresentará o resultado nas abas **"Importação"** e **"Divergências"**. Após validar as informações, confirme a importação para que o cadastro seja atualizado com os dados retornados pela SEFAZ.

**(5)** Após a importação, o botão Salvar ![Imagem 1: (5) Após a importação, o botão Salvar , localizado no canto superior esquerdo da tela, será habilitado. Clique nele…](https://ajuda.sankhya.com.br/hc/article_attachments/42109220426391), localizado no canto superior esquerdo da tela, será habilitado. Clique nele para gravar as alterações no cadastro do parceiro.

**Observação:** Além dos dados cadastrais, o sistema também atualizará automaticamente os campos **Situação Cadastral SEFAZ** e **Data/Hora da Última Consulta SEFAZ**, registrando o resultado e o momento da última consulta realizada.

**Importante:** A SEFAZ não garante que as informações de endereço do parceiro estejam sempre atualizadas.

**(1)**Para manter histórico das consultas realizadas habilite o parâmetro "ARMCONCADSFZ" (Armazenar consulta do cadastro SEFAZ?). Isso permitirá acessar a tela "Consulta Cadastro SEFAZ" com o histórico de todas as consultas realizadas

**(1)** Dica: Se você atualizar dados de um parceiro já existente e quiser manter o nome original, ative o parâmetro "MANNOMEPARCIMP" (Manter nome do parceiro na importação de dados).

## Atualizar Situação Cadastral via ReceitaWS

Também é possível consultar e atualizar a situação cadastral do parceiro utilizando a integração com a **ReceitaWS**.

Para realizar a consulta:

Acesse a tela **Parceiros(**Configurações » Cadastros » Parceiros)

Selecione o botão "Outras Opções" localizado no canto superior direito.

Escolha a opção **"Atualizar situação cadastral ReceitaWS".**

Após a consulta, os campos **Situação Cadastral ReceitaWS** e **Data/Hora da Última Consulta ReceitaWS**, localizados na aba **Fiscal**, serão preenchidos automaticamente com a situação cadastral retornada pela ReceitaWS e com a data e hora da última consulta realizada.

**Observação:** ao utilizar a opção , caso não seja identificada, por exemplo, a informação da cidade ou do endereço, a integração criará os registros necessários para concluir a atualização cadastral.

**Observação:** através do parâmetro **"Qtde de dias para realizar nova consulta na ReceitaWS. - QTDDIACONSRFD"** determine a quantidade de dias para realização de consultas junto a [Receita WS](https://receitaws.com.br/).

**Importante:** As informações retornadas dependem da disponibilidade e da atualização dos serviços consultados (SEFAZ e ReceitaWS) podendo ocorrer eventuais indisponibilidades ou divergências cadastrais.

## Informações/configurações adicionais:

Você pode configurar a validação automática na tela Tipos de Operação - TOP:

Acesse Tipos de Operação - TOP(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

Aba Geral >> seção "Validação de cadastro do parceiro":

- Valida situação cadastro na SEFAZ? - Caso a marcação **"Valida situação cadastro na SEFAZ?"** seja realizada, fará com que, ao ser utilizada a TOP em questão, o sistema valide a situação cadastral do parceiro junto a SEFAZ.
- Valida situação cadastro na ReceitaWS? - Ao realizar a marcação **"Valida situação cadastro na ReceitaWS?"**, fará com que, ao utilizar a TOP em questão, o sistema valide a situação cadastral do parceiro junto à Receita ([Receita WS](https://receitaws.com.br/)).

**Importante:** Os serviços consultados são de responsabilidade da SEFAZ e da ReceitaWS e existe a possibilidade de que as informações retornadas estejam desatualizadas.

**Importante:** Para parceiros do tipo **Pessoa Física**, essa funcionalidade não possui efeito. A validação será realizada apenas para parceiros do tipo **Pessoa Jurídica**, desde que a marcação esteja habilitada na TOP.

### Melhores práticas para manutenção de cadastros

Recomenda-se realizar a validação cadastral dos parceiros periodicamente, principalmente antes da emissão de documentos fiscais. O acompanhamento dos campos Data/Hora da Última Consulta SEFAZ e Data/Hora da Última Consulta ReceitaWS permite identificar quando foi realizada a última validação cadastral.

Essa funcionalidade auxilia na manutenção de cadastros atualizados, reduz inconsistências cadastrais e contribui para minimizar rejeições durante a emissão de NF-e e NFC-e.
