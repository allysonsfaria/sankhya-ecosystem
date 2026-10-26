---
id: "26977642821527"
titulo: "Erro de geração no R4020 - cvc-pattern-valid: Value \"\" is not facet-valid with respect to pattern '\\d{3}'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26977642821527-Erro-de-gera%C3%A7%C3%A3o-no-R4020-cvc-pattern-valid-Value-is-not-facet-valid-with-respect-to-pattern-d-3"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:22Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Cidades", "XML", "Erro de geração no R4020", "is not facet-valid with respect to pattern", "cvc-pattern-valid: Value", "EFD-REINF"]
---

# Erro de geração no R4020 - cvc-pattern-valid: Value "" is not facet-valid with respect to pattern '\d{3}'

O erro **cvc-pattern-valid** está relacionado à **validação de padrões em XML** com base em um esquema (XSD). O **cvc** (constraints validation context) é um prefixo que indica uma verificação de restrições no contexto da validação de um documento XML em relação ao seu esquema.

Especificamente significa que o valor de um elemento ou atributo XML não atende ao padrão definido no esquema. 

- **cvc-pattern-valid: Value "" is not facet-valid with respect to pattern '\d{3}'**:
  - o elemento relFontPg espera um valor que corresponda ao padrão \d{3}, ou seja, deve ser um número de 3 dígitos (por exemplo, "123"). No entanto, o valor fornecido para relFontPg está vazio, o que viola a regra do padrão.

![Imagem 1: o elemento relFontPg espera um valor que corresponda ao padrão \d{3}, ou seja, deve ser um número de 3 dígitos (por…](https://ajuda.sankhya.com.br/hc/article_attachments/27115170268951)

Verificando a Tabela 3 Temos os seguintes possíveis valores

![Imagem 2: Verificando a Tabela 3 Temos os seguintes possíveis valores](https://ajuda.sankhya.com.br/hc/article_attachments/27115134283799)

**Link da tabela 3 - Rendimentos de Beneficiários no Exterior:**

<http://sped.rfb.gov.br/estatico/AE/C60E9D9BF5128AA07A232DAA39A6A42F8D7724/Leiautes%20da%20EFD-Reinf%20v1.1%20-%20Anexo%20I%20-%20Tabelas.pdf>

![Imagem 3: Acesse a tela "Cidades" - deve ter cadastrado a Cidade do Exterior:](https://ajuda.sankhya.com.br/hc/article_attachments/27115134288151)Acesse a tela **"Cidades" -** deve ter cadastrado a Cidade do Exterior:

- Campo **"Identificação de Estrangeiro"** preenchido
- O **"Mun. domicílio fiscal"** informa 9999999

![Imagem 4: O "Mun. domicílio fiscal" informa 9999999](https://ajuda.sankhya.com.br/hc/article_attachments/27115134290327)

**Importante:** essa configuração irá habilitar os campos da parte **"Informações para REINF"** na aba **"Fiscal"**, onde será possível configurar o **"Tipo Relação fonte pagadora"**.

![Imagem 5: Importante: essa configuração irá habilitar os campos da parte "Informações para REINF" na aba "Fiscal" , onde será…](https://ajuda.sankhya.com.br/hc/article_attachments/27115170281879)

- Na tela **"Parceiros",** aba **"Endereço",** configure endereço com a Cidade

![Imagem 6: Na tela "Parceiros", aba "Endereço", configure endereço com a Cidade](https://ajuda.sankhya.com.br/hc/article_attachments/27115170286487)

- Na tela **"Parceiros",**aba **"Fiscal",** sessão **"Informações para REINF",**  configure o campo Tipo Relação fonte pagadora

![Imagem 7: Na tela "Parceiros", aba "Fiscal", sessão "Informações para REINF", configure o campo Tipo Relação fonte pagadora](https://ajuda.sankhya.com.br/hc/article_attachments/27115170289687)

**Verificar as [configurações de parceiro no exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/12273471043863-Ebook-Reinf#h_01H0JS9J3TV7RRM3SYYHE8172F)**
