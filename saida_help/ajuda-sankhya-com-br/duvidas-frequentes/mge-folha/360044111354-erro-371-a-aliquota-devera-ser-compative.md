---
id: "360044111354"
titulo: "Erro 371 - A alíquota deverá ser compatível como CNAE preponderante informado. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111354-Erro-371-A-al%C3%ADquota-dever%C3%A1-ser-compat%C3%ADvel-como-CNAE-preponderante-informado-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:58Z"
rotulos: ["e-social", "Alíquotas", "Configuração", "eSocial", "Central do eSocial", "Verificar e corrigir CNAE e alíquota", "Preencher corretamente CNAE taxas e transmitir novamente", "Alíquota incompatível com CNAE", "CNAE", "Erro"]
---

# Erro 371 - A alíquota deverá ser compatível como CNAE preponderante informado. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16980897198615) MENSAGEM:**

401 - Conteúdo do evento inválido. Erro 371 - A alíquota deverá ser compatível como CNAE preponderante informado.

Ação Sugerida: Verifique se a alíquota e o CNAE estão corretos. Elemento:/eSocial/evtTabEstab/infoEstab/inclusao/dadosEstab/aliqGilrat/aliqRat [0]”

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16980897203479) SITUAÇÃO:**

Ao tentar Transmitir o arquivo do eSocial, apresenta a rejeição.

**![Imagem 3: SOLUÇÃO: Para correção deste erro, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16980897204887) SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse: MGEPessoal » Arquivos » Cadastros » Empresas (Dados Básicos) Aba: "Natureza" Campo " CNAE preponderante"](https://ajuda.sankhya.com.br/hc/article_attachments/16980865838743) Acesse: MGEPessoal » Arquivos » Cadastros » Empresas (Dados Básicos)
Aba: **"Natureza"**
Campo **"CNAE preponderante"**

Acesse o Decreto 3.048 através do link: [http://www.planalto.gov.br/ccivil\_03/decreto/d3048.htm](http://www.planalto.gov.br/ccivil_03/decreto/d3048.htm%20) e localize o CNAE da empresa.

Lembrando que deverá ser consultada a listagem disponível no **Anexo V** e o número do CNAE não pode estar riscado.

Preencha o campo CNAE preponderante, salve o Registro.

Dúvidas, consulte a Área Fiscal da Empresa para o correto preenchimento

![Imagem 5: Acesse: MGEPessoal » Avançado » Registro Fiscal Verifique se o "Percentual de Taxa de Seguro" e "Cód. FPAS" , estão…](https://ajuda.sankhya.com.br/hc/article_attachments/16980865842455) Acesse: MGEPessoal » Avançado » Registro Fiscal
Verifique se o **"Percentual de Taxa de Seguro"** e **"Cód. FPAS"**, estão preenchidos

![Imagem 6: Acesse: MGEPessoal » Avançado » Central do eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/16980897211159) Acesse: MGEPessoal » Avançado » Central do eSocial.

Transmita novamente as obrigações.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16980865847703)CAUSA:**

Ao tentar transmitir o eSocial e os dados do CNAE não estiverem devidamente preenchidos no cadastro de Empresas, será causado o erro no evento evento S-1000.

**![Imagem 8: OBSERVAÇÃO: Manual Orientação do eSocial](https://ajuda.sankhya.com.br/hc/article_attachments/16980897214615) OBSERVAÇÃO:**
[Manual Orientação do eSocial](http://portal.esocial.gov.br/manuais/mos-manual-de-orientacao-do-esocial-2-4-publicada.pdf/@@download/file/MOS%20Manual%20de%20Orienta%C3%A7%C3%A3o%20do%20eSocial%20-%202.4.pdf)
