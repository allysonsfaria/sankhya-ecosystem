---
id: "360042584334"
titulo: "Modelo da NFC-e diferente de 65 (NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042584334-Modelo-da-NFC-e-diferente-de-65-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:05Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Atualização", "SEFAZ", "NFC-e", "775", "Rejeição 775: Modelo NFC-e Incorreto", "Documentos Eletrônicos"]
---

# Modelo da NFC-e diferente de 65 (NT2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443562713879) MENSAGEM:**

[775-Rejeição]: Modelo da NFC-e diferente de 65 (NT2013/005)'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443520668567) SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela **[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)** no  **Sankhya W** acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da rejeição, a seguir.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443520670615) **SOLUÇÃO:**

![Imagem 4: Mantenha sempre a versão do SANNFE atualizada. Isto mantém sempre as URLs de NF-e e NFC-e, atualizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/16443520672791) Mantenha sempre a versão do SANNFE atualizada. Isto mantém sempre as URLs de NF-e e NFC-e, atualizadas.

![Imagem 5: Solicite que seja verificado os endereços das Webservices de destino usado, no arquivo 'url-webservices.xml',…](https://ajuda.sankhya.com.br/hc/article_attachments/16443520676503) Solicite que seja verificado os endereços das Webservices de destino usado, no arquivo 'url-webservices.xml', disponível na pasta 'CONF' do Diretório instalado o SANNFE.

![Imagem 6: Abra o arquivo em um Bloco de Notas. Verifique se para a respectiva UF possui URLS para NF-e e NFC-e separadamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16443520691351) Abra o arquivo em um Bloco de Notas. Verifique se para a respectiva UF possui URLS para NF-e e NFC-e separadamente.

O SANNFE possui URLs de Estados que já estão homologados no arquivo para emissão de NFC-e.

Os estados que possuem a homologação são: AM, BA, DF, GO, MT, MS, PA, PB, PR, RO, RJ, RN, RS, SP.

![Imagem 7: Caso a UF não esteja acima, entre em contato com o Service Desk para análise.](https://ajuda.sankhya.com.br/hc/article_attachments/16443562720023) Caso a UF não esteja acima, entre em contato com o Service Desk para análise.

![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443562721303) **CAUSA:**

Quando for emitida uma NF-e (modelo 55) e seu lote for encaminhado para o Ambiente Autorizador de NFC-e será retornado a rejeição "775 - Modelo da NFC-e diferente de 65".

Exemplo:

Foi emitida uma NF-e (modelo 55) e seu lote foi enviado para o endereço de recepção do ambiente de NFC-e.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443520705431) OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.
