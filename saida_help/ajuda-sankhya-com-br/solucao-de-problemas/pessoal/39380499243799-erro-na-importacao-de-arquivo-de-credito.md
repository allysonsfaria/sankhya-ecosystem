---
id: "39380499243799"
titulo: "Erro na importação de arquivo de crédito consignado do trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39380499243799-Erro-na-importa%C3%A7%C3%A3o-de-arquivo-de-cr%C3%A9dito-consignado-do-trabalhador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-28T18:41:46Z"
rotulos: ["Importação", "Folha", "eSocial", "Erro", "Artigo criado KCS", "Sankhya RH - KCS", "Cadastro Funcionários", "Crédito Consignado"]
---

# Erro na importação de arquivo de crédito consignado do trabalhador

**MENSAGEM**

Durante a importação do arquivo de crédito consignado do trabalhador, podem ocorrer diferentes mensagens de erro:

- **java.lang.StackOverflowError**
- É necessário o envio com sucesso do evento **"S-2206"** do cadastro ativo deste funcionário para realizar o lançamento
- Não há funcionário cadastrado com o CPF, matrícula e data admissão informados
- O **"Número do Contrato"** relacionado ao crédito do trabalhador não está informado, impedindo o cálculo

**SITUAÇÃO**

Os erros ocorrem ao tentar importar o arquivo de crédito consignado do trabalhador na tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento), na aba **"Funcionários"**. O problema pode afetar um ou mais funcionários, mesmo aqueles que tiveram importações bem-sucedidas em meses anteriores.

**SOLUÇÃO**

A solução varia conforme o tipo de erro apresentado:

**Para erro java.lang.StackOverflowError ou problemas com datas de transferência:**

**(1)** Acesse o cadastro do funcionário e verifique as **"Datas de Transferência"** entre empresas.
**(2)** Identifique se há duplicidade de datas, onde a data de transferência de origem e destino estão iguais.
**(3)** Mantenha a data de transferência do funcionário na empresa de destino.
**(4)** Na empresa de origem, ajuste a data para um dia anterior à admissão na nova empresa.
**(5)** Realize novamente a importação do arquivo.

**Para erro relacionado ao evento S-2206:**

**(1)** Verifique se existe envio do evento **"S-2206"** no sistema para o funcionário em questão. Em caso de transferência essa informação já é preenchida no momento dessa transferência. 
**(2)** Caso não exista, realize o envio dos eventos **"S-2205"** e/ou **"S-2206"**.
**(3)** Importe novamente a planilha de crédito consignado.

**Para erro de divergência de dados cadastrais (CPF, matrícula ou data de admissão):**

**(1)** Abra a planilha de importação e verifique os dados do funcionário que apresentou erro.
**(2)** Compare o **"CPF"**, **"Matrícula"** e **"Data de Admissão"** da planilha com os dados cadastrados no sistema.
**(3)** Acesse o portal do eSocial para confirmar qual informação está correta.
**(4)** Corrija manualmente na planilha os dados divergentes, especialmente a **"Data de Admissão"**.
**(5)** Realize novamente a importação.
**(6)** Se a divergência estiver no sistema Emprega Brasil, abra um chamado com eles para correção das informações.

**Para erro relacionado ao número do contrato:**

**(1)** Acesse a tela **"Lançamento de Movimento"** (PPessoal+ » Rotinas Folha » Lançamento de Movimento).
**(2)** Localize os funcionários com crédito consignado e verifique se o **"Número do Contrato"** está preenchido corretamente.
**(3)** Realize o reprocessamento na tela conforme orientações da Central de Ajuda.
 ![Imagem 1: (1) Acesse a tela "Lançamento de Movimento" (PPessoal+ » Rotinas Folha » Lançamento de Movimento). (2) Localize os…](https://ajuda.sankhya.com.br/hc/article_attachments/40921258941079)

**Para erro relacionado à planilha incorreta:**

**(1)** Verifique se a planilha utilizada é a correta e está atualizada.
**(2)** Baixe novamente o arquivo do portal Emprega Brasil ou eConsignado.
**(3)** Realize a importação com o arquivo correto.

**CAUSA**

Os erros na importação do arquivo de crédito consignado podem ocorrer por diferentes motivos:

- **Datas de transferência duplicadas ou incorretas** no cadastro do funcionário, causando conflito no processamento.
- **Ausência de eventos S-2206 finalizados** no sistema, especialmente para funcionários transferidos entre empresas.
- **Divergência de dados cadastrais** entre a planilha de importação e o cadastro do sistema (CPF, matrícula ou data de admissão).
- **Número do contrato não informado** no lançamento de movimento do funcionário.
- **Utilização de planilha incorreta ou desatualizada** para importação.
