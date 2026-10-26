---
id: "26976140354071"
titulo: "Erro de geração no R4020 - cvc-pattern-valid: Value \"\" is not facet-valid with respect to pattern '[0-9]{2}':"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26976140354071-Erro-de-gera%C3%A7%C3%A3o-no-R4020-cvc-pattern-valid-Value-is-not-facet-valid-with-respect-to-pattern-0-9-2"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:24Z"
rotulos: ["Configuração", "XML", "Impostos", "Erro de geração no R4020", "cvc-pattern-valid", "Value \"\" is not facet-valid with respect to pattern '[0-9]{2}", "Erro", "EFD-REINF"]
---

# Erro de geração no R4020 - cvc-pattern-valid: Value "" is not facet-valid with respect to pattern '[0-9]{2}':

O erro cvc-pattern-valid está relacionado à **validação de padrões em XML** com base em um esquema (XSD). O **cvc** (constraints validation context) é um prefixo que indica uma verificação de restrições no contexto da validação de um documento XML em relação ao seu esquema.

Especificamente significa que o valor de um elemento ou atributo XML não atende ao padrão definido no esquema.

- **cvc-pattern-valid: Value "" is not facet-valid with respect to pattern '[0-9]{2}':** indica que o elemento frmTribut espera um valor numérico de 2 dígitos (por exemplo, "01", "99"). O erro ocorre porque o valor para frmTribut está vazio (""), o que viola o padrão esperado.

![Imagem 1: cvc-pattern-valid: Value "" is not facet-valid with respect to pattern '(0-9){2}': indica que o elemento frmTribut…](https://ajuda.sankhya.com.br/hc/article_attachments/27061509055767)

Verificando a Tabela 3 Temos os seguintes possíveis valores

![Imagem 2: Verificando a Tabela 3 Temos os seguintes possíveis valores](https://ajuda.sankhya.com.br/hc/article_attachments/27061509059607)

**Link da tabela 2: regras para utilização dos códigos de pagamento a Pessoas Físicas** <http://sped.rfb.gov.br/estatico/AE/C60E9D9BF5128AA07A232DAA39A6A42F8D7724/Leiautes%20da%20EFD-Reinf%20v1.1%20-%20Anexo%20I%20-%20Tabelas.pdf>

Quando as retenções forem sobre rendimentos de beneficiários domiciliados no exterior, acesse a tela **"Impostos"** (Configurações > Cadastros > Impostos) e preencha o campo **"Tributação IRRF - Exterior REINF",** conforme (Tabela 02 do Reinf), somente para o tipo de imposto IRF.

![Imagem 3: Quando as retenções forem sobre rendimentos de beneficiários domiciliados no exterior, acesse a tela "Impostos"…](https://ajuda.sankhya.com.br/hc/article_attachments/27061488635415)

Envolvendo Processos Administrativos/Judiciais, informe na tela **"Livros Fiscais"** (Arquivos > Processos Administrativos Judiciais), no campo **"Advogado Atuante no processo"**.

![Imagem 4: Envolvendo Processos Administrativos/Judiciais, informe na tela "Livros Fiscais" (Arquivos > Processos Administrativos…](https://ajuda.sankhya.com.br/hc/article_attachments/27061509071639)

**Verifique demais configurações de  de parceiro no exterior  >** <https://ajuda.sankhya.com.br/hc/pt-br/articles/12273471043863-Ebook-Reinf#h_01H0JS9J3TV7RRM3SYYHE8172F>
