---
id: "4406737442199"
titulo: "Geração de Arquivos Remessa NFST Modelos 21 e 22"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4406737442199-Gera%C3%A7%C3%A3o-de-Arquivos-Remessa-NFST-Modelos-21-e-22"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Rotinas descontinuadas"
atualizado_em: "2026-09-15T17:29:22Z"
rotulos: ["Configuração", "Livros Fiscais", "SEFAZ", "br.com.sankhya.mgeliv.mov.cabdedocmodelo21e22", "NFST MODELOS 21 E 22", "Emissão Notas Fiscais: Modelos 21 e 22", "Geração Arquivos: Texto via TED CD DVD", "Dados Divididos: 100 mil (CD) ou 1 milhão (DVD)", "Documentos Eletrônicos", "NFST"]
---

# Geração de Arquivos Remessa NFST Modelos 21 e 22

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313109432983) Módulo: Livros Fiscais > Conexão       ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313139546647) Versão disponível: a partir da 4.7
```

---

Por meio dessa tela, pode-se realizar a emissão de notas fiscais nos modelos 21, referente à Comunicação e, o modelo 22, sendo esta, pertinente às telecomunicações. Esses modelos são emitidos por empresas contribuintes do ICMS em via única, ou seja, que não possuem XML ou DANFE.

Esses modelos não são atualizados pela SEFAZ, portanto, não existem webservices para realizar o tráfego de informações, assim, essas notas são enviadas através de arquivos de texto via TED ou por uma mídia (CD ou DVD) diretamente da SEFAZ.

![Imagem 3: Esses modelos não são atualizados pela SEFAZ, portanto, não existem webservices para realizar o tráfego de informações,…](https://ajuda.sankhya.com.br/hc/article_attachments/4406732863895)

No **"Painel Principal"** da tela, você deve, primeiramente, informar a **"Empresa"** a qual deseja efetuar a geração dos arquivos.

Posteriormente, informe a **"Dt. de Referência"** da geração, a considerar a data da emissão.

No campo **"Finalidade"**, você deve selecionar uma dentre as opções **"N - Normal"** e **"S - Substituto"** para determinar a finalidade do arquivo que será gerado.

Após o preenchimento desses campos, realize o processamento por meio do botão **"Processar"** para que as notas persistentes às informações preenchidas sejam carregadas na tela.

---

![Imagem 4: Informações adicionais sobre a Geração de Arquivos de Remessa:](https://ajuda.sankhya.com.br/hc/article_attachments/19276595244439) **Informações adicionais sobre a Geração de Arquivos de Remessa:**

- Mesmo que o nome da cidade seja cadastrado conforme o parâmetro **"Padrão para DESCRIÇÃO dos cadastros - PADRAOENTRDADOS"** diferente de **"Normal"**, na tela Geração de Arquivos Remessa NFST Modelos 21 e 22, o campo **"Cidade"** da aba **"Destinatário Doc. Fiscal Modelo 21 e 22"** será registrado seguindo o padrão IBGE, ou seja, o padrão Normal.
- Mesmo que no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo), o campo **"Telefone"** esteja configurado com o DDI + DDD + telefone celular, quando as notas fiscais nos modelos 21 e 22 para este parceiro forem geradas, será registrado no campo **"Telefone de Contato"**, presente na sub-aba **"Destinatário Doc. Fiscal Modelo 21 e 22"**, apenas o DDD + telefone celular.
- Ao processar os Arquivos Remessa NFST Modelos 21 e 22, considerando o parâmetro **"Gera Dt. Inicio e Dt. Término da Prestação na NFST - GERDTINIFIMNFST"** ativado, os campos **"Dt. Leitura anterior"** e **"Dt. Leitura atual"** serão preenchidos com a data inicial e final da referência da nota. Assim, durante a geração do arquivo, as datas informadas nos campos Dt. Leitura anterior e Dt. Leitura atual da nota serão utilizadas para compor os campos **"Data Início da Prestação"** e **"Data Término da Prestação"**.

---

A geração desses arquivos devem ser realizadas mensalmente, de modo que, contenha todas as informações dos documentos fiscais emitidos no mês. Destaca-se ainda que, em razão da grande quantidade de dados a serem apresentados, os arquivos deverão ser divididos em volumes que contenham 100 (cem) mil documentos fiscais, se estes forem exibidos em CD-R, ou volumes contendo 1 (um) milhão de documentos fiscais, se evidenciados em DVD-R. Sendo assim, observe o exemplo:

Se determinado contribuinte emitir 4.513.091 em certo mês, este deverá apresentar as informações referentes aos documentos fiscais emitidos em DVD-R, devendo os arquivos serem gerados em 5 volumes, com os quatro primeiros contendo os dados de 1 milhão de documentos fiscais e o último contendo as informações dos 513.091 documentos fiscais restantes.

Dessa forma, confira a seguir, exemplos de como os nomes e extensões dos Arquivos de Remessa, serão identificados:

MG6529517200018522B-12012+N+01\*M.\*001 = Mestre
MG6529517200018522B-12012+N+01\*D.\*001 = Destinatário
MG6529517200018522B-12012+N+01\*I.\*001 = Itens

MG6529517200018522B-12012+N+01\*C.\*001 = Controle e Identificação - Este arquivo é gerado por aplicativo específico disponibilizado pela Secretaria da Fazenda.

Após preencher os campos e gerar o arquivo, o sistema trará os arquivos quebrados por modelo e série. Então, se no período selecionado houverem notas nos modelos 21 e 22 e séries A e B, um total de 6 (seis) arquivos serão trazidos, sendo estes, 3 para o modelo 21, série A, e 3 (três) arquivos do modelo 22, série B.

Os arquivos serão gerados com o nome destes do tipo **"M"**, **"D"** e **"I"** vinculados ao CNPJ da empresa da seguinte forma:

**(1)** Arquivo Mestre sendo este a junção de dados da nota fiscal;

**(1)** O Arquivo Destinatário com as informações do tomador de serviço e, por fim;

**(1)** O Arquivo Item do Documento Fiscal que remete às informações dos itens da nota fiscal.

![Imagem 5: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16311165024407) Acesse também:

[Configurações para Emissão de NF Modelo 21 e 22](https://ajuda.sankhya.com.br/hc/pt-br/articles/7405986347799-Configura%C3%A7%C3%B5es-Para-Emiss%C3%A3o-de-NF-Modelo-21-e-22)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406737442199-Gera%C3%A7%C3%A3o-de-Arquivos-Remessa-NFST-Modelos-21-e-22#top)
