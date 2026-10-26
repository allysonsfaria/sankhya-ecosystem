---
id: "360044607914"
titulo: "Super Sintegra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Rotinas descontinuadas"
atualizado_em: "2026-09-15T17:30:04Z"
rotulos: ["AJUDA DO SKW", "manual", "ISS", "Configuração", "Livros Fiscais", "Super", "br.com.sankhya.mgeliv.mov.supersintegra", "Super Sintegra manual", "ICMS", "Sintegra", "Configurações para gerar arquivo", "Botões e histórico disponíveis", "Substitui escrituração manual", "Documentos Eletrônicos"]
---

# Super Sintegra

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313002852631) Módulo: Livros Fiscais > Conexão
```

---

A escrituração dos Livros Fiscais previstos no regulamento do ICMS e do ISS foi substituída no ano de 2006 pela escrituração eletrônica do **"Livro Fiscal Eletrônico (LFE)"**, ou seja, o **"Super Sintegra"**, conforme layout previsto no Ato Cotepe 35/2005. A escrituração no Super Sintegra foi determinada no [Decreto nº 26.529, de 13 de janeiro de 2006](http://www.fazenda.df.gov.br/aplicacoes/legislacao/legislacao/TelaSaidaDocumento.cfm?txtNumero=26529&txtAno=2006&txtTipo=6&txtParte=.), regulamentado pela Portaria nº 210, de 14 de Julho de 2006.

Todo contribuinte do ICMS e/ou do ISS no Distrito Federal (DF) está obrigado a escrituração do Super Sintegra, salvo contribuintes enquadrados no Simples Nacional com faturamento anual inferior ao limite estabelecido para os Microempreendedores Individuais (para 2012, o valor é de R$ 60.000,00).

Além de dispensar a escrituração manual dos livros previstos no Ato Cotepe 35/2005, a escrituração do Super Sintegra dispensa a entrega do Sintegra, GIM e DMSP.

O Layout Fiscal de Processamento de Dados está organizado em blocos de informações que, por sua vez, estão organizados em registros que contém dados. Os blocos ainda são dispostos no arquivo, por tipo de documento, por forma de entrega ou por órgão. O arquivo digital será gerado na seguinte forma:

- **Registro 0000** - Abertura do arquivo
- **Bloco 0** - Identificação e referências (registros de tabelas)
- **Blocos de A a Z** - Informações fiscais (registros de dados)
- **Blocos de 1 a 9** - Informações especiais (registros de dados)
- **Registro 9999** - Encerramento do arquivo

| [P](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#preenchimentosiniciais)[reenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#preenchimentosiniciais) |  | [Aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#abaparmetros) |
| --- | --- | --- |
| [Aba Filtros Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#abafiltrosadicionais) |  | [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#botesdatela) |

![Imagem 2: Botões da tela](https://ajuda.sankhya.com.br/hc/article_attachments/1500001950482)

## Preenchimentos iniciais

A primeira informação a ser preenchida é a **"Empresa"** da qual serão gerados os dados para construção do arquivo. Ao manter o campo Empresa em branco, teremos a possibilidade de, previamente à construção do arquivo, selecionar várias ou todas as empresas configuradas para gerar o Super Sintegra.

Defina, na sequência, a **"UF"** a ser considerada para geração do documento.

Em seguida, determine o **"Período"** que irá abranger a geração do arquivo, este período é informado definindo uma data Inicial e Final para geração dos dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#top)

## Aba Parâmetros

Nessa aba, determine inicialmente a **"Finalidade da apresentação"**, ou seja, por qual motivo ele será gerado. Você ainda poderá defini-lo dentre as seguintes opções:

- Remessa regular de arquivo;
- Remessa de arquivo substituto;
- Remessa de arquivo com dados adicionais a arquivo anteriormente remetido;
- Remessa de arquivo requerido por intimação específica;
- Remessa de arquivo requerido para correção do Índice de Participação dos Municípios;
- Remessa de arquivo requerido por ato publicado no Diário Oficial;
- Sintegra - remessa regular de arquivo das operações interestaduais;
- Sintegra - remessa de arquivo substituto das operações interestaduais;
- Sintegra - remessa de arquivo com dados adicionais das operações interestaduais;
- Sintegra - remessa regular de arquivo das operações interestaduais com substituição tributária do ICMS;
- Sintegra - remessa de arquivo substituto das operações interestaduais com substituição tributária do ICMS;
- Sintegra - remessa de arquivo com dados adicinais das operações interestaduais com substituição tributária do ICMS;
- Remessa para a Sefin/Mun de arquivo de retenções do ISS efetuadas por terceiros;
- Remessa para a Sefin/Mun de arquivo substituto de retenções do ISS efetuadas por terceiros;
- Remessa para a Sefin/Mun de arquivo com dados adicionais de retenções do ISS efetuadas por terceiros;
- Emissão de documento;
- Emissão de documento fiscal avulso por repartição fiscal;
- Solicitação de Auditor-Fiscal da Secretaria da Receita Previdenciária através de MPF;
- Entrega na Secretaria da Receita Previdenciária - movimento anual de órgão público, conforme intimação;
- Remessa de informações complementares para a SEFAZ da Unidade da Federação de origem.

Existem duas opções para determinar o **"Tipo de entrada de dados"**:

- Importação de arquivo texto;
- Validação de arquivo texto.

**Nota:** esta informação tem como finalidade a geração do campo **"IND\_ED"** do registro 0000.

Informe na **"Data do inventário"** a data do inventário a ser gerada no arquivo.

Determine o **"Dia Pagto do ISS"**, que é uma informação que será utilizada na geração do campo **"Data de vencimento da obrigação"** (07-DT\_VCTO) do registro B490.

Por fim, nessa aba, determine qual será o **"Custo do Inventário"**. Esse pode ser **"Médio com ICMS"**, **"Médio sem ICMS"**, **"Gerencial"** ou de **"Reposição"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#top)

## Aba Filtros Adicionais

Nessa aba, realize as marcações de quais Blocos e seus respectivos Registros que você deseja que sejam gerados no arquivo.

![Imagem 3: Nessa aba, realize as marcações de quais Blocos e seus respectivos Registros que você deseja que sejam gerados no…](https://ajuda.sankhya.com.br/hc/article_attachments/360103008153)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#top)

## Botões da tela

No alto da tela teremos alguns botões relevantes para a realização do processe, são eles:

O botão **"Gerar Arquivo"**, quando acionado, realiza de acordo com as condições estabelecidas nos [Preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#preenchimentosiniciais), na aba [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#abaparmetros) e na aba [Filtros Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#abafiltrosadicionais), a geração do arquivo.

![Imagem 4: O botão "Gerar Arquivo" , quando acionado, realiza de acordo com as condições estabelecidas nos Preenchimentos iniciais…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001950582)

Já através do botão **"Histórico de Gerações"**, você visualizará o histórico das gerações de arquivo realizadas. Ao acioná-lo, será aberta a seguinte tela:

![Imagem 5: Já através do botão "Histórico de Gerações" , você visualizará o histórico das gerações de arquivo realizadas. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002001061)

O botão **"Consultar Nota Não Gerada"**, quando acionado, permite que você consulte alguma nota que não tenha sido gerada no livro. Será aberto o pop-up **"Consultar Nota Não Gerada"** para preenchimento das informações a respeito da nota:

![Imagem 6: O botão "Consultar Nota Não Gerada" , quando acionado, permite que você consulte alguma nota que não tenha sido gerada…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001950642)

Os campos **"Série"**, **"Data de Negociação"** e **"Empresa"** serão habilitados para preenchimento apenas se o **"Nro. Nota"** for primeiramente informado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607914-Super-Sintegra#top)
