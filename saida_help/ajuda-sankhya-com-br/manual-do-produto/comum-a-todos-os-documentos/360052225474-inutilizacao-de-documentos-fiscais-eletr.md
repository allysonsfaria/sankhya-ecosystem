---
id: "360052225474"
titulo: "Inutilização de documentos fiscais eletrônicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052225474-Inutiliza%C3%A7%C3%A3o-de-documentos-fiscais-eletr%C3%B4nicos"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > Comum a todos os documentos"
atualizado_em: "2026-09-15T15:03:55Z"
rotulos: ["CT-e", "Configuração", "Central de Notas", "NF-e", "SEFAZ", "NFC-e", "Preferências da Empresa", "Inutilização de nota", "Configuração de Parâmetros", "Homologação de Inutilização", "Tratamento de Erros", "Documentos Eletrônicos"]
---

# Inutilização de documentos fiscais eletrônicos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312184562199) Versão disponível: A partir da 4.5
```

---

Agora é possível, no momento da exclusão de documento fiscal eletrônico, que você realize a inutilização da numeração da nota. Veja logo abaixo as premissas e configurações que deverão ser realizadas para você utilizar esta funcionalidade:

**1.** Primeiramente, nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), habilite a marcação **"Enviar inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e)"** e preencha o campo **"Justificativa da inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e)"** com pelo menos 15 caracteres.

[GIF animado: Imagem 2: 1. Primeiramente, nas Preferências da Empresa , aba Propriedades , habilite a marcação "Enviar inutilização de…](https://ajuda.sankhya.com.br/hc/article_attachments/360085402373)

**Observação:** A marcação acima, quando realizada, enviará automaticamente a inutilização de numeração, quando houver exclusão de lançamento confirmado de emissão própria (modelo 55 (NF-e), 65 (NFC-e) e 57 (CT-e), que não esteja aprovado; este envio não será instantâneo mas sim, programado periodicamente de 2 em 2 horas, não sendo configurável.

**2.** Na exclusão da nota, o sistema verificará se a mesma possui todas as características necessárias para inutilizar a numeração automaticamente; se sim, irá armazenar os dados da nota com a situação **"Enviar a inutilização"**, para a futura inutilização da numeração.

**Nota:** Os modelos de documentos previstos para inutilização são: 55 (NF-e), 65 (NFC-e) e 57 (CT-e).

Abaixo, trouxemos as regras válidas aos 3 modelos de documentos acima mencionados:

- A Empresa deve estar com os dois campos (Enviar inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e) / Justificativa da inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e)) configurados;
- A série da nota deve ser numérica;
- A nota deve estar confirmada;
- O número da nota tem que ser maior do que zero;
- E a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) deve atualizar o livro fiscal.

Agora, temos algumas regras para os modelos 55 e 65:

- A [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) tem que estar com o campo **"Ambiente NF-e/NFC-e"** (aba NF-e/NFC-e) configurado como **"Homologação"** ou **"Produção"**;
- A TOP deve estar com o campo **"NF-e"** (aba NF-e/NFC-e) configurado como **"Normal"**, **"Complementar"**, **"Ajuste"** ou **"Devolução"**;
- O campo **"Status NF-e"** da nota deve estar vazio, **"Com erro de validação"** ou **"Aguardando Correção"**;
- E o campo **"Emissão NF-e"** da nota tem que estar vazio ou com uma das seguintes opções selecionadas: **"Sec. da Faz."**, **"S.V.C.Amb.Nacional"** ou **"S.V.C.Rio Grande do Sul"**;

Por fim, temos as regras válidas para o modelo 57:

- A Empresa tem que estar com o campo Ambiente NF-e/NFC-e (aba NF-e/NFC-e) configurado como Homologação ou Produção;
- A TOP deve estar com o campo NF-e (aba NF-e/NFC-e) configurado como Normal ou **"Import. Doc. (Emissão Própria)"**;
- O campo **"Status CT-e"** da nota deve estar vazio, Com erro de validação ou Aguardando Correção;
- E o campo **"Tipo de emissão do CT-e"** da nota tem que estar vazio ou **"Normal"** ou **"Autorização pela SVC-RS"** ou **"Autorização pela SVC-SP"**.

**3.** Processo realizado pelo JOB para enviar a inutilização à SEFAZ:

Habilite o parâmetro **"JOB de inutilização de documento em modo debug - DEBUGJOBINUDOC"** se você desejar ver as mensagens do XML, que é gerado no log do sistema no  momento da inutilização.

Depois, acesse a tela [Console Nf-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734) e dê o play no **"Log detalhado"** na aba [Administração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734-Console-NFe#abaadministra%C3%A7%C3%A3o). Após a inutilização do documento, as informações ficarão disponíveis no log baixado na tela [Administração de servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833) > [Download do Log](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abageral).

A consulta de numerações inutilizadas deve ser feita pelo Portal de Vendas, botão [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo), opção **"Consulta inutilização de numeração de notas"**.

Já, a**"Situação do processamento"** e **"Ocorrência"** serão apresentadas apenas na tabela TGFINUJ, pois o sistema não tem uma tela que demonstre essas informações.

**Nota:** A cada execução do JOB serão capturadas apenas as notas que estão com a situação **"Enviar a inutilização"**.

**Observações:**

- Antes de serem processadas, as notas terão as situações alteradas para **"Em processo de envio"** evitando que outro processo possa utilizá-la;
- No processamento, cada nota será validade e, se existir algum erro nos seus dados ou existir no sistema, alguma outra nota que possua a mesma combinação dos campos que foram a chave para a SEFAZ (Empresa, Série, Número e Modelo de documento), a situação será alterada para **"Inutilização descartada pelo Job"** e, no campo Ocorrência terá uma mensagem de erro.
- Ao ser enviada para a SEFAZ, a situação da nota será alterada para **"Com erro na inutilização"** ou **"Inutilização homologada"**, dependendo do retorno dado pela SEFAZ, o campo Ocorrência terá a mensagem relativa à situação.
- A tabela que contém as notas e o resultado do processamento pelo JOB não terá as informações da homologação da inutilização, ou seja, essas informações continuam sendo gravadas na tabela TGFINUJ (tabela utilizada pelos pop-up's do Portal de Notas que tratam a inutilização de numeração).

**Importante:** no parâmetro **"UF's aceitam inutilização NF-e de pessoa física. - UFACEINUTNFECPF"**, informe as UF's que permitem a inutilização de NF-e para pessoa física. Por padrão, o estado do MT vem inserido nesse parâmetro.

Caso a Empresa esteja marcada como **"Produtor Rural"** ([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral)), ao enviar o evento de inutilização, a tag CNPJ será alterada para CPF, sendo que, essa regra será válida apenas para o estado do MT.
