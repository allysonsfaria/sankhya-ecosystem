---
id: "28073845533847"
titulo: "Como autorizar parceiros a baixar o XML da NF-e/CT-e (Tag <autXML>)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28073845533847-Como-autorizar-parceiros-a-baixar-o-XML-da-NF-e-CT-e-Tag-autXML"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:38:33Z"
rotulos: ["CT-e", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "inserir mais de um CNPJ na tag <autXML>"]
---

# Como autorizar parceiros a baixar o XML da NF-e/CT-e (Tag <autXML>)

Na tela **"Empresa"**, aba **"Documentos fiscais eletrônicos"**, sub aba **"NF-e/NFC-e"**, sub aba **"Acesso ao XML da NF-e"**(para parceiros autorizados), é possível preencher, em campo específico, o CPF/CNPJ que deve ser considerado na TAG <autXML>.

![Imagem 1: Na tela "Empresa" , aba "Documentos fiscais eletrônicos" , sub aba "NF-e/NFC-e" , sub aba "Acesso ao XML da NF-e" (para…](https://ajuda.sankhya.com.br/hc/article_attachments/28112425871639)

Os registros feitos na aba Acesso ao XML da NF-e terão prioridade para preenchimento da tag <autXML> no XML da NF-e. Se houver pelo menos um linha nesta tabela para a empresa da nota.

**(1)** Se um parceiro **não tiver nenhuma marca cadastrada**, seu **CPF/CNPJ será enviado** na tag <autXML> **para qualquer NF-e da empresa cadastrada;**

**(1)** Por outro lado, se um **parceiro possuir Marcas cadastradas**, seu **CPF/CNPJ será enviado** na tag <autXML> **apenas se a NF-e possuir algum produto com as Marcas informadas** por parceiro para a empresa cadastrada.

**Observação:** **o manual da NF-e estabelece um limite de 10 ocorrências para o envio da tag <autXML>**. Dessa forma, é possível cadastrar até 10 parceiros nesta sub-aba. Se houver uma tentativa de cadastrar uma quantidade maior que essa, a seguinte mensagem será exibida:

“Não é possível cadastrar mais parceiros para acesso ao XML da NF-e. O limite estipulado pela SEFAZ é de 10 pessoas autorizadas.

**Lembrando que, não é possível gerar na tag <autXML> o mesmo CPF/CNPJ do parceiro da nota.**

**Importante: Existe ainda a opção de informar o CPF/CNPJ  na tela de Parceiro >> Aba Acesso ao XML da NF-e/CTe.**

Através desta aba, vincule um grupo de pessoas autorizadas para baixar o XML por Parceiro, para que, ao emitir NF-e's ou CT-e's, a tag **<autXML>** leve essa informação (pessoas autorizadas para fazer o download do XML).
