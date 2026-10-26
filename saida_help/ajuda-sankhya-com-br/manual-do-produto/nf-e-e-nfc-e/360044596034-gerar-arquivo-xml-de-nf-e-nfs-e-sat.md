---
id: "360044596034"
titulo: "Gerar Arquivo XML de NF-e/NFS-e/SAT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596034-Gerar-Arquivo-XML-de-NF-e-NFS-e-SAT"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NF-e e NFC-e"
atualizado_em: "2026-09-24T22:12:21Z"
rotulos: ["AJUDA DO SKW", "manual", "GERAXMLAPROVCAN", "Gerar Arquivo XML de NFe", "br.com.sankhya.com.rotinas.geracaoxmlnfe", "Gerar Arquivo XML de NFe manual", "NF-e", "XML", "SAT", "NFS-e", "Geração de Arquivo XML para NFe/NFS-e/SAT", "Notas Fiscais Eletrônicas Geração de XML Rotina Comercial", "Documentos Eletrônicos", "Comercial"]
---

# Gerar Arquivo XML de NF-e/NFS-e/SAT

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311755387671) Módulo: Comercial > Rotinas
```

---

As empresas que trabalham com Notas Fiscais Eletrônicas (emitentes e destinatários) e Notas Fiscais de Serviço Eletrônicas, deverão manter as Notas em arquivo digital pelo prazo estabelecido na legislação tributária para a guarda dos documentos fiscais, devendo estas serem apresentadas à administração tributária, quando solicitado.

Através desta tela, você fará a geração e download do arquivo XML de NF-e, NFS-e SAT/MFe já aprovadas para um diretório em sua máquina, possibilitando a visualização destes arquivos no visualizador do governo.

Além disso, você poderá gerar um arquivo XML de NF-e e NFS-e através dos Portais, utilizando o botão **"NF-e"** em sua opção **"Gerar Arquivo XML de NF-e e NFS-e"** e o botão **"NFS-e"** com a opção **"Gerar XML para NFS-e"**.

![NFSE1](https://ajuda.sankhya.com.br/hc/article_attachments/360060983094)

No campo **"Tipo Arquivo"** informe o tipo de arquivo para realizar o download. Desta forma, poderá selecionar uma das opções a seguir:

- NF-e;
- NFS-e;
- SAT/MFe.

**Observação:** ao selecionar o Tipo Arquivo NFS-e, os campos **"Chave NFe"** e **"Entrada/Saída"** serão excluídos da tela.

Em relação ao campo **"Empresa"**, selecione a empresa que se deseja realizar o download, podendo esta ser pesquisada diretamente por seu número de registro ou pela opção de **"Pesquisa"**.

**Nota:** todos os campos desta tela são filtros para que o usuário selecione a NF-e ou NFS-e desejada para realizar o download, sendo que, estes filtros deverão seguir as seguintes regras:

- Quando o Tipo Arquivo for **"NF-e"** e o campo **"Chave NFe"** for preenchido, os demais campos ficarão desabilitados, com exceção do campo Entrada/Saída.
- Preenchendo o campo **"Número da nota"** todos os campos ficarão indisponíveis, com exceção dos campos **"Série"** e Entrada/Saída.
- De outra forma, ao informar a data referente ao campo **"Período"**, os campos Chave NFe (quando o arquivo for referente a uma NF-e), Número da nota e Série não se encontrarão disponíveis.

**Importante:** o filtro trará apenas **"Notas Aprovadas"** ou **"Canceladas"**. Qualquer outro tipo de status de NF-e ou NFS-e não serão filtrados.

No campo Período, preencha a data inicial e a data final da emissão do lote.

Informe no campo Chave NFe a chave que irá compor o filtro. Desta forma, bastará que seja inserida esta informação para que o sistema selecione a nota a ser exportada, uma vez que, cada nota possui apenas um único número de chave.

Nos campos Número da Nota e Série serão inseridos o número e a série da nota desejada.

**Observação:** sendo informado apenas o número da Série sem informar o Número da Nota, será apresentada a seguinte mensagem:

**"Ao informar a série a nota deve ser informada".**

Por outro lado, inserindo-se apenas o Número da Nota, o sistema exibirá a mensagem a seguir:

**"Não foi encontrado NFe para esta nota: X e série: ''. / "Não existem notas NFS-e para gerar o arquivo".**

Ao considerar o campo **"Tipo de Período"**, você deverá indicar o tipo de período da nota a ser utilizado no filtro, sendo assim, tem-se disponibilizadas as seguintes opções:

- Negociação;
- Movimento;
- Faturamento;
- Entrada/Saída.

No campo **"Entradas/Saída"**, você pode selecionar as movimentações onde o arquivo XML será baixado. Nele, você poderá escolher uma dentre as seguintes opções:

- **Compras importadas:** Essa opção, refere-se às movimentações de entradas por XML;
- **Dev. Vendas importadas:** Ao utilizar esta opção, você executará a geração de XML das movimentações de devoluções de vendas emitidas por terceiros;
- **Emissão própria:** Por meio desta, as notas emitidas pela empresa serão geradas no XML;
- **Todas:** Através dessa opção, o XML será gerado conforme todas as opções anteriores.

Ao habilitar a marcação **"Canceladas"**, será gerado o XML apenas das NF-e's ou NFS-e's canceladas.

**Nota:** selecionando a marcação acima, o campo Entrada/Saída (quando o arquivo for referente a uma NF-e) será desabilitado.

**Observação:** para downloads de filtros que não retornam arquivos apresenta-se uma mensagem ao usuário que não foi localizado o XML de notas para o filtro informado.

Por fim, não sendo informado nenhum tipo de filtro nesta tela e acionando o botão **"Download"**, o sistema emitirá a seguinte mensagem:

**"Parâmetros para download não foram informados".**

Ao clicar no botão Download, o arquivo XML será exportado.

No campo **"TOP"**, há o ícone de ajuda, em que, ao clicar neste, será exibida a seguinte mensagem:

**"Deixar a TOP sem preencher, carrega apenas a NF-e/NFS-e aprovadas. Preencher a TOP faz com que sejam buscadas as NF-e/NFS-e aprovadas e também as NFC-e geradas com a TOP selecionadas"**

**Nota:** para realizar o download de NFC-e, o usuário deverá informar a TOP desta.

## Parâmetros que influenciam nesta rotina

O parâmetro **"Gerar XML de aprovação e cancelamento? - GERAXMLAPROVCAN"** está vinculado à marcação Canceladas, sendo que, quando este encontrar-se desligado, será realizado o download apenas do XML de cancelamento. Por outro lado, habilitando-se este parâmetro, será feito também o download do XML de aprovação.
