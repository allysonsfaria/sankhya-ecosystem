---
id: "26620389599639"
titulo: "Campo de desconto no rodapé nas centrais não está habilitado para digitação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26620389599639-Campo-de-desconto-no-rodap%C3%A9-nas-centrais-n%C3%A3o-est%C3%A1-habilitado-para-digita%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-03T14:41:35Z"
rotulos: ["Configuração", "NF-e", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Campo de desconto no rodapé não está habilitado", "Artigo atualizado KCS", "CVE - KCS"]
---

# Campo de desconto no rodapé nas centrais não está habilitado para digitação

O rodapé da **"Central de Compras"** (Configurações >> Cadastros >> Parceiros) exibe informações importantes sobre os totais do pedido, incluindo valores de desconto, seguro, frete e outros campos financeiros. Quando o campo de desconto não está habilitado para digitação no rodapé, isso geralmente está relacionado à configuração de um parâmetro específico do sistema.

**SITUAÇÃO**

Campo de desconto no rodapé nas centrais não está habilitado para digitação.

![Imagem 1: Campo de desconto no rodapé nas centrais não está habilitado para digitação.](https://ajuda.sankhya.com.br/hc/article_attachments/26620389583767)

**CAUSA**

Esse problema ocorre quando o parâmetro **"DESCTOT - Aceita desconto no pé da nota"** está desligado.

**SOLUÇÃO**

Para que o campo de desconto fique disponível para edição no rodapé das centrais de compras, siga os passos abaixo:

**(1)** Acesse a tela de **"Parâmetros do Sistema"** (Configurações >> Avançado >> Parâmetros do Sistema).
**(2)** Localize o parâmetro **"DESCTOT - Aceita desconto no pé da nota"**.
**(3)** Altere o status do parâmetro **"DESCTOT"** para **"Ligado"**.
**(4)** Salve as alterações realizadas.
**(5)** Saia da tela da **"Central de Compras"** (Comercial >> Consulta >> Central de Compras).
**(6)** Entre novamente na **"Central de Compras"** para que as alterações sejam aplicadas.
