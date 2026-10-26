---
id: "360044618233"
titulo: "O valor '' do elemento 'tpRegJor' não é válido. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618233-O-valor-do-elemento-tpRegJor-n%C3%A3o-%C3%A9-v%C3%A1lido-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:11Z"
rotulos: ["eSocial/evtAdmissao/vinculo/infoRegimeTrab/infoCeletista/tpRegJor", "Configuração", "Contrato", "XML", "eSocial", "Central do eSocial", "Valor Inválido no Campo 'tpRegJor'", "Erro"]
---

# O valor '' do elemento 'tpRegJor' não é válido. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603025102103) MENSAGEM:**

"Campo obrigatório com valor não informado. [observação]
cvc-pattern-valid: O valor '' não tem um aspecto válido em relação ao padrão '\d' do tipo '#AnonType\_tpRegJorinfoCeletistainfoRegimeTrabvinculoevtAdmissaoeSocial'.
cvc-type.3.1.3: O valor '' do elemento 'tpRegJor' não é válido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603025103255) SITUAÇÃO:**

Ao tentar transmitir o arquivo do E-social, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603025104535) SOLUÇÃO:**

![Imagem 4: MGEPessoal>>Arquivos>>Funcionários](https://ajuda.sankhya.com.br/hc/article_attachments/18603030332055) MGEPessoal>>Arquivos>>Funcionários

Aba: Contrato

Marque uma das opções do campo: **Regime Trabalhista**

Marque uma das opções do campo: **Regime Jornada**

Salve a alteração

![Imagem 5: MGEPessoal>>Avançado>>Central do E-social.](https://ajuda.sankhya.com.br/hc/article_attachments/18603025114775) MGEPessoal>>Avançado>>Central do E-social.

Transmita novamente as obrigações.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603025115415) CAUSA:**

Ocorre quando as informações do Tipo de Regime Trabalhista e Jornada do Funcionário não está configurado corretamente.

**Observação:**Evento: S-2200, [Manual Orientaçao do ESocial](https://portal.esocial.gov.br/manuais/mos-v-2-4-02-publicada-cg.pdf)
