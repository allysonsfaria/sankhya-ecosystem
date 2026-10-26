---
id: "360045107913"
titulo: "Notas Canceladas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913-Notas-Canceladas"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > Comum a todos os documentos"
atualizado_em: "2026-09-15T15:02:08Z"
rotulos: ["CT-e", "manual", "GERAXMLAPROVCAN", "Fiscal", "NF-e", "XML", "SEFAZ", "Chave NF-e", "Dt. Protocolo Cancelamento", "Emissão NFe", "Notas Canceladas", "Notas Fiscais Eletrônicas", "Nro. Protocolo Cancelamento", "Período de Cancelamento", "br.com.sankhya.com.cons.notascanceladas", "Notas Canceladas manual", "Cancelamento", "NFS-e", "NF-e CT-e"]
---

# Notas Canceladas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311960750231) Módulo: Comercial > Consulta
```

---

A tela Notas Canceladas é onde você visualizará as notas que por algum motivo foram canceladas. A partir do momento que é cancelada uma nota fiscal, não é mais possível reverter este processo, sendo necessário lançar a nota fiscal novamente.

![Imagem 2: A tela Notas Canceladas é onde você visualizará as notas que por algum motivo foram canceladas. A partir do momento que…](https://ajuda.sankhya.com.br/hc/article_attachments/5255627237271)

Os campos **"Chave NF-e"**, **"Nro. Protocolo Cancelamento"**, **"Emissão NFe"** e **"Dt. Protocolo Cancelamento"** desta tela, facilitarão o rastreamento das **"Notas Fiscais Eletrônicas"** que passaram pelo processo de cancelamento.

Você definirá no campo **"Atualiza Livros Fiscais"**, em qual livro a nota será escriturada, não dependendo da configuração do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que a mesma encontra-se vinculada. Diante disto, as opções disponíveis neste campo serão as seguintes:

Ao configurar a NF-e com a opção **"Livro de entrada"** tem-se que ao gerar o ICMS/IPI, a nota será escriturada como **"Entrada"** na tela Cadastro Livro ICMS/IPI, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abageral), campo **"Entrada/Saída"**.

Ao selecionar a opção **"Livro de saída"**, gerando o ICMS/IPI da nota esta será alterada para a opção **"Saída"** no campo acima mencionado.

Caso a nota seja alterada para a opção **"Ambos"**, esta será gerada como Entrada ou Saída, a depender da movimentação.

Selecionando a opção **"Não atualiza"**, a nota não será gerada na tela Cadastro Livro ICMS/IPI.

As informações sobre as "**Notas Fiscais Eletrônicas de Serviço"** que passaram pelo processo de cancelamento, serão visualizadas através dos campos **"Protocolo de Cancelamento (NFS-e)"**, **"Data Cancelamento Prefeitura (NFS-e)"** e **"Tipo de Cancelamento NFS-e"**.

A marcação **"NFS-e Cancelada Extemporaneamente"** não é habilitada para edição, pois será ativada automaticamente quando uma NFS-e for cancelada nas telas [Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) ou [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

A tela possui além do botão para criação de filtros personalizados através do assistente de filtros, um filtro rápido. Utilizando o filtro rápido o usuário poderá filtrar as notas por **"Empresa"**, **"Parceiro"**, **"Tipo de Operação"**, **"Período de Cancelamento"** e **"Nro. Único"**.

Ao clicar no botão ![Imagem 3: Ao clicar no botão "Cadastrar Nota Cancelada" para inclusão de uma nova nota, os campos "Número da Nota" , "Número…](https://ajuda.sankhya.com.br/hc/article_attachments/16305237156375)**"Cadastrar Nota Cancelada"** para inclusão de uma nova nota, os campos **"Número da Nota"**, **"Número Único da Nota"**, **"Série"**, **"Modelo do Documento"**, **"Empresa"**, **"Cód. Parceiro"**, **"Dt. de Neg."**, **"Dt. de Canc."** e **"Motivo"** são habilitados para preenchimento, onde estes se tornam obrigatórios.

O botão ![Imagem 4: O botão "Excluir" permite a exclusão de notas canceladas, exceto nos casos em que:](https://ajuda.sankhya.com.br/hc/article_attachments/16305237158423)**"Excluir"** permite a exclusão de notas canceladas, exceto nos casos em que:

Se algum dos seguintes campos não estejam vazios: Chave NF-e, Emissão NF-e, Nro. Protocolo NF-e, Nro. Reg. EPEC, **"Nro. Protocolo Cancelamento"**, **"Nro. Protoc. Canc. Esp."** e **"Modelo do Documento = 57"**.

Mensagem de validação apresentada ao tentar excluir alguma CT-e:

**"CT-e cancelado não pode ser excluído".** 

Para NFS-e, caso alguns dos seguintes campos não estejam vazios: Código verificação NFS-e na tabela TGFNFSE (Arquivos da NFS-e) ligado à nota ou o campo NUMNFSE da TGFCAB\_EXC ligado a nota.

Mensagem de validação apresentada ao tentar excluir alguma NFS-e:

**"NFS-e cancelada não pode ser excluída".**

#### Geração de arquivo XML

Na parte superior da tela é apresentado o botão **"NF-e"**. Este botão é composto pelas seguintes opções:

- **Gerar arquivo XML da NF-e cancelada e enviar por e-mail para o destinatário:** ao acionar esta opção, a nota que estiver posicionada na seleção é enviada para o e-mail do destinatário da NF-e (assim como é feito nos Portais, contudo para notas canceladas).
- **Gerar arquivo XML da NF-e cancelada para Download:** por meio desta opção é aberta uma tela para realização do download do arquivo, onde será acrescentado ao nome do arquivo os dizeres **"can.XML"**. Nos casos em que for realizado o download de vários **"XML's"**, um arquivo zipado será gerado.
- **Enviar Evento de cancelamento:** esta opção deve ser acionada para enviar o evento de cancelamento da NFe para a SEFAZ.

**Importante:** caso o parâmetro **"Gerar XML de aprovação e cancelamento? - GERAXMLAPROVCAN"** esteja desativado, ao selecionar-se as notas e clicar nesta opção serão gerados apenas XML's de cancelamento; caso o referido parâmetro esteja acionado, serão gerados os XML's de cancelamento e aprovação.

O botão **"CT-e"** localizado também na parte superior da tela possui as seguintes opções:

- Imprimir Dacte Cte Cancelado;
- Gerar XML de cancelamento para CT-e;
- Enviar XML de CT-e cancelado por e-mail.

**Nota:** estas opções permitirão a exportação de XML de um CT-e Cancelado, tanto para download quanto para envio por e-mail e impressão do mesmo.

**Observação:** Quando for realizada a impressão do CT-e Cancelado, no documento irá constar a escrita **"CT-e Cancelado"** à fim de identificar que o documento encontra-se cancelado.

**Nota:** estas 3 opções também estarão disponíveis no botão CT-e do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) quando o **"Tipo de Movimento"** estiver configurado para **"Canceladas"**.

**Importante:** estas funcionalidades só estarão disponíveis para Empresas que possuem o Produto CONHECIMENTO DE TRANSPORTE ELETRÔNICO/W.
