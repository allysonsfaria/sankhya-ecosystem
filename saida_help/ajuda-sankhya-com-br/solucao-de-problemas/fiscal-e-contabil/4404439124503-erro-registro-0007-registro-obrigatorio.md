---
id: "4404439124503"
titulo: "Erro registro 0007: Registro Obrigatório não encontrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404439124503-Erro-registro-0007-Registro-Obrigat%C3%B3rio-n%C3%A3o-encontrado"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:23:15Z"
rotulos: ["Configuração", "ECD", "Fiscal", "Preferências", "#ValidadoThiagoArantes", "Marcar registro nas preferências da empresa", "Inclui inscrições cadastrais obrigatórias", "Registro obrigatório não encontrado", "Erro", "ID_Bacen"]
---

# Erro registro 0007: Registro Obrigatório não encontrado

Neste registro devem ser incluídas as inscrições cadastrais da pessoa jurídica que, legalmente, tenham direito de acesso ao livro contábil digital.

O código da empresa no Banco Central corresponde ao “ID\_Bacen”, conforme registrado no Unicad (Informações sobre Entidades de Interesse do Banco Central), composto por 8 dígitos e iniciados com a letra "Z".

Em alguns casos,  ocorre o erro abaixo, registro obrigatório não encontrado:

![Imagem 1: Em alguns casos, ocorre o erro abaixo, registro obrigatório não encontrado:](https://ajuda.sankhya.com.br/hc/article_attachments/4404428509975)

**Para a resolução do incidente, siga os passos abaixo:**

![Imagem 2: Marque o registro para gerar nas preferências da empresa. Esse erro é gerado com as informações presentes na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16347394038295) Marque o registro para gerar nas preferências da empresa.

![Registro](https://ajuda.sankhya.com.br/hc/article_attachments/15686384353559)

![Imagem 4: Marque o registro para gerar nas preferências da empresa. Esse erro é gerado com as informações presentes na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16347410155671) Esse erro é gerado com as informações presentes na tela **"Preferências da Empresa"** (Caminho de acesso: contabilidade » Preferências), aba **"Instituição Responsável".**

![Registro](https://ajuda.sankhya.com.br/hc/article_attachments/15686405892247)

Link do Guia Prático da Receita:

<http://sped.rfb.gov.br/estatico/0F/F1E89FBAAB0B00C9B795215D2ED40ECD82A164/Manual_de_Orienta%c3%a7%c3%a3o_da_ECD_2020_Dezembro_Leiaute_9%20(2020-12-17).pdf>

**Trecho do Guia Prático**

**IV – Regras de Validação dos Campos:**

(1)** REGRA\_TABELA\_INSTITUICOES\_CADASTRO:** verifica se o código informado no campo código da instituição responsável pela administração do cadastro – COD\_ENT\_REF (Campo 02) – existe na Tabela de
Instituições Responsáveis pela Administração do Cadastro das Entidades. Se a regra não for cumprida, o PGE do Sped Contábil gera um erro.

(1)** REGRA\_VALIDA\_INSCRICAO:** verifica qual é a regra de formação do campo código cadastral da pessoa jurídica – COD\_INSCR (Campo 03) – que deve ser aplicada, a partir do preenchimento do campo código da instituição responsável pela administração do cadastro – COD\_ENT\_REF (Campo 02).
Para “COD\_ENT\_REF = 01”, executa a “REGRA\_VALIDA\_ID\_BACEN”.
Para “COD\_ENT\_REF = 02”, executa a “REGRA\_VALIDA\_ID\_SUSEP”.
Para o “COD\_ENT\_REF = 03”, executa a “REGRA\_VALIDA\_ID\_CVM”.
As regras acima (Bacen, Susep e CVM) verificam se a regra de formação do código de inscrição é válida. Se não forem cumpridas, o PGE do Sped Contábil gera um aviso.

**V - Exemplo de Preenchimento:**

**|0007|01|Z1234567|**
Campo 01 – Tipo de Registro: 0007
Campo 02 – Código da Instituição Responsável pela Administração do Cadastro: 01 (Bacen)
Campo 03 – Código Cadastral: Z1234567

![Imagem 6: |0007|01|Z1234567| Campo 01 – Tipo de Registro: 0007 Campo 02 – Código da Instituição Responsável pela Administração do…](https://ajuda.sankhya.com.br/attachments/token/AQKpNFRbMCkA8gPMhxs7PLlHS/?name=inline853967228.png)
