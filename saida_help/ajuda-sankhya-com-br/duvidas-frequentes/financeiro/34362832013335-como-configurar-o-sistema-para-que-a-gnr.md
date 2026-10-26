---
id: "34362832013335"
titulo: "Como configurar o sistema para que a GNRE não seja gerada automaticamente na devolução de uma venda?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34362832013335-Como-configurar-o-sistema-para-que-a-GNRE-n%C3%A3o-seja-gerada-automaticamente-na-devolu%C3%A7%C3%A3o-de-uma-venda"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:27:16Z"
rotulos: ["Configuração", "Movimentação Financeira", "GNRE", "Preferências", "Financeiro", "configurar o sistema", "devolução de uma venda", "GNRE não seja gerada automaticamente"]
---

# Como configurar o sistema para que a GNRE não seja gerada automaticamente na devolução de uma venda?

**SITUAÇÃO**

Em determinados cenários, é necessário que a GNRE não seja gerada automaticamente na devolução de uma venda. Para garantir esse comportamento, é preciso validar as configurações do sistema.

**SOLUÇÃO**

**(1)**  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

**(2)**  Localize o parâmetro **"REMOVEGNREDEV – Remove GNRE para devolução de notas que tiveram GNRE na origem?"**.

**(3)**  Certifique-se de que o parâmetro **REMOVEGNREDEV** esteja habilitado.

![Imagem 1: (1) Acesse a tela "Preferências" (Configurações » Avançado » Preferências). (2) Localize o parâmetro "REMOVEGNREDEV –…](https://ajuda.sankhya.com.br/hc/article_attachments/34362832008855)

**(4)**  Verifique o **"Tipo de Negociação"** (Comercial » Arquivo » Cadastros » Tipos de Negociação).

**(5)**  Caso exista uma fórmula configurada para geração da linha de GNRE no financeiro, inclua uma condição para tratar especificamente os movimentos de devolução, conforme exemplo:

**IF(queTGFCAB.TIPMOV = 'D', ' ', VLRICMSDIFALDEST)**

Nesse caso, quando o movimento for de devolução (**TIPMOV = 'D'**), a linha de GNRE não será gerada.

**CAUSA**

Esse comportamento ocorre quando o parâmetro **REMOVEGNREDEV** não está habilitado e não há validação na fórmula para impedir a geração da GNRE em notas de devolução.
