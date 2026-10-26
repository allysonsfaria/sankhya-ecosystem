---
id: "31322200050839"
titulo: "EFD Contribuições | Registro A100 - Campo COD_PART para operações com consumidor final não identificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31322200050839-EFD-Contribui%C3%A7%C3%B5es-Registro-A100-Campo-COD-PART-para-opera%C3%A7%C3%B5es-com-consumidor-final-n%C3%A3o-identificado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:33:19Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Impostos", "EFD Contribuições", "Registro A100", "Campo COD_PART", "operações com consumidor final não identificado"]
---

# EFD Contribuições | Registro A100 - Campo COD_PART para operações com consumidor final não identificado

Ao gerar documentos cuja emissão foi feita para consumidores finais não contribuintes e não identificados com CPF, o campo de código de participante no registro A100 não deverá ser preenchido e nem será gerado nada no 0150.

Nesse contexto, o campo **COD\_PART** no registro **A100** será gerado em branco nas seguintes situações:

**(1)** Quando a nota fiscal de prestação de serviço estiver vinculada a um parceiro incluído no parâmetro **PARCF2**;

**(1)** Ou, quando todas as condições abaixo forem atendidas:

**(2)**O parceiro estiver configurado como **"Consumidor Final não contribuinte"**;

**(2)**O **CPF/CNPJ** do parceiro estiver:

- - **Vazio** ou
  - **CPF** igual a **"00000000000"** ou
  - **CNPJ** igual a **"0000000000000"**;

**(2)**A razão social do parceiro contiver a expressão **"Consumidor final"**.

Essa regra se aplica exclusivamente ao preenchimento do campo **COD\_PART** no registro **A100** do SPED.
