---
id: "13308716779287"
titulo: "Configuração do Cupom Fiscal Eletrônico no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13308716779287-Configura%C3%A7%C3%A3o-do-Cupom-Fiscal-Eletr%C3%B4nico-no-PDV-Web"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NF-e e NFC-e"
atualizado_em: "2026-09-15T16:50:27Z"
rotulos: ["Configuração", "SEFAZ", "TOP", "PDV Web", "MFE", "Portal de Caixa", "Cupom fiscal eletrônico - CF-e", "SAT", "Prtal de Vendas", "Configuração do CF-e no PDV Web", "CF-e"]
---

# Configuração do Cupom Fiscal Eletrônico no PDV Web

O uso de aparelhos fiscais no território nacional é exclusivo para alguns estados e tem como objetivo a emissão do Cupom fiscal eletrônico - CF-e no modelo fiscal 59.

## SAT

| ![Imagem 1: SAT](https://ajuda.sankhya.com.br/hc/article_attachments/42311648399511) | O SAT Fiscal é o equipamento criado pelo estado de **São Paulo** para substituir o ECF (Emissor de Cupom Fiscal) no varejo. O hardware valida o Cupom Fiscal Eletrônico (CF-e) e o transmite à Secretaria da Fazenda automaticamente. |
| --- | --- |

## MFE

| ![Imagem 2: MFE](https://ajuda.sankhya.com.br/hc/article_attachments/42311648401687) | O MFE (Módulo Fiscal Eletrônico) é um equipamento para emissão do Cupom Fiscal Eletrônico que possui todas as regras necessárias para a validação ou rejeição do XML. Além disso, ele se comunica periodicamente com a SEFAZ para o envio e recebimento de informações . Ele foi desenvolvido para suprir a legislação fiscal que determina as novas regras de emissão de Cupom Fiscal Eletrônico (CF-e) no **Ceará**, em substituição ao Emissor de Cupom Fiscal (ECF). |
| --- | --- |

Aqui estão centralizadas todas as configurações necessárias para o uso desses aparelhos no Sankhya Om pelo PDV Web.

---

### Liberações

Primeiramente, solicite ao Service Desk que faça o vínculo do CNPJ do cliente com o CNPJ da Software House (Sankhya Om) para ativar o aparelho e obter a Assinatura SAT.

Depois, para utilizar o equipamento SAT deve ser liberado o opcional **"30784 - CUPOM FISCAL ELETRÔNICO (SAT)/W"**, já para o equipamento MFE deve ser concedido o opcional **"30365 - CUPOM FISCAL ELETRÔNICO (MFE)/W"**.

---

### Cadastro do Equipamento

Agora, acesse a tela **"Cadastro de Equipamentos Fiscais - ECF/SAT/MFE"** e cadastre o equipamento SAT ou MFE.

![Imagem 3: Conheça mais detalhes dessa tela no artigo Cadastro de Equipamentos Fiscais - ECF/SAT/MFE .](https://ajuda.sankhya.com.br/hc/article_attachments/16948631646871) Conheça mais detalhes dessa tela no artigo [Cadastro de Equipamentos Fiscais - ECF/SAT/MFE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110533).

---

### Cadastro do Tipo de Operação - TOP

Configure um [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) para emissão de vendas com o CF-e utilizando o modelo 59, conforme abaixo:

- **Modelo do documento**: Deve ser informado o 59 - Cupom Fiscal Eletrônico;
- **Modelo de impressão de nota fiscal** e **Modelo de impressão de cancelamento CF-e**: Devem ser cadastrados na rotina [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913) buscando um modelo previamente configurado em [Modelos de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034).

**Nota:** se preferir pode utilizar o modelo padrão do CF-e disponibilizado no botão ![Imagem 4: Nota: se preferir pode utilizar o modelo padrão do CF-e disponibilizado no botão "Baixar Modelos Padrões" da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16948807368983) **"Baixar Modelos Padrões"** da tela Modelo de Impressão (Nota/Pedido).

![Imagem 5: Nota: se preferir pode utilizar o modelo padrão do CF-e disponibilizado no botão "Baixar Modelos Padrões" da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/13311861143447)

**Observação:** lembrando que, ao cadastrar uma TOP com modelo 59 é obrigatório haver modelos de impressões configurados.

---

### Configuração do aparelho para o Usuário

No cadastro do Usuário, aba [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#AbaAcessosPDVWeb), vincule no campo **"Equipamento Fiscal"** o aparelho que foi cadastrado na rotina Cadastro de Equipamentos Fiscais para que o usuário possa fazer a emissão do CF-e em suas vendas.

![Imagem 6: No cadastro do Usuário , aba PDV Web , vincule no campo "Equipamento Fiscal" o aparelho que foi cadastrado na rotina…](https://ajuda.sankhya.com.br/hc/article_attachments/13312484757271)

---

**(1)** Após a realização de todas as configurações citadas acima, a emissão do CF-e poderá ser realizada.

### Emissão do CF-e

A partir de uma Venda dentro do [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047), ao receber e concluí-la, a emissão do documento CF-e deve ser realizada e disparada a impressão do modelo configurado.

A rotina para a emissão do CF-e se dá também pelo [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367), onde é possível localizar vendas não confirmadas e por ele gerar o CF-e confirmando uma ou várias notas. Caso queira realizar essa emissão em lotes, selecione as vendas com a devida TOP do modelo 59 configurado e acione a opção **"Gerar lote"** no botão CF-e.

**Observação:** durante a emissão e aprovação do CF-e, o campo **"Nr Nota"** será atualizado com o número gerado e controlado pelo aparelho (SAT/MFE). Nesta venda, também será registrado o **"Nr da série"** para fins de informação ao gerar o [SPED Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263) nos blocos C800 e C860.

Vale ressaltar que, é importante a visualização na grade das colunas **"Status CF-e"** e **"Retorno Equipamento Fiscal"**, pois auxiliam na conferência da venda emitida pelo CF-e.

![Imagem 7: Vale ressaltar que, é importante a visualização na grade das colunas "Status CF-e" e "Retorno Equipamento Fiscal" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/13312885780375)

A coluna Status CF-e irá trazer os seguintes status:

- **Aprovada:** Quando tiver a autorização e retornado a CF-e;
- **Com erro de Validação:** Quando estiver com alguma falha na tentativa de autorização ou com rejeição;

**Nota:** nestes casos deve acessar o Portal de Vendas para fazer um novo reenvio a partir da opção **"CF-e>Gerar lote"** do botão CF-e.

- **Enviada:** Quando estiver em processo de aprovação, nota confirmada e enviada, ainda não retornada com a autorização;
- **Não é CF-e:** Quando o documento de venda está com TOP que não é CF-e;
- **Não enviada:** Quando a venda foi confirmada e ainda não foi enviada.
