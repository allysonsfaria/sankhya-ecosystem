---
id: "360044594674"
titulo: "Nota MS Premiada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594674-Nota-MS-Premiada"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:19Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Programa Nota MS Premiada: Configurações e Legislação"]
---

# Nota MS Premiada

O Programa Nota MS Premiada, instituído pela Lei nº 5.463, de 16 de dezembro de 2019, tem por objetivo fomentar a cidadania fiscal no Estado de Mato Grosso do Sul, estimulando os adquirentes de mercadorias ou de bens a exigir do fornecedor localizado neste Estado, a emissão de documento fiscal hábil.

Tanto o MGE, quanto o Sankhya-W e o Fast estão preparados para atender este programa de premiação. 

**Configurações Necessárias**

1) Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba **"NF-e/NFC-e"**, é necessário marcar a opção **"Tem programa de premiação estadual?"**;

2) Para emissão de NFC-e,  se o cliente deseja participar do programa o seu CPF deverá ser preenchido. Dessa forma, para facilitar pode-se utilizar o [Consumidor Padrão Identificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863514).

**Legislação**

Segue abaixo a legislação do Estado do Mato Grosso do Sul referente ao programa Nota MS Premiada. Neste decreto é abordado todas as premissas necessárias para receber as dezenas no XML de retorno. 

Em seu art. 2º, para efeito de participação do consumidor final no sorteio do Programa Nota MS Premiada, o documento fiscal emitido pelo estabelecimento do contribuinte estabelecido no território sul-mato-grossense, fornecedor de bens ou mercadorias, deve obedecer aos seguintes parâmetros e especificações técnicas:

**I –** o número do CPF, de que trata o § 1º do art. 8º do Decreto nº 15.341, de 23 de dezembro de 2019, deve ser preenchido no campo específico: (tag CPF, grupo E. Identificação do Destinatário da Nota Fiscal eletrônica) na NFC-e ou na NF-e correspondente;

**II –** o algoritmo criptográfico, de que trata o § 1º do art. 9º do Decreto nº 15.341, de 23 de dezembro de 2019, ocorre pelo uso da classe RANDOM (pacote java.util) para a geração de diferentes tipos de séries de números aleatórios, de 01 (um) a 60 (sessenta), em JAVA.

**III –** em relação ao art. 10 do Decreto nº 15.341, de 23 de dezembro de 2019, deve ser observado o seguinte: a) somente serão aceitos os modelos de documento fiscal “tag mod” 55 (NF-e) e “tag mod” 65 (NFC-e), devendo constar no arquivo XML, transmitido pelo contribuinte:

Valor da NF-e/NFC-e maior ou igual a R$ 1,00 (um real);

NF-e/NFC-e emitidas por contribuintes de Mato Grosso do Sul (tag UF\_EMIT = MS); 3. NF-e/NFC-e com CPF do destinatário devidamente preenchido;

NF-e/NFC-e com CPF do destinatário devidamente preenchido;

NF-e/NFC-e com a Inscrição Estadual (IE) do destinatário, tag IE, não preenchida (NULL) ou preenchida com literal “ISENTO”;

NF-e/NFC-e com o indicador operação com consumidor final, tag indfinal = 1 (Consumidor Final);

NF-e/NFC-e com a finalidade de emissão da NF-e/NFC-e, tag finnfe = 1 (Normal);

NF-e/NFC-e com o identificador de local de destino da operação, tag iddest = 1 (operação Interna);

No caso de NF-e:

**8.1** que contenha o indicador da IE do destinatário, tag indiedest = 9 (Não Contribuinte) ou 2 (Isento);

**8.2** com tipo de emissão da NF-e, tag tpemis = 1 (emissão Normal) ou 2 (FS – Formulário de Segurança) ou 5 (FS-DA – Formulário de Segurança de Documento Auxiliar) ou = 4 (EPEC – Emissão Prévia de Emissão em Contingência), observado o disposto na alínea “c” deste inciso;

No caso de NFC-e:

**9.1** com tag indiedest = 9 (Não Contribuinte);

**9.2** considerar o tipo de emissão da NF-e, tag tpemis = 1 (emissão Normal) ou 9 (emissão em contingência Off-Line), observado o disposto na alínea “c” deste inciso; b) somente serão aceitos documentos fiscais com Código Fiscal de Operações e Prestações (CFOP):

No caso de NF-e: 5.101, 5.102, 5.103, 5.104, 5.115, 5.116, 5.117, 5.118, 5.119, 5.120, 5.401, 5.403, 5.405, 5.551, 5.653, 5.656, 5.667 e 5933;

No caso de NFC-e: 5.101, 5.102, 5.103, 5.104, 5.115, 5.405, 5.656, 5.667 e 5933; c) somente após a transmissão do arquivo XML e sua autorização pela SEFAZ/MS serão geradas as dezenas para concorrência ao sorteio, em caso de:

Emissão em contingência modo “off-line” da NFC-e;

Emissão em contingência FS, FS-DA e EPEC da NF-e; d) não gerará o direito de concorrência no sorteio as Notas Fiscais Avulsas Eletrônicas (NFA-e) emitidas pela SEFAZ-MS, identificadas pelas séries numeradas de 890 a 899; e) no caso de NF-e autorizada com a tag tpemis=7 (SVC-RS – SEFAZ Virtual de Contingência do Rio Grande do Sul) não serão geradas dezenas, em função de o ambiente autorizador ser diverso da SEFAZ-MS.
