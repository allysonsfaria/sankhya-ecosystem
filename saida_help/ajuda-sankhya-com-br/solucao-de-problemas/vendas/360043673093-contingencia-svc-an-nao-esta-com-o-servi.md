---
id: "360043673093"
titulo: "Contingência \"SVC-AN\" não está com o serviço em operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673093-Conting%C3%AAncia-SVC-AN-n%C3%A3o-est%C3%A1-com-o-servi%C3%A7o-em-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:46Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Contingência", "Verificar internet certificado firewall", "Configurar EPEC contingência", "Erro SEFAZ contingência", "Erro", "Documentos Eletrônicos"]
---

# Contingência "SVC-AN" não está com o serviço em operação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16120689186967) MENSAGEM:**

Contingência "SVC-AN" não está com o serviço em operação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120689191959) SOLUÇÃO:**

A mensagem acima será retornada quando a comunicação com a SEFAZ através do ambiente 'Normal' não está sendo efetiva. Essa situação pode ocorrer por motivos diversos, tais como:

- Indisponibilidade nos serviços de autorização da SEFAZ;
- Internet Indisponível no servidor onde encontra-se instalado o SANNFE;
- Certificado digital expirado;
- Bloqueios de Firewall e/ou anti-vírus.

No cenário acima, o método de 'Envio em Contingência' definido nas preferências da empresa será acionado, e se esse não encontrar-se disponível na respectiva SEFAZ, a mensagem será apresentada. Dessa forma proceder com a solução de acordo com o cenário atual:

![Imagem 3: Caso não se trate de uma indisponibilidade da SEFAZ, avaliar os outros pontos citados com apoio do T.I da empresa, de…](https://ajuda.sankhya.com.br/hc/article_attachments/16120718420759) Caso não se trate de uma indisponibilidade da SEFAZ, avaliar os outros pontos citados com apoio do T.I da empresa, de forma que a emissão em ambiente 'Normal' seja restabelecida. 

![Imagem 4: Caso a emissão em ambiente normal não seja restabelecida, sintonize com o contador da empresa se a mesma é autorizada a…](https://ajuda.sankhya.com.br/hc/article_attachments/16120718426903) Caso a emissão em ambiente normal não seja restabelecida, sintonize com o contador da empresa se a mesma é autorizada a emitir tais notas em EPEC. Em caso positivo e seja válido para o cenário atual, ajuste a configuração abaixo para **"Envio em Contingência: SVC/EPEC":**

Escolhendo esta opção, se o SVC não estiver ativo, o sistema irá marcar as notas como EPEC, numerar as notas com a série da SEFAZ e enviar em EPEC, mas se o SVC estiver ativo, ele irá numerar as notas com a série do SVC e enviar;

- Acesse a tela **"Empresa"** (Caminho de acesso: Comercial » Preferências » Empresa);
- Na aba **NF-e/NFC-e** verifique a parametrização atual do campo Envio em Contingência:

![Imagem 5: Na aba NF-e/NFC-e verifique a parametrização atual do campo Envio em Contingência :](https://ajuda.sankhya.com.br/hc/article_attachments/14637629713687)

Para mais detalhes de como regularizar/tratar as notas emitidas em EPEC, verifique o artigo: [Nota Fiscal Eletrônica status 'Enviada em Ambiente de Contingência'(EPEC).Como funciona?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626354)

![Imagem 6: Caso o ambiente 'Normal' da SEFAZ esteja em operação e as análises citadas acima tenham sido realizadas sem sucesso,…](https://ajuda.sankhya.com.br/hc/article_attachments/16120689200407) Caso o ambiente 'Normal' da SEFAZ esteja em operação e as análises citadas acima tenham sido realizadas sem sucesso, acione o Service Desk Sankhya Jiva reportando os detalhes analisados. 

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120689202071) CAUSA:**

Mensagem apresentada quando não for possível estabelecer comunicação com o ambiente 'Normal' da SEFAZ e o ambiente definido para Envio em Contingência não estiver ativo.
