---
id: "39322397312919"
titulo: "Impressão NFC-e no PDV Web sem corte automático"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39322397312919-Impress%C3%A3o-NFC-e-no-PDV-Web-sem-corte-autom%C3%A1tico"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T13:55:45Z"
rotulos: ["Configuração", "Impressão", "Preferências", "NFC-e", "PDV Web", "Artigo criado KCS", "Varejo - KCS"]
---

# Impressão NFC-e no PDV Web sem corte automático

**MENSAGEM**

Após a impressão da NFC-e pelo PDV Web, a impressora térmica não realiza o corte automático do cupom, sendo necessário realizar o corte manualmente.

**SITUAÇÃO**

Ao realizar a impressão de NFC-e através do PDV Web, o sistema efetua a impressão do cupom fiscal corretamente, porém não executa o corte automático do papel ao final da impressão. Esse comportamento obriga o operador de caixa a realizar o corte manual do comprovante, impactando a agilidade do atendimento e a experiência do cliente.

**SOLUÇÃO**

Para resolver o problema de corte automático nas impressoras térmicas, siga os passos abaixo:

**(1)**Acesse a tela **Preferências (Configurações » Avançado » Preferências).**

**(2)**Localize o parâmetro **"Ativar corte após cupom impr. Bematech? - CUTBEMATECHENB"**.

**(3)**Altere o campo "Ligado/Desligado" para Ligado.

![Imagem 1: Salve as alterações realizadas no parâmetro. Realize um teste de impressão de NFC-e através do PDV Web para validar se…](https://ajuda.sankhya.com.br/hc/article_attachments/41599378848279)

**(4)**Salve as alterações realizadas no parâmetro.

**(5)**Realize um teste de impressão de NFC-e através do **PDV Web** para validar se o corte automático está funcionando corretamente.

Após a ativação do **"CUTBEMATECHENB"**, o comportamento será normalizado, permitindo que a impressora execute o corte automático após cada impressão de cupom fiscal.

**CAUSA**

O comportamento ocorre porque o parâmetro "CUTBEMATECHENB" estava desativado no sistema.

Alguns modelos de impressoras térmicas utilizam comandos específicos para executar o corte automático do papel. Ao habilitar esse parâmetro, o sistema passa a enviar o comando de corte compatível com esses modelos ao final da impressão, permitindo que o corte do papel seja realizado automaticamente após a emissão da NFC-e.
