---
id: "360048487613"
titulo: "904 - Rejeição: Informado indevidamente campo valor de pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487613-904-Rejei%C3%A7%C3%A3o-Informado-indevidamente-campo-valor-de-pagamento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:31:49Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Financeiro", "Rejeição 904", "Campo Valor de Pagamento", "Erro"]
---

# 904 - Rejeição: Informado indevidamente campo valor de pagamento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18588816917783) MENSAGEM:**

904 - Rejeição: Informado indevidamente campo valor de pagamento.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588786108311) CAUSA:**

Informado o campo Meio de Pagamento igual a sem pagamento (tag <tPag> =90) e informado campo Valor do Pagamento diferente de zero (tag:vPag<>0).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588816930839) SOLUÇÃO:**

![Imagem 4: Certifique-se que a UF emissora da nota, não conste no parâmetro abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18588816937751) Certifique-se que a UF emissora da nota, não conste no parâmetro abaixo:

- Tela 'Preferências' (Configurações » Avançado » Preferências) >> Chave **UFs que omitem o schema NFe 4.0 v1.60B - UFNFEOMITV160B**

![Imagem 5: Tela 'Preferências' (Configurações » Avançado » Preferências) >> Chave UFs que omitem o schema NFe 4.0 v1.60B -…](https://ajuda.sankhya.com.br/hc/article_attachments/18588786128151)

Foi criado o parâmetro UFNFEOMITV160B (UFs que omitem o schema NFe 4.0 v1.60B) com default vazio. Essa criação ocorreu quando algumas UFs ainda estavam com sua SEFAZ sem implementar esse schema.

![Imagem 6: Caso utilize os módulos Delph (G1 ou Mitra), certifique-se de estar utilizando versões de executáveis atuais.…](https://ajuda.sankhya.com.br/hc/article_attachments/18588816945943) Caso utilize os módulos Delph [G1 ou Mitra], certifique-se de estar utilizando versões de executáveis atuais. [4.23.0.11 ou superior].

![Imagem 7: Após avaliar os dois itens acima, refaça o faturamento. Gere um XML em conferência e avalie se a tag <tPag> = 90, e a…](https://ajuda.sankhya.com.br/hc/article_attachments/18588816955543) Após avaliar os dois itens acima, refaça o faturamento. Gere um XML em conferência e avalie se a tag <tPag> = 90, e a tag <vPag> = 0,00

<detPag>
**<tPag>90</tPag>**
**<vPag>00.00</vPag>**
</detPag>

![Imagem 8: Gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/18588786142359)Gere um novo lote.

**Importante:**

![Imagem 9: Caso para a emissão realizada, não deva ser gerado <tPag> = 90 (Sem pagamento), será necessário junto ao setor…](https://ajuda.sankhya.com.br/hc/article_attachments/18588816937751) Caso para a emissão realizada, não deva ser gerado <tPag> = 90 [Sem pagamento], será necessário junto ao setor financeiro da empresa, reavaliar as marcações abaixo:

- Acesse o cadastro da TOP, e verifique na aba:Geral, o campo 'Financeiro' = [INCLUIR]
- Se a TOP já estiver configurada para gerar financeiro, verifique o Tipo de Titulo vinculado ao Tipo de Negociação usado na NFC-e, acesse o cadastro de tipo de titulo (Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título), aba Geral, campo **'Tipo de pgto para NFC-e / NF-e / CF-e**:' e verifique se está configurado com a opção 90-Sem Pagamento. [Ajuste conforme recomendado pelo Financeiro]

![Imagem 10: Nota Técnica 2016.002 - v 1.60:](https://ajuda.sankhya.com.br/hc/article_attachments/18588816945943) Nota Técnica 2016.002 - v 1.60:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=>
