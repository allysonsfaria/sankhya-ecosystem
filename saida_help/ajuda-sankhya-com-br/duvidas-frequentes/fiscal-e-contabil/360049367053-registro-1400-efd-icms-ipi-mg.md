---
id: "360049367053"
titulo: "Registro 1400 - EFD ICMS/IPI - MG"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049367053-Registro-1400-EFD-ICMS-IPI-MG"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:31:25Z"
rotulos: ["Configuração", "IPI", "SEFAZ", "ICMS", "Impostos", "EFD", "Registro 1400: Informação sobre valores agregados.", "Causa: Decreto 47.861/2020 e Resolução 5.369/2020.", "Configuração: Marque em 'Preferências' 'Tipos de Operação' e 'Códigos de itens'.", "MG"]
---

# Registro 1400 - EFD ICMS/IPI - MG

**REGISTRO 1400 - EFD ICMS/IPI - Informação sobre valores agregados:**

A partir de 2020 (VAF ano-base 2019) a 'Declaração Anual do Movimento Econômico Fiscal - DAMEF' do contribuinte Débito/Crédito ou Isento/Imune será apurada pela SEF/MG através dos arquivos de Escrituração Fiscal Digital - EFD.

Decreto nº 47.861 de 10 de fevereiro de 2020 - Altera o Regulamento  do ICMS/ RICMS, aprovado pelo Decreto nº 43.080, de 13 de dezembro de 2012.

Em seguida estabelece a obrigatoriedade de apresentação do Registro 1400 da Escrituração Fiscal Digital - EFD - e institui o **Manual de Orientação para a Geração do Registro 1400 da EFD**, através da Resolução nº 5.953/2025

**Qual a composição do Registro 1400?**

01 - REG - Texto fixo contendo "1400"

02 - COD\_ITEM\_IPM - Código do item (Tabela própria da unidade da federação(Tabela de Itens UF Índice de Participação dos Municípios) ou campo 02 do Registro 0200

03 - MUN - Código do Município de origem/destino

04 - VALOR -  Valor mensal correspondente ao município

**Quais as configurações no sistema para geração do Registro 1400 ?**

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/20471301547927) Acesse as preferências da 'Empresa' (Comercial » Preferências » Empresa) e verificar se o Registro 1400 está marcado para gerar no respectivo Bloco:

- Aba EFD-Escrituração Fiscal digital >> Tipo de escrituração: EFD
- Bloco:1
- Registro:1400- Informação sobre valores agregados

![Imagem 2: Registro:1400- Informação sobre valores agregados](https://ajuda.sankhya.com.br/hc/article_attachments/19580820212759)

![Imagem 3: Na tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) >> Aba Fiscal, o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19580866780439) Na tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) >> Aba Fiscal, o campo **"Gerar Registro 1400 no SPED Fiscal?"** deve estar marcado.

![Imagem 4: Na tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) >> Aba Fiscal, o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/360072147654)

- A marcação deve ser realizada nas TOP's das notas com as operações envolvidas e pertinentes a este registro 1400.
- Esse campo na TOP é histórico, ou seja  vai ser valido apenas a utilização da TOP do momento que marcar em diante.
- Quais TOP's devo marcar? Essa será uma definição da empresa, juntamente com a equipe de contabilidade, a partir da análise da legislação pertinente.

![Imagem 5: Acesse a tela 'Códigos de itens (IPM) por UF no registro 1400' (Livros Fiscais > Avançado > Escrituração Fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/19580866783127) Acesse a tela **'Códigos de itens (IPM) por UF no registro 1400'** (Livros Fiscais > Avançado > Escrituração Fiscal Digital):

Maiores informações sobre as funcionalidades dessa rotina, acesse: [Códigos de itens (IPM) por UF no registro 1400](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093)

- Importe a tabela e cadastrar os produtos e grupo de produtos na tela "Códigos de itens (IPM) por UF no registro 1400".
- Solicite a tabela ao Contador responsável pela empresa, e/ou extraia através do Portal SPED:

  [http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal.](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)
- Abaixo segue exemplo de tabela UF MG:

![Imagem 6: Abaixo segue exemplo de tabela UF MG:](https://ajuda.sankhya.com.br/hc/article_attachments/19580866790551)

![Imagem 7: Abaixo segue exemplo de tabela UF MG:](https://ajuda.sankhya.com.br/hc/article_attachments/19580820252695)

![Imagem 8: Abaixo segue exemplo de tabela UF MG:](https://ajuda.sankhya.com.br/hc/article_attachments/19580820263831) Gere o arquivo EFD e certifique-se que o registro foi devidamente gerado, conforme exemplo abaixo:

1400|Produtos\_Agropecuarios|3117603|171084,72|

|1400|Produtos\_Agropecuarios|3126000|344873,80|

|1400|Produtos\_Agropecuarios|3130200|142142,44|

|1400|Produtos\_Agropecuarios|3145802|36937,60|

|1400|Produtos\_Agropecuarios|3147105|2427393,07|

|1400|Produtos\_Agropecuarios|3163102|1006170,74|

**Observações:**

De acordo com o Guia Prático este registro tem como objetivo fornecer informações para o cálculo do valor adicionado por município, sendo utilizado para subsidiar cálculos de índices de participação e deve ser apresentado apenas se a unidade federada do declarante assim o exigir.

Vide: [Guia Prático EFD-ICMS/IPI – Versão 3.0.3 Atualização: 14 de outubro de 2019, Página 253 à 304](http://sped.rfb.gov.br/estatico/0D/434EFF065B893AB70D59AD102A946DC9237680/2019.05.21_GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%203.0.3%20-%20v3%20para%20publica%c3%a7%c3%a3o.pdf)
